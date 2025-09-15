"""Test for header_skipper.py."""

from __future__ import annotations

import csv
from typing import TYPE_CHECKING

import pytest

from godslayer.csv.reader_operators.header_skipper import HeaderSkipper
from godslayer.exceptions import InvalidHeaderError
from tests.testlibraries.instance_resource import InstanceResource

if TYPE_CHECKING:
    from pathlib import Path


class TestHeaderSkipper:
    """Test for HeaderSkipper."""

    @staticmethod
    def test(path_gold_point_card_plus: Path) -> None:
        with path_gold_point_card_plus.open("r", encoding="shift_jis_2004") as file_input:
            header_skipper = HeaderSkipper(InstanceResource.REGEX_HEADER_GOLD_POINT_CARD_PLUS)
            with pytest.raises(InvalidHeaderError):
                for _list_column in header_skipper.process(csv.reader(file_input)):
                    pass
