from decimal import Decimal
from collections import defaultdict
from cars_manager.model.car import Car
from cars_manager.model.enums import CarBodyType, TyreType
from cars_manager.services.types import SortType, SortCarBodyType, SortEngineType, StatisticsType, Statistics


class CarsService:
    def __init__(self, cars: list[Car]) -> None:
        self.cars = cars

    def show_all_cars(self) -> list[Car]:
        """

        :return:
        """
        return [car for car in self.cars]

    """
    Metoda zwraca kolekcję samochodów posortowaną według kryterium
    podanego jako argument. Metoda powinna umożliwiać sortowanie
    według ilości komponentów, mocy silnika oraz rozmiaru opony.
    Dodatkowo metoda powinna umożliwiać sortowanie rosnąco oraz
    malejąco.
    """

    def sort_by_comp_or_power_or_wheel_size(self, type: SortType = SortType.POWER, reverse: bool = False) \
            -> list[Car]:
        """

        :param type:
        :param reverse:
        :return:
        """
        match type:
            case SortType.COMPONENTS:
                return sorted(self.cars, key=lambda car: len(car.car_body.components), reverse=reverse)
            case SortType.POWER:
                return sorted(self.cars, key=lambda car: car.engine.power, reverse=reverse)
            case SortType.WHEEL_SIZE:
                return sorted(self.cars, key=lambda car: car.wheel.size, reverse=reverse)
            case _:
                raise ValueError('Sort type is not correct')

    """
    Metoda zwraca kolekcję samochodów o określonym rodzaju nadwozia
    przekazanym jako argument (CarBodyType) oraz o cenie z przedziału 
    <a, b>, gdzie a oraz b to kolejne argumenty metody.
    """

    def sort_cars_by_car_body_type_and_between_price(self, type: SortCarBodyType = SortCarBodyType.HATCHBACK,
                                                     min_price: Decimal = 100, max_price: Decimal = 200) -> list[Car]:
        if min_price > max_price:
            raise ValueError('The price range is not correct')

        match type:
            case SortCarBodyType.HATCHBACK:
                return [car for car in self.cars if car.has_car_body_type(CarBodyType.HATCHBACK.name)
                        and car.has_price_in_range(min_price, max_price)]
            case SortCarBodyType.SEDAN:
                return [car for car in self.cars if car.has_car_body_type(CarBodyType.SEDAN.name)
                        and car.has_price_in_range(min_price, max_price)]
            case SortCarBodyType.COMBI:
                return [car for car in self.cars if car.has_car_body_type(CarBodyType.COMBI.name)
                        and car.has_price_in_range(min_price, max_price)]

    """
    Metoda zwraca posortowaną alfabetycznie kolekcję modeli samochodów, 
    które posiadają typ silnika (EngineType) przekazany jako argument metody.
    """

    def sort_by_engine_type(self, type: SortEngineType = SortEngineType.GASOLINE, reverse: bool = False) \
            -> list[Car]:
        match type:
            case SortEngineType.GASOLINE:
                return sorted([car for car in self.cars if car.has_engine_type(SortEngineType.GASOLINE.name)],
                              key=lambda car: car.model, reverse=reverse)
            case SortEngineType.LPG:
                return sorted([car for car in self.cars if car.has_engine_type(SortEngineType.LPG.name)],
                              key=lambda car: car.model, reverse=reverse)
            case SortEngineType.DIESEL:
                return sorted([car for car in self.cars if car.has_engine_type(SortEngineType.DIESEL.name)],
                              key=lambda car: car.model, reverse=reverse)
            case _:
                raise ValueError('Sort engine type is not correct')

    def get_statistics(self, statistic_type: StatisticsType) -> Statistics:
        def get_price_statistics() -> Statistics:
            prices = [car.price for car in self.cars]
            return Statistics(
                min(prices),
                sum(prices) / len(prices),
                max(prices),
            )

        def get_mileage_statistics() -> Statistics:
            mileages = [car.mileage for car in self.cars]
            return Statistics(
                min(mileages),
                sum(mileages) / len(mileages),
                max(mileages),
            )

        def get_power_engine_statistics() -> Statistics:
            engine_power = [car.engine.power for car in self.cars]
            return Statistics(
                min(engine_power),
                sum(engine_power) / len(engine_power),
                max(engine_power)
            )

        match statistic_type:
            case StatisticsType.PRICE:
                return get_price_statistics()
            case StatisticsType.MILEAGE:
                return get_mileage_statistics()
            case StatisticsType.POWER:
                return get_power_engine_statistics()
            case _:
                raise ValueError('Incorrect statistics type')

    """
    Metoda zwraca mapę, w której kluczem jest obiekt klasy Car,
    natomiast wartością jest liczba kilometrów, które samochód
    przejechał. Pary w  mapie posortowane są malejąco według 
    wartości.
    """

    def get_cars_with_mileage(self, reverse: bool = True) -> dict[Car, int]:
        grouped_by_mileage = defaultdict(list)
        for car in self.cars:
            grouped_by_mileage[car].append(car.mileage)
        return dict(sorted([(car, car_mileage[0]) for car, car_mileage in grouped_by_mileage.items()],
                           key=lambda item: item[1], reverse=reverse))

    """
    Metoda zwraca mapę, w której kluczem jest rodzaj opony (TyreType), 
    a wartością lista samochodów o takim typie opony. Mapa posortowana 
    jest malejąco po ilości elementów w kolekcji.
    """

    def group_cars_by_tyre_type(self, reverse: bool = True) -> dict[TyreType, int]:
        count_tyre_type = defaultdict(list)
        for car in self.cars:
            count_tyre_type[car.wheel.type].append(car)
        return dict(sorted(count_tyre_type.items(), key=lambda item: len(item[1]), reverse=reverse))

    """
    Metoda zwraca kolekcję samochodów, które posiadają wszystkie komponenty
    z kolekcji przekazanej jako argument. Kolekcja posortowana jest 
    alfabetycznie według nazwy modelu samochodu.
    """

    def get_cars_containing_all_components(self, components: list[str], reverse: bool = False) -> list[Car]:
        return sorted([car for car in self.cars if car.has_all_components(components)], key=lambda c: c.model,
                      reverse=reverse)
