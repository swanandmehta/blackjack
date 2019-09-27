# This is a configuration service
from config import configuration
from core import logger_services
config = None


def init():
    """  Help in initializing config service and configuration object """
    logger_services.log("Configuration service Init : Started")

    global config
    config = configuration.Configuration(no_of_users=1, min_amount=50, max_amount=100)

    logger_services.log("Configuration service Init : Completed")


def get_configuration():
    """  This allows us to get configuration  """
    global config
    return config
