from __future__ import unicode_literals
from hazm import *

import io
from pathlib import Path
import os.path
import codecs

my_normalizer = Normalizer()

basepath = Path('Poems/')
files_in_basepath = basepath.iterdir()


for item in files_in_basepath:
    # read raw file
    f = io.open(item, mode="r", encoding="utf-8")
    # normalize file
    normalized_text = my_normalizer.normalize(f.read())
    # tokenize file
    tokenized_words = word_tokenize(normalized_text)
    # words to text
    text="\n".join(tokenized_words)
    # save preprocessed file
    save_path = 'C:/Users/Maryam/Desktop/Term1/IR/HW1_amali/dataset/poems/hazm/NT_hazm/'
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
    # words to text
    text="\n".join(tokenized_words)
    # save preprocessed file
    save_path = 'C:/Users/Maryam/Desktop/Term1/IR/HW1_amali/dataset/queries/hazm/NT_hazm/'
    completeName = os.path.join(save_path, item.name)
    file2 = codecs.open(completeName, "w", "utf-8")
    file2.write(text)
    file2.close()