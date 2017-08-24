#!/usr/bin/env python
# coding: utf-8

'''
emoji_converter.py

Script to convert emoji to their description (e.g., 😊 > :smiling face with smiling eyes:)
or vice versa by making use of the Python emoji module [https://pypi.python.org/pypi/emoji/]

Date: 15.06.2016
'''

import codecs
import emoji
import sys


def replace_emoji_in_text(filePath):
	assert filePath.endswith('.txt') or filePath.endswith('.tsv')
	outfilePath = filePath[:-4] + '_emoji_replaced.txt'
	outF = codecs.open(outfilePath, 'w','utf8')
	inL = codecs.open(filePath, 'r', 'utf8').readlines()
	# Convert emoji to UTF-8 descriptions
	for line in inL:
		outF.write(emoji.demojize(line))
	outF.close()

def replace_descriptions_back_to_emoji(filePath):
	assert filePath.endswith('.txt') or filePath.endswith('.tsv')
	outfilePath = filePath[:-4] + '_emoji.txt'
	outF = codecs.open(outfilePath, 'w','utf8')
	inL = codecs.open(filePath, 'r', 'utf8').readlines()
	# Convert descriptions back to original emoji
	for line in inL:
		outF.write(emoji.emojize(line))
	outF.close()


def main():
    filePath = sys.argv[1] # path to the input file
    replace_emoji_in_text(filePath)
#     replace_descriptions_back_to_emoji(filePath)
    
if __name__ == "__main__":
    main()