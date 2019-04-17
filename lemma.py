class Lemma:

    def __init__(self, lemma):
        self.lemma = lemma
        self.wordforms = {}


    def spellings_count(self):
        # counts all spellings of one lemma including hapax legomena
        spellings_count = 0
        for wordform_obj in self.wordforms.itervalues():
            spellings_count += wordform_obj.spellings_count
        return spellings_count

    def spellings_count_entropy(self):
        # counts all spellings of one lemma without hapax legomena
        spellings_count = 0
        for wordform_obj in self.wordforms.itervalues():
            if wordform_obj.spellings_count != 1: # sorts out hapax legomena
                spellings_count += wordform_obj.spellings_count
        return spellings_count



    def entropy(self):
        # calculates the weighted mean
        wordforms_spellings = 0.0
        full_entropies = 0.0
        for wordform in self.wordforms.itervalues():
            full_entropies += wordform.entropy * float(wordform.spellings_count)
            wordforms_spellings += float(wordform.spellings_count)
        return full_entropies / wordforms_spellings