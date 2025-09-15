"""ReaderOperator to read record before footer."""

from __future__ import annotations

from typing import Generator
from typing import Iterator

from godslayer.csv.reader_operators.reader_operator import ReaderOperator


class RecordBeforeFooterReader(ReaderOperator):
    """ReaderOperator to read record before footer."""

    def __init__(self, index_footer_line: int, *, before_task: ReaderOperator | None = None) -> None:
        super().__init__(before_task=before_task)
        self.index_footer_line = index_footer_line

    def process(self, reader_input: Iterator[list[str]]) -> Generator[list[str], None, None]:
        yield from super().process(reader_input)
        for self._index, list_input_row_standard_type_value in enumerate(reader_input):
            if self.index >= self.index_footer_line:
                break
            yield list_input_row_standard_type_value
