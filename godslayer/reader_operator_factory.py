"""Factory for ReaderOperator."""

from __future__ import annotations

from typing import TYPE_CHECKING

from godslayer.csv.reader_operators.header_skipper import HeaderSkipper
from godslayer.csv.reader_operators.partition_skip_record_before_footer_reader import (
    PartitionSkipRecordBeforeFooterReader,  # noqa: H301,RUF100
)
from godslayer.csv.reader_operators.partition_skip_record_reader import PartitionSkipRecordReader
from godslayer.csv.reader_operators.record_before_footer_reader import RecordBeforeFooterReader
from godslayer.csv.reader_operators.record_reader import RecordReader
from godslayer.last_line_detector import LastLineDetector

if TYPE_CHECKING:
    from pathlib import Path

    from godslayer.csv.reader_operators.reader_operator import ReaderOperator

__all__ = ["ReaderOperatorFactory"]


class ReaderOperatorFactory:
    """Factory for ReaderOperator."""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        path_to_file: Path,
        *,
        header: list[str] | None = None,
        partition: list[str] | None = None,
        footer: list[str] | None = None,
        # pylint: disable=duplicate-code
        encoding: str = "utf-8",
    ) -> None:
        self.path_to_file = path_to_file
        self.header = header
        self.partition = partition
        self.footer = footer
        self.encoding = encoding

    def create(self) -> ReaderOperator:
        """Creates ReaderOperator."""
        header_skipper: HeaderSkipper | None = None if self.header is None else HeaderSkipper(self.header)
        if self.footer is not None:
            index_last_line = LastLineDetector.detect_index(self.path_to_file, self.footer, self.encoding)
            reader_operator = self._create_record_before_footer_reader(index_last_line, header_skipper)
        else:
            reader_operator = self._create_no_footer_record_reader(header_skipper)
        return reader_operator

    def _create_no_footer_record_reader(self, header_skipper: HeaderSkipper | None) -> ReaderOperator:
        if self.partition is not None:
            return PartitionSkipRecordReader(self.partition, before_task=header_skipper)
        return RecordReader(before_task=header_skipper)

    def _create_record_before_footer_reader(
        self,
        index_last_line: int,
        header_skipper: HeaderSkipper | None,
    ) -> ReaderOperator:
        if self.partition is not None:
            return PartitionSkipRecordBeforeFooterReader(self.partition, index_last_line, before_task=header_skipper)
        return RecordBeforeFooterReader(index_last_line, before_task=header_skipper)
