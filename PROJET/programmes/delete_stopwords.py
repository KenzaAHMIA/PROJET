# programme python pour éliminer les stopwords, permettant :
# une analyse efficace
# des nuages cohérents


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import csv

en_tokens = []
stop_words_en =stopwords.words('english')
stop_words_en += ['\n', 'lang', '<', '<text>', 'a']


# preparation et nettoyage fichier anglais
with open ('../itrameur/contextes-en.txt', 'r') as file_en:
    content_en = file_en.readlines()
    
    for line in content_en:
        new_line = line.split()
        en_tokens += new_line

    for w in en_tokens:
        if w in stop_words_en or w in string.punctuation:
            en_tokens.remove(w)
   
# write to an output  file
with open('../itrameur/clean_contextes_en.txt', 'w', ) as clean_en: 
    for word in en_tokens:
        clean_en.write(f"{word} ")

################################################
# preparation et nettoyage fichier français 
fr_tokens = []
stop_words_fr =stopwords.words('french')
stop_words_fr += ['\n', 'lang', '<', '>', '<text>', '</text>', '</page>', 'lt', 'gt', 'en', 'En', \
    'le' , 'la', 'fr', 'Fr', 'Le', 'La', 'de', 'De', 'Un', 'Il' ]

with open ('../itrameur/clean_contextes_fr.txt', encoding="utf8", errors="ignore") as file_fr:
    content_fr = file_fr.readlines()

    for line in content_fr:
        new_line = line.split()
        fr_tokens += new_line

    for w in fr_tokens:
        if w in stop_words_fr or w in string.punctuation:
            fr_tokens.remove(w)

# write to a clean file
with open('../itrameur/clean_contextes-fr.txt', 'w', ) as clean_fr: 
    for word in fr_tokens:
        clean_fr.write(f"{word} ")
   

