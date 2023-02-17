from typing import Literal

SignType = Literal[-1, 0, 1]


def sign(number: int | float) -> SignType: ...
