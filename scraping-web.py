#tagging and categorizing nouns and context using training data and using it on a random webpage

#Calling relevant libraries
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import io
from nltk.tokenize import PunktSentenceTokenizer
nltk.download('punkt')

#getting a request
resp = requests.get('https://en.wikipedia.org/wiki/Gull')

#get the text document
html = resp.text

#converting to a beautiful soup object
so = BeautifulSoup(html, "html5lib")

#geting the text and cleaning it
text = so.get_text(strip=True)


#training data
with io.open("totrain.txt", encoding="latin-1") as m_file:
    ttext = m_file.read()

#tokenizing training text
custom_tokenizer = PunktSentenceTokenizer(ttext)

#removing the stopwords
tokens = [t for t in text.split()]
clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

print tokens

#tokenizing the text to be worked on
token = custom_tokenizer.tokenize(text)

#part of speech tagging script by creating a function that will run through and tag all of the parts of speech per sentence
def process_content():
    try:
        for i in token[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #Using Regular expressions to carve out Nouns
            chunkGram = r"""Categories: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            #only interested in getting just the chunks, ignoring the rest.
            print(chunked)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)

    except Exception as e:
        print(str(e))

process_content()

