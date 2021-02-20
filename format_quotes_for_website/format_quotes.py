from pathlib import Path
import re
from os import linesep, makedirs
from shutil import rmtree
from typing import Tuple, Optional
from datetime import datetime as dt

website_path = Path("/home/jh/jac08h.github.io")
website_quotes = Path(website_path, "book_quotes")
original_quotes = Path("/home/jh/books/quotes")

metadata_pattern = re.compile(r"(\d+)_(.+)__(.+)")


def create_markdown_quotes(original_dir: Path, new_dir: Path, dont_update_current_year: Optional[bool] = True) -> None:
    current_year = dt.now().year
    for file in original_dir.iterdir():
        year, author, title = get_metadata(file)
        year = int(year)
        if dont_update_current_year and year == current_year:
            continue

        year_dir = Path(new_dir, str(year))
        makedirs(year_dir, exist_ok=True)

        quote = file.read_text()
        markdown = create_markdown_text(author, title, year, quote)
        markdown_file = Path(new_dir, str(year), file.stem + ".md")
        if not markdown_file.exists():
            markdown_file.write_text(markdown)


def get_metadata(quote_filename: Path) -> Tuple[int, str, str]:
    metadata = metadata_pattern.match(quote_filename.stem)
    year_s, author, title = metadata.groups()
    year = int(year_s) + 2000
    title = title.replace("_", " ")
    return year, author, title


def create_markdown_text(author: str, title: str, year: int, quote: str) -> str:
    header = f"""## {author} - {title}"""
    year_line = f"###### {year}"
    return header + linesep + linesep + quote + linesep + linesep + year_line


def generate_quotes_page(quotes_directory: Path, dont_update_current_year: Optional[bool] = True) -> None:
    current_year = dt.now().year
    for year_directory in sorted(quotes_directory.iterdir()):
        if not year_directory.is_dir():
            continue
        year = int(year_directory.stem)
        if dont_update_current_year and current_year == year:
            continue

        year_file = Path(quotes_directory, str(year) + ".md")
        quote_paths = sorted([q for q in year_directory.iterdir() if q.is_file() and q.suffix == ".md"])
        list_elements = []
        for quote_path in quote_paths:
            year, author, title = get_metadata(quote_path)
            list_elements.append(f"* [{author} - {title}](/book_quotes/{year}/{quote_path.stem})")

        year_file.write_text(linesep.join(list_elements))


def generate_random_quote_page(quotes_directory: Path):
    all_quotes = []
    for child in quotes_directory.iterdir():
        if child.is_dir():
            all_quotes += list(child.iterdir())
    quotes_directory_path_length = len(quotes_directory.__str__())
    all_quotes = [i.__str__()[quotes_directory_path_length + 1:-3] for i in all_quotes]

    random_path = Path(quotes_directory, "random.html")
    # note escaped '{' and '}'
    random_js = f"""<script>
      <!-- Inspired by https://derekkedziora.com/blog/Getting-Random-Post-in-Jekyll -->

      const allQuotes = {all_quotes}

      function linkToRandomQuote() {{
          const randomQuoteLink = allQuotes[Math.floor(Math.random() * allQuotes.length)];
          return randomQuoteLink;
      }}

      location.replace(linkToRandomQuote())
    </script>

    <noscript>
      <h1>Javascript is Disabled</h1>
      <p>To get to a random post, turn on JavaScript.</p>
    </noscript>"""
    random_path.write_text(random_js)


if __name__ == '__main__':
    rmtree(website_quotes)
    create_markdown_quotes(original_quotes, website_quotes)
    generate_quotes_page(website_quotes, True)
    generate_random_quote_page(website_quotes)
