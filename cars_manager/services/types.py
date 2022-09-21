from enum import Enum
from dataclasses import dataclass
from decimal import Decimal


class SortType(Enum):
    COMPONENTS = 1
    POWER = 2
    WHEEL_SIZE = 3


class SortEngineType(Enum):
    DIESEL = 1
    GASOLINE = 2
    LPG = 3


class SortCarBodyType(Enum):
    HATCHBACK = 1
    SEDAN = 2
    COMBI = 3


class StatisticsType(Enum):
    PRICE = 1,
    MILEAGE = 2
    POWER = 3


@dataclass
class Statistics:
    min: float | Decimal
    avg: float | Decimal
    max: float | Decimal

