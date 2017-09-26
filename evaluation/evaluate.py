#!/usr/bin/env python

"""
evaluate.py

This is the scoring script for SemEval-2018 Task 3: Irony detection in English tweets.

The script:
  * is used to evaluate Task A and Task B
  * takes as input a submission dir containing the system output (format: 1 prediction per line)
  * prediction files should be named 'predictions-taskA.txt' and/or 'predictions-taskB.txt'
  * calculates accuracy, precision, recall and F1-score.

Date: 08.08.2017, adapted on 26.09.2017
"""

from __future__ import division
import sys
import os


def score(input_dir, output_dir):
    # unzipped submission data is always in the 'res' subdirectory
    submission_dir = os.path.join(input_dir, 'res')
    submission_file = []
    for el in os.listdir(submission_dir):
        if el.startswith('predictions'):
            submission_file.append(el)
    if not len(submission_file) == 1:
       print ("Warning: the submission folder should only contain 1 file ('predictions-taskA.txt' or 'predictions-taskB.txt'). Process terminated.")
       sys.exit()
    submission_file_name = submission_file[0]
    submission_path = os.path.join(submission_dir, submission_file_name)
    if any (name in submission_file_name.lower() for name in ['taska', 'task-a', 'task_a']):
        task = "A"
    elif any (name in submission_file_name.lower() for name in ['taskb', 'task-b', 'task_b']):
        task = "B"
    else:
        message = "Task not found. Please check the name of your submission file."
        sys.exit()
    with open(submission_path) as submission_file:
        submission = submission_file.readlines()

    # unzipped reference data is always in the 'ref' subdirectory
    if task == "A":
        with open(os.path.join(input_dir, 'ref', 'goldstandard_train_A.txt')) as truth_file:
            truth = truth_file.readlines()
    elif task == "B":
        with open(os.path.join(input_dir, 'ref', 'goldstandard_train_B.txt')) as truth_file:
            truth = truth_file.readlines()

    true = []
    predicted = []
    for s,t in zip(submission, truth):
        if s.strip() and t.strip():
            true.append(int(t.strip()))
            predicted.append(int(s.strip()))

    if task == "A":
        for el in list(set(true+predicted)):
            if not el in [0,1]:
                print ("Warning: some labels are not recognised. Class labels are [0,1] for task A. Process terminated.")
                sys.exit()
    elif task == "B":
        for el in list(set(true+predicted)):
            if not el in [0,1,2,3]:
                print ("Warning: some labels are not recognised. Class labels are [0,1,2,3] for task B. Process terminated.")
                sys.exit()

    with open(os.path.join(output_dir, 'scores.txt'), 'w') as output_file:
        acc = calc_accuracy(true, predicted)
        if task == "A":
            p, r, f = precision_recall_fscore(true, predicted, beta=1, labels=[0,1], pos_label=1)
        elif task == "B":
            p, r, f = precision_recall_fscore(true, predicted, beta=1, labels=[0,1,2,3])
        output_file.write("Accuracy:{0}\nPrecision:{1}\nRecall:{2}\nF1-score:{3}\n".format(acc, p,r,f))


def calc_accuracy(true, predicted):
    """Calculates the accuracy of a (multiclass) classifier, defined as the fraction of correct classifications."""
    return sum([t==p for t,p in zip(true, predicted)]) / float(len(true))


def precision_recall_fscore(true, predicted, beta=1, labels=None, pos_label=None, average=None):
    """Calculates the precision, recall and F-score of a classifier.
    :param true: iterable of the true class labels
    :param predicted: iterable of the predicted labels
    :param beta: the beta value for F-score calculation
    :param labels: iterable containing the possible class labels
    :param pos_label: the positive label (i.e. 1 label for binary classification)
    :param average: selects weighted, micro- or macro-averaged F-score
    """

    # Build contingency table as ldict
    ldict = {}
    for l in labels:
        ldict[l] = {"tp": 0., "fp": 0., "fn": 0., "support": 0.}

    for t, p in zip(true, predicted):
        if t == p:
            ldict[t]["tp"] += 1
        else:
            ldict[t]["fn"] += 1
            ldict[p]["fp"] += 1
        ldict[t]["support"] += 1

    # Calculate precision, recall and F-beta score per class
    beta2 = beta ** 2
    for l, d in ldict.items():
        try:
            ldict[l]["precision"] = d["tp"]/(d["tp"] + d["fp"])
        except ZeroDivisionError: ldict[l]["precision"] = 0.0
        try: ldict[l]["recall"]    = d["tp"]/(d["tp"] + d["fn"])
        except ZeroDivisionError: ldict[l]["recall"]    = 0.0
        try: ldict[l]["fscore"] = (1 + beta2) * (ldict[l]["precision"] * ldict[l]["recall"]) / (beta2 * ldict[l]["precision"] + ldict[l]["recall"])
        except ZeroDivisionError: ldict[l]["fscore"] = 0.0

    # If there is only 1 label of interest, return the scores. No averaging needs to be done.
    if pos_label:
        d = ldict[pos_label]
        return (d["precision"], d["recall"], d["fscore"])
    # If there are multiple labels of interest, macro-average scores.
    else:
        for label in ldict.keys():
            avg_precision = sum(l["precision"] for l in ldict.values()) / len(ldict)
            avg_recall = sum(l["recall"] for l in ldict.values()) / len(ldict)
            avg_fscore = sum(l["fscore"] for l in ldict.values()) / len(ldict)
        return (avg_precision, avg_recall, avg_fscore)


def main():
    [_, input_dir, output_dir] = sys.argv
    score(input_dir, output_dir)
    
    
if __name__ == "__main__":
    main()