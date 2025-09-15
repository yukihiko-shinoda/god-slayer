"""ReadOperator for skip header."""

from __future__ import annotations

from typing import Generator
from typing import Iterator

from godslayer.csv.reader_operators.reader_operator import ReaderOperator
from godslayer.exceptions import InvalidHeaderError
from godslayer.list_string_matcher import ListStringMatcher


class HeaderSkipper(ReaderOperator):
    """ReadOperator for skip header."""

    def __init__(self, header: list[str]) -> None:
        super().__init__()
        self.header = header

    def process(self, reader_input: Iterator[list[str]]) -> Generator[list[str], None, None]:
        yield from super().process(reader_input)
        for self._index, list_input_row_standard_type_value in enumerate(reader_input):
            if ListStringMatcher.is_matched(self.header, list_input_row_standard_type_value):
                return
        msg = f"CSV file does not contain header row.Confirm CSV file and header again. Header = {self.header}"
        raise InvalidHeaderError(msg)
