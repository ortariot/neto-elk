import random
import datetime
import json
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def log_generator():
    while True:
        
        log = {
            'level': random.choice(('info', 'error', 'warning', 'debug')),
            'msg': random.choice(
                ('get_data', 'update_data', 'set_data')
                ),
            'asctime': datetime.datetime.now(datetime.timezone.utc).isoformat(
                timespec='milliseconds', sep=' '
            )
        }

        with open(os.path.join(BASE_DIR, 'log_gen.log'), 'a') as f:
            f.write(json.dumps(log) + '\n')

        time.sleep(1)


if __name__ == '__main__':
    log_generator()