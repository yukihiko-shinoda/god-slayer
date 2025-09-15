"""Factory for GodSlayer."""

from __future__ import annotations

from typing import TYPE_CHECKING

from godslayer.csv.god_slayer import GodSlayer
from godslayer.reader_operator_factory import ReaderOperatorFactory

if TYPE_CHECKING:
    from pathlib import Path

__all__ = ["GodSlayerFactory"]


class GodSlayerFactory:
    """Factory for GodSlayer."""

    def __init__(
        self,
        *,
        header: list[str] | None = None,
        partition: list[str] | None = None,
        footer: list[str] | None = None,
        encoding: str = "utf-8",
    ) -> None:
        self.header = header
        self.partition = partition
        self.footer = footer
        self.encoding = encoding

    def create(self, path_to_file: Path) -> GodSlayer:
        return GodSlayer(
            path_to_file,
            ReaderOperatorFactory(
                path_to_file,
                header=self.header,
                partition=self.partition,
                footer=self.footer,
                encoding=self.encoding,
            ),
            encoding=self.encoding,
        )
