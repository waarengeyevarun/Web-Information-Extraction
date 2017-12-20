#Categorizing Nouns through pos and tokenizing without semi supervised learning
import nltk
nltk.download('punkt')

#opening and reading the text file
import io
with io.open("toread.txt", encoding="latin-1") as my_file:
    mytext = my_file.read()

nouns = [] #empty to array to hold all nouns

#finding the nouns from the text
for word,pos in nltk.pos_tag(nltk.word_tokenize(mytext)):
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
        nouns.append(word)

print(nouns)

#chunking the context and noun phrases
def process_content():
    try:
        for i in mytext:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # Using Regular expressions to carve out Nouns
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)

    except Exception as e:
        print(str(e))

process_content()