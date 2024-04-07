import logging.config
import uuid

import yaml

ID = uuid.UUID

# Load the config file
with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

# Example of getting a logger object
#logger = logging.getLogger('development')
#logger = logging.getLogger('staging')
#logger = logging.getLogger('production')

# Log some messages
#logger.debug('This is a debug message')
#logger.info('This is an info message')
#logger.warning('This is a warning message')
#logger.error('This is an error message')
#logger.critical('This is a critical message')