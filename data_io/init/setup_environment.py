import os
import yaml
import sqlalchemy
import logging

log = logging.getLogger(__name__)


def get_engine_from_profile(config_file):
    """
    Return sqlalchemy.create_engine(url) from config file.
    Input:
    config_file: File containing user, password, host, port, dbname,
    which are the credentials for the PostgreSQL database
    """

    with open(config_file, 'r') as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    if not ('user' in config.keys() and
            'password' in config.keys() and
            'host' in config.keys() and
            'port' in config.keys() and
            'dbname' in config.keys()):
        raise Exception('Bad config file: ' + config_file)

    url = 'postgresql://{user}:{password}@{host}:{port}/{dbname}'.format(user=config['user'],
                                                                        password=config['password'],
                                                                        host=config['host'],
                                                                        port=config['port'],
                                                                        dbname=config['dbname'])
    engine = sqlalchemy.create_engine(url)
    return engine


def get_engine(config_file = './init/default_profile.yaml'):
    try:
        engine = get_engine_from_profile(config_file)
        log.info('Connected to PostgreSQL database!')
    except IOError:
        log.exception('Failed to get database connection!')
        return None, 'fail'

    return engine
