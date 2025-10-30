"""ReaderOperator to read record."""

from __future__ import annotations

from typing import Generator
from typing import Iterator

from godslayer.csv.reader_operators.reader_operator import ReaderOperator


class RecordReader(ReaderOperator):
    """ReaderOperator to read record."""

    def process(self, reader_input: Iterator[list[str]]) -> Generator[list[str], None, None]:
        yield from super().process(reader_input)
        for index, list_input_row_standard_type_value in enumerate(reader_input):
            self._index = index
            yield list_input_row_standard_type_value
