"""Tests for last_line_detector.py."""
import pytest

from godslayer.exceptions import InvalidFooterError
from godslayer.last_line_detector import LastLineDetector
from tests.testlibraries.instance_resource import InstanceResource


class TestLastLineDetector:
    """Tests for LastLineDetector."""

    @staticmethod
    def test(path_gold_point_card_plus_201912):
        assert (
            LastLineDetector.detect_index(
                path_gold_point_card_plus_201912, InstanceResource.REGEX_FOOTER_GOLD_POINT_CARD_PLUS, "shift_jis_2004"
            )
            == 3
        )

    @staticmethod
    def test_error(path_gold_point_card_plus_201912):
        with pytest.raises(InvalidFooterError):
            LastLineDetector.detect_index(
                path_gold_point_card_plus_201912, ["", "", "", "", "", r"^\D*$", ""], "shift_jis_2004"
            )

    @staticmethod
    def test_newline_contains(path_itabashiku_population_newline_contains):
        assert (
            LastLineDetector.detect_index(
                path_itabashiku_population_newline_contains,
                InstanceResource.FOOTER_ITABASHIKU_POPULATION,
                "shift_jis_2004",
            )
            == 126
        )
