import xml.etree.cElementTree as ET
from paths import Paths
from lemma import Lemma
from spelling import Spelling
from wordform import Wordform
import json
import re

regexletter = re.compile('[a-zA-Z]+')
regexcode = re.compile('(&#x[a-zA-Z0-9]+;)')

class Text:

    def __init__(self, filename, date_pub = 'unspecified', date_cre = 'unspecified', genre = 'unspecified', places = [], typedesc = 'unspecified', edition = 'unspecified'):
        self.filename = filename
        self.date_pub = date_pub
        self.date_cre = date_cre
        self.genre = genre
        self.places = places
        self.typedesc = typedesc
        self.edition = edition
        self.lemmas = {}


    def read(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()

        paths = Paths()

        # save the edition
        self.edition = root.findall(paths.editionpath())[0].attrib['n']
        # save the place(s) in a list
        self.places = [ place.text for place in root.findall(paths.placespath()) ]

        # read the date(s)
        dates = root.findall(paths.datespath())
        if len(root.findall(paths.typedescpath())) > 0:
            self.typedesc = root.findall(paths.typedescpath())[0].text
        
        # read the genre (and save the DWDS1main classification)
        allgenres = root.findall(paths.allgenrespath())
        for genres in allgenres:
                if genres.attrib['scheme'] == 'http://www.deutschestextarchiv.de/doku/klassifikation#dwds1main':
                    self.genre = genres.text

        tokenList = root.findall(paths.tokenspath())
        lemmaList = root.findall(paths.lemmaspath())
        tagList = root.findall(paths.tagspath())
        correctionList = root.findall(paths.correctionspath())


        for date in dates:
            if date.attrib['type'] == 'publication':
                self.date_pub = date.text
            elif date.attrib['type'] == 'creation':
                self.date_cre = date.text

        # save the tokens with their IDs in a dictionary
        tokenListDict = {}
        for tokenElement in tokenList:
            tokenListDict[tokenElement.attrib['ID']] = tokenElement.text

        # detect tokens tagged as foreign material, punctuation or non-words
        # also detect tokens only consisting of characters that aren't a-z
        filtered_IDs = [] 
        for tag in tagList:
            if tag.text.startswith('FM') == True or tag.text.startswith('$') == True or tag.text == 'XY' or regexletter.search(regexcode.sub('', tokenListDict[tag.attrib['tokenIDs']])) is None:
                filtered_IDs.append(tag.attrib['tokenIDs'])
        filtered_IDs = set(filtered_IDs)

        # save the corrections (if there are any) with their IDs in a dictionary
        corrections_dict = {}
        correction_IDs = [] # needed for wordform generation
        for correction in correctionList:
            correction_IDs.append(correction.attrib['tokenIDs'])
            if correction.attrib['tokenIDs'] not in filtered_IDs:
                if correction.text is not None:
                    corrections_dict[correction.attrib['tokenIDs']] = correction.text.lower()
                else:
                    corrections_dict[correction.attrib['tokenIDs']] = None
        correction_IDs = set(correction_IDs)

        # save the lemmas with their IDs in a dictionary
        lemmas_dict = {}
        for lemma in lemmaList:
            if lemma.attrib['tokenIDs'] not in filtered_IDs:
                lemmas_dict[lemma.attrib['tokenIDs']] = lemma.text

        # generate the spellings from the tokens
        # generate the wordforms from the corrections if available, otherwise from the tokens
        spellings_dict = {}
        wordforms_dict = {}
        for token in tokenList:
            if token.attrib['ID'] not in filtered_IDs: # ignore filtered tokens
                if token.attrib['ID'] in correction_IDs:
                    wordforms_dict[token.attrib['ID']] = corrections_dict[token.attrib['ID']]
                else:
                    wordforms_dict[token.attrib['ID']] = token.text.lower()
                spellings_dict[token.attrib['ID']] = token.text.lower()

        # merge lemmas with their wordforms and wordforms with their spellings via token/spelling ID
        # generate Lemma, Wordform and Spelling objects
        for spelling_id, spelling_text in spellings_dict.items():
            wordform_text = wordforms_dict[spelling_id]
            lemma_text = lemmas_dict[spelling_id]
            if lemma_text not in self.lemmas:
                self.lemmas[lemma_text] = Lemma(lemma_text)
            if wordform_text not in self.lemmas[lemma_text].wordforms:
                self.lemmas[lemma_text].wordforms[wordform_text] = Wordform(wordform_text)
            if spelling_text not in self.lemmas[lemma_text].wordforms[wordform_text].spellings:
                self.lemmas[lemma_text].wordforms[wordform_text].spellings[spelling_text] = Spelling(spelling_text)
            self.lemmas[lemma_text].wordforms[wordform_text].spellings[spelling_text].count += 1


    def toJson(self):
        return json.dumps(self, default=lambda x: x.__dict__, indent=True)            

    @classmethod
    def fromJson(cls, filetext):
        dictionary = json.loads(filetext)
        text = Text(dictionary['filename'])
        text.places = dictionary['places']
        text.genre = dictionary['genre']
        text.date_pub = dictionary['date_pub']
        text.date_cre = dictionary['date_cre']
        text.typedesc = dictionary['typedesc']
        text.edition = dictionary['edition']

        for lemma_dict in dictionary['lemmas'].values():
            lemma_obj = Lemma(lemma_dict['lemma'])
            for wordform_dict in lemma_dict['wordforms'].values():
                wordform_obj = Wordform(wordform_dict['wordform'])
                for spelling_dict in wordform_dict['spellings'].values():
                    spelling_obj = Spelling(spelling_dict['spelling'])
                    spelling_obj.count = spelling_dict['count']
                    wordform_obj.spellings[spelling_obj.spelling] = spelling_obj
                wordform_obj.calculate_spellings_count()
                wordform_obj.calculate_entropy()
                lemma_obj.wordforms[wordform_obj.wordform] = wordform_obj
            text.lemmas[lemma_obj.lemma] = lemma_obj
        return text

    @classmethod
    def fromJsonCollection(cls, filetext):
        dictionary = json.loads(filetext)
        text = Text('collection')

        for lemma_dict in dictionary['lemmas'].values():
            lemma_obj = Lemma(lemma_dict['lemma'])
            for wordform_dict in lemma_dict['wordforms'].values():
                wordform_obj = Wordform(wordform_dict['wordform'])
                for spelling_dict in wordform_dict['spellings'].values():
                    spelling_obj = Spelling(spelling_dict['spelling'])
                    spelling_obj.count = spelling_dict['count']
                    wordform_obj.spellings[spelling_obj.spelling] = spelling_obj
                wordform_obj.calculate_spellings_count()
                wordform_obj.calculate_entropy()
                lemma_obj.wordforms[wordform_obj.wordform] = wordform_obj
            text.lemmas[lemma_obj.lemma] = lemma_obj
        return text
    

    def spellings_count_entropy(self):
        # counts all spellings of a text without hapax legomena
        spellings_count = 0
        for lemma_obj in self.lemmas.values():
            for wordform_obj in lemma_obj.wordforms.values():
                if wordform_obj.spellings_count != 1: # sorts out hapax legomena
                    spellings_count += wordform_obj.spellings_count
        return spellings_count


    def spellings_count(self):
        # counts all spellings of a text including hapax legomena
        spellings_count = 0
        for lemma_obj in self.lemmas.values():
            for wordform_obj in lemma_obj.wordforms.values():
                spellings_count += wordform_obj.spellings_count
        return spellings_count


    
    def entropy(self):
        # calculates the weighted mean based on wordform-entropies
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