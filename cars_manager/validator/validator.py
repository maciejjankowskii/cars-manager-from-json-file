from cars_manager.model.car import Car
import re

import logging
logger = logging.getLogger(__name__)


def validate_car(car: Car) -> bool:
    if not re.match(r'^[A-Z][A-Z\s]*$', car.model):
        logger.error(f'Car model must consist of capital letters only: {car.model}')
        return False

    if car.price < 0:
        logger.error(f'Car price must be greater than 0: {car.price}')
        return False

    if car.mileage < 0:
        logger.error(f'Car mileage must be greater than 0: {car.mileage}')
        return False

    return True


def validate_engine(car: Car) -> bool:
    if car.engine.power < 0:
        logger.error(f'Engine power must be greater than 0: {car.engine.power}')
        return False

    return True


def validate_wheel(car: Car) -> bool:
    if not re.match(r'^[A-Z][A-Z\s]*$', car.wheel.model):
        logger.error(f'Wheel model must consist of capital letters only: {car.wheel.model}')
        return False

    if car.wheel.size < 0:
        logger.error(f'Wheel size must be greater than 0: {car.wheel.size}')
        return False

    return True


def validate_car_body(car: Car) -> bool:
    for comp in car.car_body.components:
        if not re.match(r'^[A-Z][A-Z\s]+$', comp):
            logger.error(f'Car body components must consist of capital letters only: {comp}')
            return False

    return True


