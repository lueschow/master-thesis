# Scripts from my 2018 Master's thesis

Scripts to read the DTA, generate .json-files and calculate the spelling counts and entropies; also a Monte Carlo simulation based on these files (older scripts from 2018)

## Usage

A config.py-file which looks as follows is needed:

```python
XML_PATH = '' # the path with the original DTA files (tcf.xml)
JSON_PATH = '' # the path where the .json-files should be saved
OUTPUT_PATH = '' # the path where the results of the Monte Carlo simulation should be saved
```

readall.py is for generating the .json-files. It has to be executed before the Monte Carlo simulation can be used.
