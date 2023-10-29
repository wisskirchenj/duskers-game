import os

import jsonpickle

SAVE_PATH = "high_scores.json"


class ScoreManager:

    def __init__(self):
        self.scores = self.load_scores()

    @staticmethod
    def load_scores() -> list[(str, int)]:
        if os.path.isfile(SAVE_PATH):
            with open(SAVE_PATH, 'r') as file:
                return jsonpickle.decode(file.read())
        else:
            return []

    def save_scores(self):
        with open(SAVE_PATH, 'w') as file:
            file.write(jsonpickle.encode(self.scores[:10]))

    def add_score(self, name: str, score: int):
        self.scores.append((name, score))
        self.scores.sort(key=lambda x: x[1], reverse=True)
        self.save_scores()

    def show_scores(self):
        print('\n	HIGH SCORES\n')
        if not self.scores:
            print('No scores to display.')
        for i, (name, score) in enumerate(self.scores):
            print(f'({i + 1}) {name} {score}')
