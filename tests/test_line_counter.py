"""Tests for line_counter.py."""

from __future__ import annotations

from typing import TYPE_CHECKING

from godslayer.line_counter import LineCounter

if TYPE_CHECKING:
    from pathlib import Path


class TestLineCounter:
    """Tests for LineCounter."""

    EXPECTED_LINE_COUNT_GOLD_POINT_CARD = 5
    EXPECTED_LINE_COUNT_ITABASHIKU_POPULATION = 133

    @staticmethod
    def test_gold_point_card_plus_201912(path_gold_point_card_plus_201912: Path) -> None:
        actual = LineCounter.count(path_gold_point_card_plus_201912, "shift_jis_2004")
        assert actual == TestLineCounter.EXPECTED_LINE_COUNT_GOLD_POINT_CARD

    @staticmethod
    def test_itabashiku_population_newline_contains(path_itabashiku_population_newline_contains: Path) -> None:
        actual = LineCounter.count(path_itabashiku_population_newline_contains, "shift_jis_2004")
        assert actual == TestLineCounter.EXPECTED_LINE_COUNT_ITABASHIKU_POPULATION
