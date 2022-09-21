from decimal import Decimal
from typing import Final
from pprint import pprint
from cars_manager.services.cars import CarsService
from cars_manager.services.types import SortType, SortCarBodyType, SortEngineType, StatisticsType
from cars_manager.data_loader.json import get_cars
from cars_manager.config.logger import logger_config


def main() -> None:
    logger_config()

    FILENAME: Final = 'cars_manager/resources/cars.json'
    cars_list = get_cars(FILENAME)
    cars = CarsService(cars_list)
    #pprint(cars.show_all_cars())
    #pprint(cars.sort_by_comp_or_power_or_wheel_size(SortType.COMPONENTS))
    #pprint(cars.sort_cars_by_car_body_type_and_between_price(SortCarBodyType.HATCHBACK, Decimal(150), Decimal(500)))
    #pprint(cars.sort_by_engine_type(SortEngineType.GASOLINE))
    #pprint(cars.get_statistics(StatisticsType.POWER))
    #pprint(cars.get_cars_with_mileage(), sort_dicts=False)
    #pprint(cars.group_cars_by_tyre_type())
    #pprint(cars.get_cars_containing_all_components(['ABS']))


if __name__ == '__main__':
    main()
