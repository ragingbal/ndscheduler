"""Settings to override default settings."""

import logging

#
# Override settings
#
DEBUG = True

HTTP_PORT = 8888
HTTP_ADDRESS = '0.0.0.0'


DATABASE_CLASS = 'ndscheduler.corescheduler.datastore.providers.postgres.DatastorePostgres'
DATABASE_CONFIG_DICT = {
     'user': 'username',
     'password': 'password',
     'hostname': '192.168.0.157',
     'port': 5432,
     'database': 'scheduler',
     'sslmode': 'disable'
 }


#
# Set logging level
#
logging.getLogger().setLevel(logging.DEBUG)

JOB_CLASS_PACKAGES = ['simple_scheduler.jobs']
