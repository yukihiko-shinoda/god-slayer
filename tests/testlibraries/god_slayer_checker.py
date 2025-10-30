"""Test library for check GodSlayer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING
from typing import Iterator

import pytest

if TYPE_CHECKING:
    from godslayer.csv.god_slayer import GodSlayer


@dataclass
class GodSlayerCheckState:
    iterator_actual: Iterator[list[str]]
    length_record: int = 0
    gap: bool = False
    last_index: int | None = None


class GodSlayerChecker:
    """Test library for check GodSlayer."""

    @staticmethod
    def assert_god_slayer(god_slayer: GodSlayer, expected_index_start: int, expected: list[list[str]]) -> None:
        """Checks GodSlayer."""
        god_slayer_check_state = GodSlayerCheckState(iter(god_slayer))
        # Order of argument for zip() is important.
        # First argument should be "expected"
        # to confirm that next iteration of actual raises StopIteration,
        # since zip() iterates first argument even if second argument is empty.
        for index, (expected_record, actual) in enumerate(zip(expected, god_slayer_check_state.iterator_actual)):
            assert god_slayer.index == expected_index_start + index
            assert actual == expected_record
            god_slayer_check_state.length_record += 1
        GodSlayerChecker.assert_length(expected, god_slayer_check_state)

    @staticmethod
    def assert_god_slayer_partition(god_slayer: GodSlayer, expected: list[list[str]]) -> None:
        god_slayer_check_state = GodSlayerCheckState(iter(god_slayer))
        GodSlayerChecker._assert_god_slayer_partition(expected, god_slayer, god_slayer_check_state)
        GodSlayerChecker.assert_length(expected, god_slayer_check_state)
        assert god_slayer_check_state.gap

    @staticmethod
    def _assert_god_slayer_partition(
        expected: list[list[str]],
        god_slayer: GodSlayer,
        god_slayer_check_state: GodSlayerCheckState,
    ) -> None:
        for expected_record, actual in zip(expected, god_slayer_check_state.iterator_actual):
            if (
                god_slayer_check_state.last_index is not None
                and god_slayer.index - god_slayer_check_state.last_index > 1
            ):
                god_slayer_check_state.gap = True
            god_slayer_check_state.last_index = god_slayer.index
            assert actual == expected_record
            god_slayer_check_state.length_record += 1

    @staticmethod
    def assert_length(expected: list[list[str]], god_slayer_check_state: GodSlayerCheckState) -> None:
        assert god_slayer_check_state.length_record == len(expected)
        with pytest.raises(StopIteration):
            next(god_slayer_check_state.iterator_actual)
