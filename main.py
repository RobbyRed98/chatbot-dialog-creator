from chatbot_dialog_creater.config import MOVIE_COUNTER
from chatbot_dialog_creater.config import USER_COUNTER
from chatbot_dialog_creater.config import LINE_COUNTER
from chatbot_dialog_creater.config import update as update_config
from chatbot_dialog_creater.generator import DialogGenerator

if __name__ == '__main__':
    generator: DialogGenerator = DialogGenerator(MOVIE_COUNTER, USER_COUNTER, LINE_COUNTER)
    while True:
        print("")
        generator.create_dialog()
        update_config(generator.movie_counter, generator.user_counter, generator.line_counter)

