from math import log

class Wordform:

    def __init__(self, wordform, spellings_count = 0, entropy = 0):
        self.wordform = wordform
        self.spellings = {}
        self.spellings_count = spellings_count
        self.entropy = entropy


    
    def calculate_spellings_count(self):
        # counts all spellings of one wordform
        self.spellings_count = 0
        for spelling_obj in self.spellings.itervalues():
            self.spellings_count += spelling_obj.count       


    
    def calculate_entropy(self):
        self.entropy = 0
        for spelling in self.spellings.itervalues():
            percentage = float(spelling.count) / float(self.spellings_count)
            self.entropy = self.entropy - (log(percentage, 2) * percentage)