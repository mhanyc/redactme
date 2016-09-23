#!ve/bin/python3
"""
This script extracts the Named Entities from a text file (must be utf8 encoded)
and outputs a list of these entities, one per line.

extract_names.py [-h|--file] <utf8 encoded text file to process>

This script is based on https://gist.github.com/onyxfish/322906#gistcomment-1485426

Jonah Bossewitch, MHA of NYC
"""

import sys
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

    # Print unique entity names
    return (set(entity_names))


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="filename: a utf8 encoded text file")
    args = parser.parse_args()

    entity_list = list(parse_file(args.filename)) # returns a set, so cast to list
    entity_list.sort()                            # sort the list
    
    # print the names out to stdout, one per line. 
    # meant to be redirected into an output file.
    for entity in entity_list:
        print(entity)

if __name__ == "__main__":
    sys.exit(main())
