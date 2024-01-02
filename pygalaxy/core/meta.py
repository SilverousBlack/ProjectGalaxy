import typing
from dataclasses import dataclass

@dataclass
class MinLen:
    value: int

@dataclass
class MaxLen:
    value: int

@dataclass
class IntRanged:
    min: int
    max: int

@dataclass
class FloatRanged:
    min: float
    max: float
    