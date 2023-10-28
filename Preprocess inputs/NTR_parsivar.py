from parsivar import Normalizer
from parsivar import Tokenizer

import io
from pathlib import Path
import os.path
import codecs

my_normalizer = Normalizer()
my_tokenizer = Tokenizer()

def remove_stop_words(tokenized_words):
    f = io.open("Stopwords/Stopwords.txt", mode="r", encoding="utf-8")
    stopwords = my_tokenizer.tokenize_words(my_normalizer.normalize(f.read()))
    for word in tokenized_words:
        if word in stopwords:
            tokenized_words.remove(word)
    return tokenized_words

basepath = Path('Poems/')
files_in_basepath = basepath.iterdir()

for item in files_in_basepath:
    # read raw file
    f = io.open(item, mode="r", encoding="utf-8")
    # normalize and tokenize file
    tokenized_words = my_tokenizer.tokenize_words(my_normalizer.normalize(f.read()))
    # remove stop words
    tokenized_words_after_removing = remove_stop_words(tokenized_words)
    # words to text
    text = "\n".join(tokenized_words_after_removing)
    # save preprocessed file
    save_path = 'C:/Users/Maryam/Desktop/Term1/IR/HW1_amali/dataset/poems/parsivar/NTR_parsivar/'
    completeName = os.path.join(save_path, item.name)
    file1 = codecs.open(completeName, "w", "utf-8")
    file1.write(text)
    file1.close()

    basepath = Path('Queries/')
    files_in_basepath = basepath.iterdir()

    for item in files_in_basepath:
        # read raw file
        f = io.open(item, mode="r", encoding="utf-8")
        # normalize and tokenize file
        tokenized_words = my_tokenizer.tokenize_words(my_normalizer.normalize(f.read()))
        # remove stop words
        tokenized_words_after_removing = remove_stop_words(tokenized_words)
        # words to text
        text = "\n".join(tokenized_words_after_removing)
        # save preprocessed file
        save_path = 'C:/Users/Maryam/Desktop/Term1/IR/HW1_amali/dataset/queries/parsivar/NTR_parsivar/'
        completeName = os.path.join(save_path, item.name)
        file2 = codecs.open(completeName, "w", "utf-8")
        file2.write(text)
        file2.close()
