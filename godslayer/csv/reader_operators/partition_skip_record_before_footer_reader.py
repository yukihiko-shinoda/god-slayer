"""ReaderOperator to skip partition record until before footer."""
from typing import Generator, Iterator, List, Optional

from godslayer.csv.reader_operators.reader_operator import ReaderOperator
from godslayer.list_string_matcher import ListStringMatcher


class PartitionSkipRecordBeforeFooterReader(ReaderOperator):
    """ReaderOperator to skip partition record and read until before footer."""

    def __init__(self, partition: List[str], index_footer_line: int, *, before_task: Optional[ReaderOperator] = None):
        super().__init__(before_task=before_task)
        self.partition = partition
        self.index_footer_line = index_footer_line

    def process(self, reader_input: Iterator[List[str]]) -> Generator[List[str], None, None]:
        yield from super().process(reader_input)
        # pylint: disable=duplicate-code
        for self._index, list_input_row_standard_type_value in enumerate(reader_input):
            if self.index >= self.index_footer_line:
                break
            if ListStringMatcher.is_matched(self.partition, list_input_row_standard_type_value):
                continue
            yield list_input_row_standard_type_value
