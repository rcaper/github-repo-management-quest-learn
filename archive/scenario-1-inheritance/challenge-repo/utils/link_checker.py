"""
Link Checker Utility for TechFlow Documentation

This script checks all markdown files for broken links.
"""

import os
import re
from pathlib import Path
from urllib.parse import urlparse
import requests


class LinkChecker:
    """Check markdown files for broken internal and external links."""

    def __init__(self, docs_dir):
        self.docs_dir = Path(docs_dir)
        self.broken_links = []
        self.checked_urls = {}

    def find_markdown_files(self):
        """Find all markdown files in the documentation directory."""
        return list(self.docs_dir.rglob("*.md"))

    def extract_links(self, file_path):
        """Extract all links from a markdown file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find markdown links: [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        links = re.findall(link_pattern, content)

        return [(text, url) for text, url in links]

    def check_internal_link(self, base_file, link_url):
        """Check if an internal link (relative path) exists."""
        # Remove anchor
        path_part = link_url.split('#')[0]
        if not path_part:
            return True  # Anchor-only links are OK

        # Resolve relative path
        base_dir = base_file.parent
        target_path = (base_dir / path_part).resolve()

        return target_path.exists()

    def check_external_link(self, url):
        """Check if an external URL is accessible."""
        # Use cache to avoid checking same URL multiple times
        if url in self.checked_urls:
            return self.checked_urls[url]

        try:
            response = requests.head(url, timeout=5, allow_redirects=True)
            is_valid = response.status_code < 400
            self.checked_urls[url] = is_valid
            return is_valid
        except:
            self.checked_urls[url] = False
            return False

    def check_file(self, file_path):
        """Check all links in a file."""
        links = self.extract_links(file_path)

        for link_text, link_url in links:
            parsed = urlparse(link_url)

            if parsed.scheme in ['http', 'https']:
                # External link
                if not self.check_external_link(link_url):
                    self.broken_links.append({
                        'file': str(file_path),
                        'link_text': link_text,
                        'url': link_url,
                        'type': 'external'
                    })
            elif not parsed.scheme:
                # Internal link
                if not self.check_internal_link(file_path, link_url):
                    self.broken_links.append({
                        'file': str(file_path),
                        'link_text': link_text,
                        'url': link_url,
                        'type': 'internal'
                    })

    def run(self):
        """Run the link checker on all markdown files."""
        print(f"Checking links in {self.docs_dir}...")

        md_files = self.find_markdown_files()
        print(f"Found {len(md_files)} markdown files")

        for file_path in md_files:
            print(f"Checking {file_path.name}...")
            self.check_file(file_path)

        return self.broken_links

    def report(self):
        """Generate a report of broken links."""
        if not self.broken_links:
            print("\n✅ No broken links found!")
            return

        print(f"\n❌ Found {len(self.broken_links)} broken links:\n")

        for link in self.broken_links:
            print(f"File: {link['file']}")
            print(f"  Text: {link['link_text']}")
            print(f"  URL: {link['url']}")
            print(f"  Type: {link['type']}")
            print()


def main():
    """Main entry point."""
    # TODO: Add command-line argument parsing
    docs_dir = "../docs"

    checker = LinkChecker(docs_dir)
    checker.run()
    checker.report()


if __name__ == "__main__":
    main()
