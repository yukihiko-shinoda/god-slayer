"""Top-level package for God Slayer."""

from __future__ import annotations

from godslayer.exceptions import *  # noqa: F403
from godslayer.god_slayer_factory import *  # noqa: F403
from godslayer.last_line_detector import *  # noqa: F403
from godslayer.line_counter import *  # noqa: F403
from godslayer.list_string_matcher import *  # noqa: F403
from godslayer.reader_operator_factory import *  # noqa: F403

__author__ = """Yukihiko Shinoda"""
__email__ = "yuk.hik.future@gmail.com"
__version__ = "1.1.1"

__all__: list[str] = []
# pylint: disable=undefined-variable
__all__ += exceptions.__all__  # type: ignore[name-defined] # noqa: F405
__all__ += god_slayer_factory.__all__  # type: ignore[name-defined] # noqa: F405
__all__ += last_line_detector.__all__  # type: ignore[name-defined] # noqa: F405
__all__ += line_counter.__all__  # type: ignore[name-defined] # noqa: F405
__all__ += list_string_matcher.__all__  # type: ignore[name-defined] # noqa: F405
__all__ += reader_operator_factory.__all__  # type: ignore[name-defined] # noqa: F405
