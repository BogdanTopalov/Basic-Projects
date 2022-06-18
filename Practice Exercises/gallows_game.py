class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if self.words and not self.game_over:
            if not self.words[-1][-1] == word[0] or word in self.words:
                self.game_over = True
                return 'game over'

        self.words.append(word)
        return self.words

    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'
