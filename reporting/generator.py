# reporting/generator.py

import pandas as pd

class ReportGenerator:
    """A helper class to generate Markdown reports."""

    def __init__(self, title: str, introduction: str):
        self.content = f"# {title}\n\n{introduction}\n\n"

    def add_section(self, title: str, level: int = 2):
        """Adds a new section header."""
        self.content += f"{'#' * level} {title}\n\n"

    def add_question(self, question_number: str, question_text: str):
        """Adds a formatted question block."""
        self.content += f"### Question {question_number}: {question_text}\n\n"

    def add_text(self, text: str):
        """Adds a paragraph of text."""
        self.content += f"{text}\n\n"

    def add_code_block(self, code: str, language: str = 'python'):
        """Adds a formatted code block."""
        self.content += f"``` {language}\n{code}\n```\n\n"

    def add_table(self, dataframe: pd.DataFrame, title: str = None):
        """Adds a markdown table from a pandas DataFrame."""
        if title:
            self.content += f"**{title}**\n\n"
        if dataframe.empty:
            self.content += "No data to display.\n\n"
        else:
            self.content += dataframe.to_markdown(index=False) + "\n\n"

    def add_image(self, title: str, image_path: str):
        """Adds a markdown image link."""
        self.content += f"**{title}**\n\n"
        self.content += f"![{title}]({image_path})\n\n"

    def save_report(self, file_path: str):
        """Saves the generated report content to a file."""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(self.content)
        print(f"Report successfully saved to {file_path}")


