"""This module implements row pattern matcher."""

from __future__ import annotations

import re

__all__ = ["ListStringMatcher"]


class ListStringMatcher:
    """This class implements row pattern matcher."""

    @staticmethod
    def is_matched(list_pattern: list[str], list_column: list[str]) -> bool:
        """Returns whether all column is same or match with pattern or not."""
        if len(list_pattern) != len(list_column):
            return False
        return ListStringMatcher._is_matched(list_pattern, list_column)

    @staticmethod
    def _is_matched(list_pattern: list[str], list_column: list[str]) -> bool:
        for pattern, column in zip(list_pattern, list_column):
            compiled_pattern = re.compile(pattern, re.UNICODE)
            if pattern != column and not compiled_pattern.search(column):
                return False
        return True
