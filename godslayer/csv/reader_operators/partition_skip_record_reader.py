"""ReaderOperator to skip partition record."""

from __future__ import annotations

from typing import Generator
from typing import Iterator

from godslayer.csv.reader_operators.reader_operator import ReaderOperator
from godslayer.list_string_matcher import ListStringMatcher


class PartitionSkipRecordReader(ReaderOperator):
    """ReaderOperator to skip partition record."""

    def __init__(self, partition: list[str], *, before_task: ReaderOperator | None = None) -> None:
        super().__init__(before_task=before_task)
        self.partition = partition

    def process(self, reader_input: Iterator[list[str]]) -> Generator[list[str], None, None]:
        yield from super().process(reader_input)
        for self._index, list_input_row_standard_type_value in enumerate(reader_input):
            if ListStringMatcher.is_matched(self.partition, list_input_row_standard_type_value):
                continue
            yield list_input_row_standard_type_value
