from pathlib import Path
import re
from os import linesep, makedirs
from typing import Tuple

website_path = Path("/home/jh/jac08h.github.io")
website_quotes = Path(website_path, "book_quotes")
original_quotes = Path("/home/jh/books/quotes")

metadata_pattern = re.compile(r"(\d+)_(.+)__(.+)")


def create_markdown_quotes(original_dir: Path, new_dir: Path) -> None:
    for file in original_dir.iterdir():
        year, author, title = get_metadata(file)
        year_dir = Path(new_dir, str(year))
        makedirs(year_dir, exist_ok=True)

        quote = file.read_text()
        markdown = create_markdown_text(author, title, quote)

        markdown_file = Path(new_dir, str(year), file.stem + ".md")
        if not markdown_file.exists():
            markdown_file.write_text(markdown)


def get_metadata(quote_filename: Path) -> Tuple[int, str, str]:
    metadata = metadata_pattern.match(quote_filename.stem)
    year_s, author, title = metadata.groups()
    year = int(year_s) + 2000
    title = title.replace("_", " ")
    return year, author, title


def create_markdown_text(author: str, title: str, quote: str) -> str:
    header = f"""## {author} - {title}"""
    return header + linesep + linesep + quote


if __name__ == '__main__':
    create_markdown_quotes(original_quotes, website_quotes)
