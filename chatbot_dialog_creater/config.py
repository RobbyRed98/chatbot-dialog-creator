import os
import yaml

from chatbot_dialog_creater.counter import Counter

CURRENT_FILE: str = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CONFIG_FILE = f'{CURRENT_FILE}/resources/counter.yaml'

LAST_USER_ID = 0
LAST_LINE_ID = 0
LAST_MOVIE_ID = 0

if os.path.isfile(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as _config:
        _data: dict = yaml.safe_load(_config)
        LAST_USER_ID = _data['user']
        LAST_LINE_ID = _data['line']
        LAST_MOVIE_ID = _data['movie']
else:
    print("Error: No config file found!")
    exit(1)

USER_COUNTER = Counter('user', LAST_USER_ID)
LINE_COUNTER = Counter('line', LAST_LINE_ID)
MOVIE_COUNTER = Counter('movie', LAST_MOVIE_ID)


def update(movie_counter: Counter, user_counter: Counter, line_counter: Counter) -> None:
    with open(CONFIG_FILE, "w") as config:
        data: dict = {'user': user_counter.get(), 'line': line_counter.get(), 'movie': movie_counter.get()}
        yaml.safe_dump(data, config)
