#!/usr/bin/env python
# encoding: utf-8

"""
evaluate.py

This is the scoring script for SemEval-2018 Task 3: Irony detection in English tweets.

The script:
    - is be used to evaluate Task A and Task B
    - takes as input a file containing 1 prediction per line
    - calculates accuracy, precision, recall and F1-score.

Date: 08.08.2017
"""

from __future__ import division
import codecs
import sys
import os


def preliminary_check(input_dir):
    """Checks the task and whether the data format corresponds with the task"""
    fileCount = 0
    # Check presence and format of the prediction files
    for el in os.listdir(os.path.join(input_dir, 'res')):
        if 'predictions-task' in el:
            fileCount += 1
    if fileCount > 1:
        print "Warning: there should only be 1 prediction file in your submission dir. Evaluation stopped."
        sys.exit()
    if el == 'predictions-taskA.txt':
        predictionsfile = os.path.join(input_dir, 'res', 'predictions-taskA.txt')
        goldfile = os.path.join(input_dir, 'ref', 'goldstandard-taskA.txt')
    elif el == 'predictions-taskB.txt':
        predictionsfile = os.path.join(input_dir, 'res', 'predictions-taskB.txt')
        goldfile = os.path.join(input_dir, 'ref', 'goldstandard-taskB.txt')
    else:
        print "Warning, the prediction file should either be predictions-taskA.txt or predictions-TaskB.txt. Evaluation stopped."
        sys.exit()
    return predictionsfile, goldfile


def calculate_score(predictionsfile, goldfile, outfilepath):
    """Calculates the submission scores"""
    predicted = codecs.open(predictionsfile, "r", "utf8").readlines()
    gold = codecs.open(goldfile, "r", "utf8").readlines()
    outf = codecs.open(outfilepath, 'w','utf8')
    task = None
    assert len(gold) == len(predicted), "Warning: check whether the files contain 1 prediction per instance."
    predicted_labels = []
    gold_labels = []
    for pred, gold in zip(predicted,gold):
        predicted_labels.append(int(pred))
        gold_labels.append(int(gold))
    # Calculate accuracy
    accuracy = calc_accuracy(gold_labels, predicted_labels)
    # Check which task is evaluated, based on the labels in the gold standard
    if list(set(gold_labels)) == list(set(predicted_labels)) == [0,1]:
        task = "A"
    elif list(set(gold_labels)) == list(set(predicted_labels)) == [1,2,3,4]:
        task = "B"
    else:
        print "Warning: some labels are not recognised. Remember that class labels are [0,1] for task A and [1,2,3,4] for task B."
        sys.exit()
    if task == "A":
        precision, recall, fscore = precision_recall_fscore(gold_labels, predicted_labels, labels= [0,1], pos_label= 1)
        outf.write("%s %s\n%s %s\n%s %s\n%s %s\n" % ("Accuracy:", accuracy, "Precision:", precision, "Recall:", recall, "F1-score:", fscore))
    elif task == "B":
        precision, recall, fscore = precision_recall_fscore(gold_labels, predicted_labels, labels= [1,2,3,4], average= "macro")
        outf.write("%s %s\n%s %s\n%s %s\n%s %s\n" % ("Accuracy:", accuracy, "Macro-avg. precision:", precision, "Macro-avg. recall:", recall, "Macro-avg. F1-score:", fscore))
    outf.close()


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


    # If there is only 1 label of interest, return the scores.
    # No averaging needs to be done.
    if pos_label:
        d = ldict[pos_label]
        return (d["precision"], d["recall"], d["fscore"])

    else:
        # Macro-average scores
        for label in ldict.keys():
            avg_precision = sum(l["precision"] for l in ldict.values()) / len(ldict)
            avg_recall = sum(l["recall"] for l in ldict.values()) / len(ldict)
            avg_fscore = sum(l["fscore"] for l in ldict.values()) / len(ldict)
        return avg_precision, avg_recall, avg_fscore


def main():
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    outfile = os.path.join(output_dir, 'scores.txt')
    predictionsfile, goldfile = preliminary_check(input_dir)

    calculate_score(predictionsfile, goldfile, outfile)
    
    
if __name__ == "__main__":
    main()
