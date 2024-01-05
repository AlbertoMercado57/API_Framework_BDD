import configparser


def getConfigs():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config
