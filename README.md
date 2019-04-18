# Scripts from my 2018 Master's thesis

Scripts to read the DTA (Deutsches Textarchiv; German text archive), generate .json-files and calculate the spelling counts and entropies; also a Monte Carlo simulation based on these files
\[older scripts from 2018\]

## Usage

A config.py-file which looks as follows is needed:

```python
XML_PATH = '' # the path with the original DTA files (.tcf.xml)
JSON_PATH = '' # the path where the .json-files should be saved
OUTPUT_PATH = '' # the path where the results of the Monte Carlo simulation should be saved
```

readall.py is for generating the .json-files. It has to be executed before the Monte Carlo simulation can be used.


## Background information

The .tcf.xml-format in which the DTA can be obtained contains the following layers:
* metadata
* tokens
* [sentences]
* lemmas
* POS-Tags
* corrections (if necessary)

These are used to generate multiple instances of the following objects:
* *Spelling* (from the tokens)
* *Wordform* (from the corrections if available, otherwise from the tokens)
* *Lemma* (from lemmas)

*Text*s contain metadata and *Lemma*s from one text.
*Collection*s contain only *Lemma*s.
*Lemma*s contain *Wordform*s.
*Wordform*s contain *Spelling*s.
And *Spelling*s contain spelling counts.

All of these are put into one dictionary per text/collection and saved as .json-files.