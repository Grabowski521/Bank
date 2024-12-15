import logging
import os

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def setup_logger(name, log_file, level=logging.INFO):

    logger = logging.getLogger(name)
    logger.setLevel(level)

    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

logger_masks = setup_logger('masks', os.path.join(log_dir, 'masks.log'))
logger_utils = setup_logger('utils', os.path.join(log_dir, 'utils.log'))