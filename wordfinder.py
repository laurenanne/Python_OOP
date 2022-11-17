"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    ...

    def __init__(self, filename):
        self.filename = filename
        self.lst = []
        self.read_file()

    def read_file(self):
        f = open(self.filename, "r")
        for line in f:
            line = line.strip()
            self.lst.append(line)

        return self.lst

    def random(self):
        return (random.choice(self.lst))


class SpecialWordFinder(WordFinder):

    def create_clean_lst(self):
        self.lst = [item for item in self.lst if item != ""]
        self.lst = [
            item for item in self.lst if not item.startswith('#')]
        return self.lst
