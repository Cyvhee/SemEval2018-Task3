---
# SemEval18 Irony Shared Task Example Scripts
This repository contains a benchmark system for the SemEval-2018 Task 3 <b>Irony detection in English tweets</b>.
The script <tt>example.py</tt> contains Python example code for simple featurisation and classification using the Scikit-learn library.

The script is written in Python 3 but is Python 2 compatible.


## Dependencies
- Python 3.6.x
- NLTK 3.2.4
- numpy 1.13.1
- scikit-learn 0.19.0
- scipy 0.19.1
- six 1.10.0

Python module dependencies can be found in `requirements.txt`

Install with pip:
`pip install -r requirements.txt`

## Usage
Run `python example.py` from terminal.

**NOTE**: the path to the input file and the task (A or B) has to be hard-coded in the script.