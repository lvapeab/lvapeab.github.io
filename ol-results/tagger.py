import spacy
from spacy.tokens import Doc
import sys


def tag(filename, outfilename, nlp):

    with open(filename, 'r') as f:
        lines = f.read().splitlines()


    doc = nlp.pipe(lines,
                   disable=['sentencizer'])
    with open(outfilename, 'w') as outf:
        for d in doc:
            pos = " ".join(t.pos_ for t in d)
            outf.write(pos + '\n')

class WhitespaceTokenizer(object):
    def __init__(self, vocab):
        self.vocab = vocab

    def __call__(self, text):
        words = text.split(' ')
        # All tokens 'own' a subsequent space character in this tokenizer
        spaces = [True] * len(words)
        return Doc(self.vocab, words=words, spaces=spaces)


if __name__ == '__main__':
    nlp = spacy.load('es_core_news_md')
    nlp.tokenizer = WhitespaceTokenizer(nlp.vocab)

    tag(sys.argv[1], sys.argv[2], nlp)