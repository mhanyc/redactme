# redactme
A collection of scripts to streamline redaction processing.

This project is an attempt to streamline and improve the way we redact documents with sensitive data. 

## Overview
These process is built around pdf inputs, and is intended to be used alongside OpenText's [Redact-It Desktop](http://www.opentext.com/what-we-do/products/enterprise-content-management/content-centric-applications/opentext-redact-it/opentext-redact-it-desktop).

The basic strategy is to precompute a list of likely Named Entities using python's NLTK natural language processing libary.  This list is generated in a format that can be easily loaded into Redact-It when manually redacting (each file being redacted will have it's own custom list of precomputed stopwords). http://nlp.stanford.edu/software/CRF-NER.shtml

## Processing pipeline
Our documents begin as pdfs.
# Save the pdf as a text file using Adobe Acrobat (reader supports this)
# make sure the output is utf8, not windows 
# precompute Named Entities. 
# Optional: it may be a good idea to filter out this list of stopwords before loading it into the Redact-It software, elimianted obvious false postives - keep track of the name of this file, as you will need it to load into Redact-It


## Installation
Clone the repo. Running make build a virtual environment with all of the dependecies you need installed. The first time you run the program you will need to load some NLTK data dictionaries, as per http://www.nltk.org/data.html.

Once the script is built, ./extract_names.py can be used to process test files, and outputs the stopwords it finds. 
