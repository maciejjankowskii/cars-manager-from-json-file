import os
import json
import jsonschema
from jsonschema import validate
import logging
from decimal import Decimal
from cars_manager.model.car import Car, Engine, CarBody, Wheel
from cars_manager.validator.validator import validate_car, validate_engine, validate_wheel, validate_car_body

logger = logging.getLogger(__name__)


def validate_json(car: Car) -> bool:
    cars_schema = {
        "type": "object",
        "properties": {
            "model": {"type": "string"},
            "price": {"type": "number", "multipleOf": 0.01},
            "mileage": {"type": "integer"},
            "engine": {"type": "object",
                       "properties": {
                           "type": {"enum": ["DIESEL", "GASOLINE", "LPG"]},
                           "power": {"type": "integer"}},
                       "required": ["type", "power"],
                       },
            "car_body": {"type": "object",
                         "properties": {
                             "color": {"enum": ["BLACK", "SILVER", "WHITE", "RED", "BLUE", "GREEN"]},
                             "type": {"enum": ["SEDAN", "HATCHBACK", "COMBI"]},
                             "components": {"type": "array", "items": {"type": "string"}},
                         },
                         "required": ["color", "type", "components"],
                         },
            "wheel": {"type": "object",
                      "properties": {
                          "type": {"enum": ["SUMMER", "WINTER"]},
                          "model": {"type": "string"},
                          "size": {"type": "integer"}
                      },
                      "required": ["type", "model", "size"],
                      }
        }}

    try:
        if validate(instance=car, schema=cars_schema) is None:
            return True

    except jsonschema.exceptions.ValidationError as error:
        logger.error(f'{error.args[0]}. Wrong json file format')


def get_cars(filename: str) -> list[Car]:
    """
    The function returns a list of cars from the file specified as an argument
    :param filename:
    :return: list of Car class objects
    """

    if os.stat(filename).st_size == 0:
        raise ValueError('Json file is empty')

    with open(filename, 'r') as json_file:
        data = json.load(json_file)

    cars = [Car(car['model'],
                Decimal(car['price']),
                int(car['mileage']),
                Engine(car['engine']['type'], int(car['engine']['power'])),
                CarBody(car['car_body']['color'], car['car_body']['type'], car['car_body']['components']),
                Wheel(car['wheel']['type'], car['wheel']['model'], int(car['wheel']['size']))) for car in data
            if validate_json(car)]

    return [car for car in cars if validate_car(car)
            and validate_engine(car)
            and validate_wheel(car)
            and validate_car_body(car)]
