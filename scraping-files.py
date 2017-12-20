#tagging and categorizing nouns and context using training data and using it on a text file only
#Calling relevant libraries
from nltk.tokenize import PunktSentenceTokenizer
import nltk
nltk.download('punkt')
import io

#saving the file by reading the text
with io.open("toread.txt", encoding="latin-1") as my_file:
    mytext = my_file.read()

#training data
with io.open("totrain.txt", encoding="latin-1") as m_file:
    ttext = m_file.read()

#tokenizing training text
custom_tokenizer = PunktSentenceTokenizer(ttext)

#tokenizing
token = custom_tokenizer.tokenize(mytext)

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

