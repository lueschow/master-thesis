class Paths:

    def __init__(self):
        pass

    def editionpath(self):
        editionpath = './/{http://www.dspin.de/data/metadata}MetaData/{http://www.dspin.de/data/metadata}source/{http://www.clarin.eu/cmd/1}CMD/{http://www.clarin.eu/cmd/1}Components/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}teiHeader/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}fileDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}sourceDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}biblFull/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}editionStmt/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}edition'
        return editionpath

    def placespath(self):
        placespath = './/{http://www.dspin.de/data/metadata}MetaData/{http://www.dspin.de/data/metadata}source/{http://www.clarin.eu/cmd/1}CMD/{http://www.clarin.eu/cmd/1}Components/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}teiHeader/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}fileDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}sourceDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}biblFull/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}publicationStmt/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}pubPlace'
        return placespath

    def datespath(self):
        datespath = './/{http://www.dspin.de/data/metadata}MetaData/{http://www.dspin.de/data/metadata}source/{http://www.clarin.eu/cmd/1}CMD/{http://www.clarin.eu/cmd/1}Components/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}teiHeader/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}fileDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}sourceDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}biblFull/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}publicationStmt/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}date'
        return datespath

    def typedescpath(self):
        typedescpath = './/{http://www.dspin.de/data/metadata}MetaData/{http://www.dspin.de/data/metadata}source/{http://www.clarin.eu/cmd/1}CMD/{http://www.clarin.eu/cmd/1}Components/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}teiHeader/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}fileDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}sourceDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}msDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}physDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}typeDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}p'
        return typedescpath

    def allgenrespath(self):
        allgenrespath = './/{http://www.dspin.de/data/metadata}MetaData/{http://www.dspin.de/data/metadata}source/{http://www.clarin.eu/cmd/1}CMD/{http://www.clarin.eu/cmd/1}Components/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}teiHeader/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}profileDesc/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}textClass/{http://www.clarin.eu/cmd/1/profiles/clarin.eu:cr1:p_1381926654438}classCode'
        return allgenrespath

    def tokenspath(self):
        tokenspath = './/{http://www.dspin.de/data/textcorpus}TextCorpus/{http://www.dspin.de/data/textcorpus}tokens/{http://www.dspin.de/data/textcorpus}token'
        return tokenspath

    def lemmaspath(self):
        lemmaspath = './/{http://www.dspin.de/data/textcorpus}TextCorpus/{http://www.dspin.de/data/textcorpus}lemmas/{http://www.dspin.de/data/textcorpus}lemma'
        return lemmaspath

    def tagspath(self):
        tagspath = './/{http://www.dspin.de/data/textcorpus}TextCorpus/{http://www.dspin.de/data/textcorpus}POStags/{http://www.dspin.de/data/textcorpus}tag'
        return tagspath

    def correctionspath(self):
        correctionspath = './/{http://www.dspin.de/data/textcorpus}TextCorpus/{http://www.dspin.de/data/textcorpus}orthography/{http://www.dspin.de/data/textcorpus}correction'
        return correctionspath
        
