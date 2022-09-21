import logging


def logger_config():
    logging.basicConfig(level=logging.ERROR,
                        format='%(asctime)s %(module)-12s %(levelname)-8s %(message)s',
                        filename='error.log',
                        filemode='a')

    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s %(module)-12s %(levelname)-8s %(message)s')
    console.setFormatter(formatter)

    logging.getLogger('').addHandler(console)
