from enum import Enum


class EngineType(Enum):
    DIESEL = 1
    GASOLINE = 2
    LPG = 3


class TyreType(Enum):
    WINTER = 1
    SUMMER = 2


class CarBodyColor(Enum):
    BLACK = 1
    SILVER = 2
    WHITE = 3
    RED = 4
    BLUE = 5
    GREEN = 6


class CarBodyType(Enum):
    SEDAN = 1
    HATCHBACK = 2
    COMBI = 3
