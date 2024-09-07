class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, words):
        return [word for word in words if sorted(word) == self.sorted_word and word != self.word]