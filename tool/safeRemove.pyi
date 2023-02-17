from typing import TypeVar

_T = TypeVar("_T")


def safe_remove(list_: list[_T], value:_T) -> list[_T]: ...
