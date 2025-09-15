"""Tests for last_line_detector.py."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from godslayer.exceptions import InvalidFooterError
from godslayer.last_line_detector import LastLineDetector
from tests.testlibraries.instance_resource import InstanceResource

if TYPE_CHECKING:
    from pathlib import Path


class TestLastLineDetector:
    """Tests for LastLineDetector."""

    EXPECTED_LAST_LINE_INDEX_GOLD_POINT_CARD = 3
    EXPECTED_LAST_LINE_INDEX_ITABASHIKU_POPULATION = 126

    @staticmethod
    def test(path_gold_point_card_plus_201912: Path) -> None:
        assert (
            LastLineDetector.detect_index(
                path_gold_point_card_plus_201912,
                InstanceResource.REGEX_FOOTER_GOLD_POINT_CARD_PLUS,
                "shift_jis_2004",
            )
            == TestLastLineDetector.EXPECTED_LAST_LINE_INDEX_GOLD_POINT_CARD
        )

    @staticmethod
    def test_error(path_gold_point_card_plus_201912: Path) -> None:
        with pytest.raises(InvalidFooterError):
            LastLineDetector.detect_index(
                path_gold_point_card_plus_201912,
                ["", "", "", "", "", r"^\D*$", ""],
                "shift_jis_2004",
            )

    @staticmethod
    def test_newline_contains(path_itabashiku_population_newline_contains: Path) -> None:
        assert (
            LastLineDetector.detect_index(
                path_itabashiku_population_newline_contains,
                InstanceResource.FOOTER_ITABASHIKU_POPULATION,
                "shift_jis_2004",
            )
            == TestLastLineDetector.EXPECTED_LAST_LINE_INDEX_ITABASHIKU_POPULATION
        )
