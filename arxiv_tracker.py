#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    ArXiv Paper Tracker

    This script periodically tracks and retrieves new papers from arXiv based on a configurable search query.
    It filters out previously known papers and stores the results in JSON format. The results can be saved to
    a README.md file and HTML pages (index and archive). It also generates Markdown summaries for new papers.

    The script uses the arXiv API and handles the retrieval, storage, and display of relevant papers based on
    specific search criteria. It is ideal for monitoring research progress in particular domains like materials
    discovery or generative models.

    Features:
    - Search for new papers on arXiv based on a configurable query
    - Filter out previously known papers
    - Store new papers in JSON format and save the results in an organized manner
    - Update the README.md file with new papers
    - Generate HTML and Markdown pages for the papers
    - Archive the results for long-term tracking and visualization

    Dependencies:
    - `arxiv` Python package
    - `json`
    - `argparse`
    - `logging`

    Author: Wang Jianghai@NTU (Ocean-JH)
    GitHub: https://github.com/Ocean-JH/ArXivDaily-AI4MAT
    Date: 2025-07-16
"""
import os
import datetime
import html
import json
import argparse
import logging
import re
from typing import List, Dict, Any, Optional

import arxiv


# Configure logging  
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("arxiv-tracker")
SGT = datetime.timezone(datetime.timedelta(hours=8))
VERSIONED_ARXIV_ID = re.compile(r"^(?P<base>.+?)v(?P<version>\d+)$")


class ArxivTracker:
    """Periodically track new papers on arXiv"""

    def __init__(self,
                 query: str,
                 max_results: int = 200,
                 output_dir: str = "./data/results",
                 known_papers_file: str = "./data/known_papers.json",
                 templates_dir: str = "./templates"):
        """
        Initialize ArxivMonitor

        Parameters:
            query: Search query string
            max_results: Maximum number of results per search
            output_dir: Directory to save results
            known_papers_file: File to store known paper IDs
            templates_dir: Directory for HTML templates
        """
        self.query = query
        self.max_results = max_results
        self.output_dir = output_dir
        self.known_papers_file = known_papers_file
        self.templates_dir = templates_dir
        self.known_papers = self._load_known_papers()
        self.client = arxiv.Client(
            page_size=500,
            delay_seconds=5.0
        )

        # Create directories
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.dirname(known_papers_file), exist_ok=True)
        os.makedirs(templates_dir, exist_ok=True)

    def _load_known_papers(self) -> dict:
        """Load the set of known papers from file"""
        if os.path.exists(self.known_papers_file):
            try:
                with open(self.known_papers_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return {str(k): int(v) for k, v in data.items()}
            except FileNotFoundError as e:
                logger.error(f"Known papers file not found: {e}")
                return {}
        return {}

    def _save_known_papers(self):
        """Save the set of known papers to file"""
        try:
            with open(self.known_papers_file, 'w', encoding='utf-8') as f:
                json.dump(self.known_papers, f)
        except Exception as e:
            logger.error(f"Error saving known papers: {e}")

    def search_papers(self) -> List[arxiv.Result]:
        """Execute search and return results"""
        search = arxiv.Search(
            query=self.query,
            max_results=self.max_results,
            sort_by=arxiv.SortCriterion.LastUpdatedDate,
            sort_order=arxiv.SortOrder.Descending
        )

        results = list(self.client.results(search))
        return results

    def _get_base_id(self, short_id: str):
        """Extract base ID from short ID (removing version)"""
        match = VERSIONED_ARXIV_ID.match(short_id)
        return match.group("base") if match else short_id

    def _get_version(self, short_id: str):
        """Extract version from short ID"""
        match = VERSIONED_ARXIV_ID.match(short_id)
        return int(match.group("version")) if match else 1

    def _html(self, value: Any) -> str:
        """Escape generated content before inserting it into static HTML."""
        return html.escape("" if value is None else str(value), quote=True)

    def _paper_base_id(self, paper: Dict[str, Any]) -> str:
        """Return the stable arXiv ID without the version suffix."""
        if paper.get("base_id"):
            return str(paper["base_id"])

        paper_id = paper.get("id") or paper.get("url") or ""
        short_id = str(paper_id).rstrip("/").split("/")[-1]
        return self._get_base_id(short_id)

    def _paper_version(self, paper: Dict[str, Any]) -> int:
        """Return a comparable paper version from saved result data."""
        try:
            return int(paper.get("version", 1))
        except (TypeError, ValueError):
            short_id = str(paper.get("id") or paper.get("url") or "").rstrip("/").split("/")[-1]
            return self._get_version(short_id)

    def _dedupe_papers(self, papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Keep only the latest saved version for each arXiv base ID."""
        latest_papers: Dict[str, Dict[str, Any]] = {}

        for paper in papers:
            base_id = self._paper_base_id(paper)
            current = latest_papers.get(base_id)

            if current is None:
                latest_papers[base_id] = paper
                continue

            paper_key = (self._paper_version(paper), paper.get("updated", ""))
            current_key = (self._paper_version(current), current.get("updated", ""))
            if paper_key > current_key:
                latest_papers[base_id] = paper

        return list(latest_papers.values())

    def paper_to_dict(self, paper: arxiv.Result) -> Dict[str, Any]:
        """Convert paper object to dictionary for saving"""
        return {
            "id": paper.entry_id,
            "title": paper.title,
            "authors": [str(author) for author in paper.authors],
            "summary": paper.summary,
            "published": paper.published.isoformat(),
            "updated": paper.updated.isoformat(),
            "categories": paper.categories,
            "primary_category": paper.primary_category,
            "comment": paper.comment,
            "journal_ref": paper.journal_ref,
            "doi": paper.doi,
            "pdf_url": paper.pdf_url,
            "base_id": self._get_base_id(paper.get_short_id()),
            "version": str(self._get_version(paper.get_short_id())),
            "url": paper.entry_id
        }

    def filter_new_papers(self, papers: List[arxiv.Result]) -> List[Dict[str, Any]]:
        """Filter out papers we've already seen"""
        new_papers = []
        latest_results = {}

        for paper in papers:
            base_id = self._get_base_id(paper.get_short_id())
            version = self._get_version(paper.get_short_id())
            existing = latest_results.get(base_id)
            if existing is None or version > self._get_version(existing.get_short_id()):
                latest_results[base_id] = paper

        for base_id, paper in latest_results.items():
            version = self._get_version(paper.get_short_id())
            prev_version = self.known_papers.get(base_id, 0)
            if version > prev_version:
                tag = "new" if prev_version == 0 else "update"
                new_papers.append({
                    "paper": paper,
                    "tag": tag,
                    "base_id": base_id,
                    "version": version,
                })
                self.known_papers[base_id] = version
        return new_papers

    def save_results(self, papers: List[Dict[str, Any]], timestamp: str) -> Optional[str]:
        """Save results to file"""
        if not papers:
            return None

        filename = f"arxiv_results_{timestamp}.json"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump([self.paper_to_dict(paper["paper"]) for paper in papers], f,
                      ensure_ascii=False, indent=2)

        return filepath

    def generate_markdown(self, papers: List[arxiv.Result], is_new: bool = False) -> str:
        """Generate markdown for papers"""
        if not papers:
            md = f"## 🥳 No new papers today. Take it easy and recharge!"
            md += f"*Last updated: {datetime.datetime.now(SGT).strftime('%Y-%m-%d %H:%M:%S')} (SGT)*\n\n"
        else:
            status = "New " if is_new else ""
            md = f"## {status}Papers ({len(papers)})\n\n"
            md += f"*Last updated: {datetime.datetime.now(SGT).strftime('%Y-%m-%d %H:%M:%S')} (SGT)*\n\n"

            for i, paper in enumerate(papers):
                md += f"### {i + 1}. {paper.title}\n\n"
                md += f"**Authors:** {', '.join(str(author) for author in paper.authors)}\n\n"
                md += f"**Published:** {paper.published.strftime('%Y-%m-%d')}\n\n"
                md += f"**Category:** {paper.primary_category}\n\n"
                md += f"**ID:** {paper.get_short_id()}\n\n"
                md += f"**Link:** [{paper.entry_id}]({paper.entry_id})\n\n"
                md += f"**Summary:** {paper.summary}...\n\n"
                md += "---\n\n"

        return md

    def update_readme(self, papers: List[Dict[str, Any]], readme_path: str = "README.md"):
        """Update the README.md with new papers"""
        papers = [paper['paper'] for paper in papers]  # Extract arxiv.Result objects
        # Generate markdown for new papers
        new_papers_md = self.generate_markdown(papers, is_new=True)

        # Read existing README  
        readme_content = ""
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                readme_content = f.read()

                # Find the section marker or create it
        section_marker = "<!-- ARXIV_PAPERS_START -->"
        end_marker = "<!-- ARXIV_PAPERS_END -->"

        if section_marker in readme_content and end_marker in readme_content:
            # Replace the section  
            start_idx = readme_content.find(section_marker)
            end_idx = readme_content.find(end_marker) + len(end_marker)
            readme_content = (
                    readme_content[:start_idx] +
                    section_marker + "\n\n" +
                    new_papers_md +
                    "\n" + end_marker +
                    readme_content[end_idx:]
            )
        else:
            # Add the section at the end  
            if readme_content:
                readme_content += "\n\n"
            readme_content += f"{section_marker}\n\n{new_papers_md}\n{end_marker}"

            # Write updated README
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        logger.info(f"Updated README with {len(papers)} new papers")

    def generate_html(self, papers: List[arxiv.Result], is_new: bool = False) -> str:
        """Generate HTML for papers"""
        if not papers:
            return f"<div class='notice'>🥳 No new papers today<br>Enjoy the break!</div>"

        with open("templates/paper_item.html", 'r', encoding='utf-8') as f:
            paper_template = f.read()

        status = "New " if is_new else ""
        html = f"<h2>{status}Papers ({len(papers)})</h2>\n"
        html += f"<p><em>Last updated: {datetime.datetime.now(SGT).strftime('%Y-%m-%d %H:%M:%S')} SGT</em></p>\n"

        for i, paper in enumerate(papers):
            if self._get_version(paper.get_short_id()) == 1:
                tag_html = " <span class='paper-badge'>New</span>"
            else:
                tag_html = " <span class='paper-badge updated'>Updated</span>"

            paper_html = paper_template.format(
                index=i + 1,
                title=self._html(paper.title),
                authors=self._html(", ".join(str(author) for author in paper.authors)),
                published_date=self._html(paper.published.strftime("%Y-%m-%d")),
                category=self._html(paper.primary_category),
                paper_id=self._html(paper.get_short_id()),
                url=self._html(paper.entry_id),
                summary=self._html(paper.summary),
                tag=tag_html
            )
            html += paper_html

        return html

    def load_base_template(self) -> str:
        """Load the base HTML template"""
        with open("templates/base.html", 'r', encoding='utf-8') as f:
            return f.read()

    def create_index_html(self, papers: List[Dict[str, Any]], output_path: str = "index.html"):
        """Create an index.html file with new papers"""
        html_template = self.load_base_template()
        navbar = """
    <div class="nav">
        <strong>Latest Papers</strong> | <a href="archive.html">View Archive</a>
    </div>
    """
        papers = [paper['paper'] for paper in papers]  # Extract arxiv.Result objects
        # Generate HTML content for papers
        content = self.generate_html(papers, is_new=True)

        # Fill in the template
        html_content = html_template.format(
            title="ArXiv Daily - Latest Papers",
            content=content,
            navbar=navbar,
            timestamp=datetime.datetime.now(SGT).strftime("%Y-%m-%d %H:%M:%S") + " (SGT)"
        )

        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        logger.info(f"Created index.html with {len(papers)} papers")

    def create_archive_html(self, output_path: str = "archive.html"):
        """Create an archive.html file with all known papers"""
        # Load all saved results
        all_papers = []
        results_files = sorted(f for f in os.listdir(self.output_dir) if f.endswith('.json'))
        navbar = """
    <div class="nav">
        <a href="index.html">Latest Papers</a> | <strong>Archive</strong>
    </div>
    """

        for file in results_files:
            try:
                with open(os.path.join(self.output_dir, file), 'r', encoding='utf-8') as f:
                    papers_data = json.load(f)
                    all_papers.extend(papers_data)
            except Exception as e:
                logger.error(f"Error loading results file {file}: {e}")

        all_papers = self._dedupe_papers(all_papers)
        all_papers.sort(key=lambda p: (p.get('published', ''), p.get('updated', '')), reverse=True)

        with open("templates/paper_item.html", 'r', encoding='utf-8') as f:
            paper_template = f.read()

            # Generate HTML content
        content = "<h2>All Papers</h2>\n"
        content += f"<p><em>Total: {len(all_papers)} papers</em></p>\n"

        for i, paper in enumerate(all_papers):
            paper_html = paper_template.format(
                index=i + 1,
                title=self._html(paper.get("title", "")),
                authors=self._html(", ".join(paper.get("authors", []))),
                published_date=self._html(paper.get("published", "")[:10]),
                category=self._html(paper.get("primary_category", "")),
                paper_id=self._html(f"{self._paper_base_id(paper)}v{self._paper_version(paper)}"),
                url=self._html(paper.get("url", "")),
                summary=self._html(paper.get("summary", "")),
                tag=""
            )
            content += paper_html

        # Fill in the template (reuse the same template as index.html)
        html_template = self.load_base_template()

        html_content = html_template.format(
            title="ArXiv Daily - Archive",
            content=content,
            navbar=navbar,
            timestamp=datetime.datetime.now(SGT).strftime("%Y-%m-%d %H:%M:%S") + " (SGT)"
        )

        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        logger.info(f"Created archive.html with {len(all_papers)} unique papers")

    def run(self, update_readme: bool = True, create_html: bool = True):
        """Run the tracker once"""
        timestamp = datetime.datetime.now(SGT).strftime("%Y%m%d_%H%M%S")
        logger.info(f"Searching for: {self.query}")

        try:
            # Get papers
            papers = self.search_papers()
            logger.info(f"Found {len(papers)} papers in total")

            # Filter new papers
            new_papers = self.filter_new_papers(papers)
            logger.info(f"Found {len(new_papers)} new papers")

            if new_papers:
                # Save results
                filepath = self.save_results(new_papers, timestamp)
                if filepath:
                    logger.info(f"Results saved to: {filepath}")

                    # Update README if requested
                if update_readme:
                    self.update_readme(new_papers)

                if create_html:
                    self.create_index_html(new_papers)
                    self.create_archive_html()
            else:
                if create_html:
                    self.create_index_html(new_papers)
                    self.create_archive_html()

                    # Save known papers
            self._save_known_papers()

            return new_papers

        except Exception as e:
            logger.error(f"Error during search: {e}", exc_info=True)
            return []


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="arXiv Paper Tracker")
    parser.add_argument("--config", type=str, default="config.json", help="Path to config file")
    parser.add_argument("--query", type=str, help="Search query (overrides config)")
    parser.add_argument("--max-results", type=int, help="Maximum results (overrides config)")
    parser.add_argument("--no-readme", action="store_true", help="Don't update README")
    args = parser.parse_args()

    # Load config  
    config = {
        "query": "(cat:cond-mat.mtrl-sci OR cat:cs.AI OR cat:cs.LG) AND (all:\"materials design\" OR all:\"materials discovery\" OR all:\"inverse design\") AND (all:\"generative\" OR all:\"crystal structure prediction\")",
        "max_results": 500,
        "output_dir": "./data/results",
        "known_papers_file": "./data/known_papers.json"
    }

    if os.path.exists(args.config):
        try:
            with open(args.config, 'r', encoding='utf-8') as f:
                config.update(json.load(f))
        except Exception as e:
            logger.error(f"Error loading config: {e}")

            # Override with command line arguments
    if args.query:
        config["query"] = args.query
    if args.max_results:
        config["max_results"] = args.max_results

        # Create and run Tracker
    tracker = ArxivTracker(
        query=config["query"],
        max_results=config["max_results"],
        output_dir=config["output_dir"],
        known_papers_file=config["known_papers_file"]
    )

    tracker.run(update_readme=not args.no_readme)


if __name__ == "__main__":
    main()
