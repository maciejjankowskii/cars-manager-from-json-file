from dataclasses import dataclass, field
from decimal import Decimal
from .enums import EngineType, TyreType, CarBodyColor, CarBodyType


@dataclass(frozen=True,  eq=True)
class Engine:
    type: EngineType
    power: float


@dataclass(frozen=True,  eq=True)
class Wheel:
    type: TyreType
    model: str
    size: int


@dataclass(frozen=True,  eq=True)
class CarBody:
    color: CarBodyColor
    type: CarBodyType
    components: list[str] = field(compare=False)


@dataclass(frozen=True,  eq=True)
class Car:
    model: str
    price: Decimal
    mileage: int
    engine: Engine
    car_body: CarBody
    wheel: Wheel

    def has_car_body_type(self, car_body_type: str) -> bool:
        return self.car_body.type == car_body_type

    def has_price_in_range(self, min_price: Decimal, max_price: Decimal):
        return min_price <= self.price <= max_price

    def has_engine_type(self, engine_type: str) -> bool:
        return self.engine.type == engine_type

    def has_all_components(self, components: list[str]) -> bool:
        return all(c in self.car_body.components for c in components)
