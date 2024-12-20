# steps to install spacy 
# addn. req - pip numpy setuptools wheel
# pip install -U pip setuptools wheel
# pip instal -U spacy
# python -m spacy download en_core_web_sm


from spacy import *
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarizer(rawdocs):
    stopwords=list(STOP_WORDS)
    nlp = load('en_core_web_sm') #spacy
    doc = nlp(rawdocs)
    wordtokens = [token.text for token in doc]
    wordfreq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in wordfreq.keys():
                wordfreq[word.text]=1
            else:
                wordfreq[word.text]+=1

    maxfreq = max(wordfreq.values())
    for word in wordfreq.keys():
        wordfreq[word] = wordfreq[word]/maxfreq
    
    sentencetokens = [sent for sent in doc.sents]
    sentencescore = {}
    for sent in sentencetokens:
        for word in sent:
            if word.text in wordfreq.keys():
                if sent not in sentencescore.keys():
                    sentencescore[sent] = wordfreq[word.text]
                else:
                    sentencescore[sent] += wordfreq[word.text]

    selectlength = int(len(sentencetokens)*0.4)
    summary = nlargest(selectlength,sentencescore,key=sentencescore.get)

    finalsummary = [word.text for word in summary]
    summary = ' '.join(finalsummary)

    return summary,doc,len(rawdocs.split()),len(summary.split())
