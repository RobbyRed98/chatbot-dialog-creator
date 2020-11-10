from chatbot_dialog_creater.counter import Counter


class DialogGenerator:

    def __init__(self, movie_counter: Counter, user_counter: Counter, line_counter: Counter):
        self.line_counter: Counter = line_counter
        self.user_counter: Counter = user_counter
        self.movie_counter: Counter = movie_counter
        self.questioner: str = input("Enter the questioner's name: ")
        if self.questioner in ["q", "quit"]:
            exit(0)

        self.respondent: str = input("Enter the respondent's name: ")
        if self.respondent in ["q", "quit"]:
            exit(0)

        self.questioner_id: int = user_counter.inc()
        self.respondent_id: int = user_counter.inc()
        self.movie_id: int = movie_counter.inc()

    def create_dialog(self) -> None:
        line_id_question = self.line_counter.inc()
        line_id_response = self.line_counter.inc()

        question = input("Question: ")
        if question in ['q', 'quit']:
            exit(0)

        response = input("Answer: ")
        if response in ['q', 'quit']:
            exit(0)

        with open("lines.txt", 'a') as lines:
            lines.write(
                f"L{line_id_response} +++$+++ u{self.respondent_id} +++$+++ m{self.movie_id} +++$+++ {self.respondent} +++$+++ {response}\n")
            lines.write(
                f"L{line_id_question} +++$+++ u{self.questioner_id} +++$+++ m{self.movie_id} +++$+++ {self.questioner} +++$+++ {question}\n")

        with open("dialogs.txt", 'a') as dialogs:
            dialogs.write(
                f"u{self.respondent_id} +++$+++ u{self.questioner_id} +++$+++ m{self.movie_id} +++$+++ ['L{line_id_question}', 'L{line_id_response}']\n")
