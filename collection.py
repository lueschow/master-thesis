from text import Text
from lemma import Lemma
from spelling import Spelling
from wordform import Wordform
import json

class Collection:

    def __init__(self):
        self.lemmas = {}


    def addText(self, text):
        lemmaSet = set(self.lemmas.keys())
        for lemmakey, lemma in text.lemmas.items():
            if lemmakey not in lemmaSet:
                self.lemmas[lemma.lemma] = lemma
                lemmaSet.add(lemmakey)
            else:
                for wordformkey, wordform in lemma.wordforms.items():
                    if wordformkey not in self.lemmas[lemma.lemma].wordforms:
                        self.lemmas[lemma.lemma].wordforms[wordform.wordform] = wordform
                    else:
                        for spellingkey, spelling in wordform.spellings.items():
                            if spellingkey not in self.lemmas[lemma.lemma].wordforms[wordform.wordform].spellings:
                                self.lemmas[lemma.lemma].wordforms[wordform.wordform].spellings[spelling.spelling] = spelling
                            else:
                                self.lemmas[lemma.lemma].wordforms[wordform.wordform].spellings[spelling.spelling].count += spelling.count
                    self.lemmas[lemma.lemma].wordforms[wordform.wordform].calculate_spellings_count()
                    self.lemmas[lemma.lemma].wordforms[wordform.wordform].calculate_entropy()

    def toJson(self):
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys = True, indent=True) 


    def spellings_count_entropy(self):
        # counts all spellings of the collection without hapax legomena
        spellings_count = 0
        for lemma_obj in self.lemmas.values():
            for wordform_obj in lemma_obj.wordforms.values():
                if wordform_obj.spellings_count != 1: # sorts out hapax legomena
                    spellings_count += wordform_obj.spellings_count
        return spellings_count


    def spellings_count(self):
        # counts all spellings of the collection including hapax legomena
        spellings_count = 0
        for lemma_obj in self.lemmas.values():
            for wordform_obj in lemma_obj.wordforms.values():
                spellings_count += wordform_obj.spellings_count
        return spellings_count


    def entropy(self):
        # calculates the entropy of the collection
        # weighted mean based on wordform entropies
        wordforms_spellings = 0.0
        full_entropies = 0.0
        for lemma in self.lemmas.values():
            for wordform in lemma.wordforms.values():
                if wordform.spellings_count != 1: # sorts out hapax legomena
                    full_entropies += wordform.entropy * wordform.spellings_count
                    wordforms_spellings += wordform.spellings_count
        if wordforms_spellings != 0: 
            return full_entropies / wordforms_spellings
        else:
            return 0