from __future__ import unicode_literals
from hazm import *

import io
from pathlib import Path
import os.path
import codecs

my_normalizer = Normalizer()

def remove_stop_words(tokenized_words):
    f = io.open("Stopwords/Stopwords.txt", mode="r", encoding="utf-8")
    normalized_text = my_normalizer.normalize(f.read())
    stopwords = word_tokenize(normalized_text)
    for word in tokenized_words:
        if word in stopwords:
            tokenized_words.remove(word)
    return tokenized_words


basepath = Path('Poems/')
files_in_basepath = basepath.iterdir()

for item in files_in_basepath:
    # read raw file
    f = io.open(item, mode="r", encoding="utf-8")
    # normalize file
    normalized_text = my_normalizer.normalize(f.read())
    # tokenize file
    tokenized_words = word_tokenize(normalized_text)
    # remove stop words
    tokenized_words_after_removing = remove_stop_words(tokenized_words)
    # lemmatize file
    lemmatized_words = []
    lemmatizer = Lemmatizer()
    for word in tokenized_words_after_removing:
        lemmatized_word = lemmatizer.lemmatize(word)
        if "#" in lemmatized_word:
            lemmatized_word = lemmatized_word.split("#")[0]
        lemmatized_words.append(lemmatized_word)
    # words to text
    text = "\n".join(lemmatized_words)
    # save preprocessed file
    save_path = 'C:/Users/Maryam/Desktop/Term1/IR/HW1_amali/dataset/poems/hazm/NTRL_hazm/'
    completeName = os.path.join(save_path, item.name)
    file1 = codecs.open(completeName, "w", "utf-8")
    file1.write(text)
    file1.close()


basepath = Path('Queries/')
files_in_basepath = basepath.iterdir()

for item in files_in_basepath:
    # read raw file
    f = io.open(item, mode="r", encoding="utf-8")
    # normalize file
    normalized_text = my_normalizer.normalize(f.read())
    # tokenize file
    tokenized_words = word_tokenize(normalized_text)
    # remove stop words
    tokenized_words_after_removing = remove_stop_words(tokenized_words)
    # lemmatize file
    lemmatized_words = []
    lemmatizer = Lemmatizer()
    for word in tokenized_words_after_removing:
        lemmatized_word = lemmatizer.lemmatize(word)
        if "#" in lemmatized_word:
            lemmatized_word = lemmatized_word.split("#")[0]
        lemmatized_words.append(lemmatized_word)
    # words to text
    text = "\n".join(lemmatized_words)
    # save preprocessed file
    save_path = 'C:/Users/Maryam/Desktop/Term1/IR/HW1_amali/dataset/queries/hazm/NTRL_hazm/'
    completeName = os.path.join(save_path, item.name)
    file2 = codecs.open(completeName, "w", "utf-8")
    file2.write(text)
    file2.close()