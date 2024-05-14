import json
import logging
import os
from datetime import datetime
import time


SUCCESS_LEVEL_NUM = 25
logging.addLevelName(SUCCESS_LEVEL_NUM, "SUCCESS")

def success(self, message, *args, **kws):
    if self.isEnabledFor(SUCCESS_LEVEL_NUM):
        self._log(SUCCESS_LEVEL_NUM, message, args, **kws)

logging.Logger.success = success

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger

def log_message(logger, level, log_string, timestamp):
    log_entry = {
        "level": level,
        "log_string": log_string,
        "timestamp": timestamp,
        "metadata": {
            "source": logger.handlers[0].baseFilename
        }
    }
    if level == 'success':
        logger.success(json.dumps(log_entry))
    else:
        logger.log(getattr(logging, level.upper()), json.dumps(log_entry))

def main():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    
    loggers = {}
    for api in config['apis']:
        loggers[api['name']] = setup_logger(api['name'], api['log_file'], getattr(logging, api['log_level'].upper()))

    for i in range(5):  # Adjust the range for more logs
        log_message(loggers['API1'], 'info', f'API1 processed request {i}', datetime.utcnow().isoformat() + 'Z')
        log_message(loggers['API2'], 'error', f'API2 encountered an error {i}', datetime.utcnow().isoformat() + 'Z')
        log_message(loggers['API3'], 'success', f'API3 completed successfully {i}', datetime.utcnow().isoformat() + 'Z')
        time.sleep(1)

if __name__ == "__main__":
    if not os.path.exists('logs'):
        os.makedirs('logs')
    main()



    

