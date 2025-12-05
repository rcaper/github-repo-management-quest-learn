"""
Markdown Format Validator

Checks markdown files for common formatting issues.
"""

import re
from pathlib import Path


class MarkdownValidator:
    """Validate markdown files for formatting issues."""

    def __init__(self):
        self.issues = []

    def check_heading_hierarchy(self, file_path, content):
        """Check that headings follow proper hierarchy (no skipped levels)."""
        lines = content.split('\n')
        heading_pattern = r'^(#{1,6})\s+(.+)$'

        previous_level = 0
        for line_num, line in enumerate(lines, 1):
            match = re.match(heading_pattern, line)
            if match:
                current_level = len(match.group(1))

                # Check if we skipped a level
                if current_level > previous_level + 1 and previous_level > 0:
                    self.issues.append({
                        'file': str(file_path),
                        'line': line_num,
                        'type': 'heading_hierarchy',
                        'message': f'Heading level skipped from H{previous_level} to H{current_level}',
                        'severity': 'medium'
                    })

                previous_level = current_level

    def check_code_blocks(self, file_path, content):
        """Check that code blocks specify a language."""
        lines = content.split('\n')

        for line_num, line in enumerate(lines, 1):
            # Check for code blocks without language specification
            if line.strip() == '```':
                self.issues.append({
                    'file': str(file_path),
                    'line': line_num,
                    'type': 'code_block',
                    'message': 'Code block missing language specifier',
                    'severity': 'low'
                })

    def check_list_formatting(self, file_path, content):
        """Check for inconsistent list formatting."""
        lines = content.split('\n')
        list_pattern = r'^(\s*)([-*+]|\d+\.)\s+(.+)$'

        current_list_marker = None
        for line_num, line in enumerate(lines, 1):
            match = re.match(list_pattern, line)
            if match:
                marker = match.group(2)

                # Skip numbered lists
                if marker[-1] == '.':
                    continue

                if current_list_marker and marker != current_list_marker:
                    self.issues.append({
                        'file': str(file_path),
                        'line': line_num,
                        'type': 'list_formatting',
                        'message': f'Inconsistent list marker: using {marker} but previously used {current_list_marker}',
                        'severity': 'low'
                    })

                if current_list_marker is None:
                    current_list_marker = marker
            elif line.strip() == '':
                current_list_marker = None

    def check_link_formatting(self, file_path, content):
        """Check for link formatting issues."""
        # Check for 'click here' or similar non-descriptive link text
        bad_link_text = r'\[(?:click here|here|link|this)\]\('

        matches = re.finditer(bad_link_text, content, re.IGNORECASE)
        for match in matches:
            # Find line number
            line_num = content[:match.start()].count('\n') + 1

            self.issues.append({
                'file': str(file_path),
                'line': line_num,
                'type': 'link_text',
                'message': 'Link uses non-descriptive text (click here, here, link, this)',
                'severity': 'medium'
            })

    def check_trailing_whitespace(self, file_path, content):
        """Check for trailing whitespace."""
        lines = content.split('\n')

        for line_num, line in enumerate(lines, 1):
            if line.rstrip() != line and line.strip():  # Has trailing space
                self.issues.append({
                    'file': str(file_path),
                    'line': line_num,
                    'type': 'trailing_whitespace',
                    'message': 'Line has trailing whitespace',
                    'severity': 'low'
                })

    def validate_file(self, file_path):
        """Validate a single markdown file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.check_heading_hierarchy(file_path, content)
        self.check_code_blocks(file_path, content)
        self.check_list_formatting(file_path, content)
        self.check_link_formatting(file_path, content)
        self.check_trailing_whitespace(file_path, content)

    def validate_directory(self, directory):
        """Validate all markdown files in a directory."""
        docs_dir = Path(directory)
        md_files = list(docs_dir.rglob("*.md"))

        print(f"Validating {len(md_files)} markdown files...\n")

        for file_path in md_files:
            self.validate_file(file_path)

    def report(self):
        """Generate a validation report."""
        if not self.issues:
            print("✅ No formatting issues found!\n")
            return

        print(f"❌ Found {len(self.issues)} formatting issues:\n")

        # Group by severity
        by_severity = {'critical': [], 'high': [], 'medium': [], 'low': []}
        for issue in self.issues:
            by_severity[issue['severity']].append(issue)

        for severity in ['critical', 'high', 'medium', 'low']:
            issues = by_severity[severity]
            if not issues:
                continue

            print(f"{severity.upper()} ({len(issues)} issues):")
            for issue in issues:
                print(f"  {issue['file']}:{issue['line']}")
                print(f"    {issue['message']}")
            print()


def main():
    """Main entry point."""
    validator = MarkdownValidator()
    validator.validate_directory("../docs")
    validator.report()


if __name__ == "__main__":
    main()
