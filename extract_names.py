#!ve/bin/python3
"""
This script extracts the Named Entities from a text file (must be utf8 encoded)
and outputs a list of these entities, one per line.

extract_names.py [-h|--help] <utf8 encoded text file to process>

This script is based on https://gist.github.com/onyxfish/322906#gistcomment-1485426

Jonah Bossewitch, MHA of NYC
"""

import sys
import os
import nltk


def extract_entity_names(t):
    """extracts entity names from an nltk tree, in this case a sentence chunk"""

    entity_names = []
    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names


def parse_file(filename):
    """takes a text filename and returns a list of unique nltk extracted names"""

    with open(filename, 'r') as f:
        file = f.read()

    sentences = nltk.sent_tokenize(file)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

    entity_names = []
    for tree in chunked_sentences:
        entity_names.extend(extract_entity_names(tree))

    # return unique entity names
    return (set(entity_names))


def print_entity_list(file_name):
    # returns a set, so cast to list
    entity_list = list(parse_file(file_name))
    # sort the list
    entity_list.sort()

    # print the names out to stdout, one per line.
    # meant to be redirected into an output file.
    for entity in entity_list:
        print(entity)


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", help="UTF8 encoded text file or "
                                      "directory containing multiple")
    args = parser.parse_args()
    path = args.path

    try:
        # make sure path exists
        assert os.path.exists(path)

        if os.path.isdir(path):
            # if path is a folder, iterate and print
            for file in os.listdir(path):
                print('=====RESULTS: {0}====='.format(file))
                print_entity_list('{0}/{1}'.format(path, file))
        elif os.path.isfile(path):
            # if path is a file, just print
            print_entity_list(path)
    except:
        raise OSError('Error opening file or folder')


if __name__ == "__main__":
    sys.exit(main())
