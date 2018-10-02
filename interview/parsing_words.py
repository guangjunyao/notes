"""
Created on Tue Oct 02 14:28:24 2018

@author: Wei Wu
"""
import sys
import re
import string


def wordparser(input_lines):
    """
    Given a set of lines, return the count of unique words and letters. A word is defined as any sequence of one or more lower-case letters (no numbers, no punctuation) where words are separated by white space

    Args:
        input_lines : list of lines from std intput to be parsed

    Returns:
        str : A string containing the following information:
            the count of words in the input
            the word "words"
            each unique word, and the count of times it occurs in the input (in alphabetical order, each on its own line)
            the word "letters"
            for every letter from a to z, the letter, and the count of times that letter occurred IN A WORD in the input

        Example output would be similar to the following:
            words
            test 1
            case 1
            letters
            a 1
            c 1
            e 2
            s 1
            t 2

         As a result string "words\ntest 1\ncase 1\nletters\na 1\nc 1\ne 2\ns 1\nt 2\n"
    """
    tmp = []
    findNonWord = False
    wordList = []

    for iLine in input_lines:
        findNonWord = False
        for idx in range(len(iLine)):
            iChar = iLine[idx]

            if re.match("[a-z]", iChar) and not findNonWord:
                tmp.append(iChar)
            elif iChar == ' ':
                if not findNonWord and len(tmp) > 0:
                    wordList.append(''.join(tmp))
                tmp = []
                findNonWord = False
            else:
                findNonWord = True
                tmp = []

            if idx == len(iLine) - 1:
                if not findNonWord and len(tmp) > 0:

                    wordList.append(''.join(tmp))
                tmp = []

    # print wordList
    # print ''
    result = ''
    wordCount = len(wordList)
    result = result + str(wordCount) + '\n'
    # print wordCount
    result = result + 'words' + '\n'
    # print 'words'
    wordSet = sorted(set(wordList))

    for iWord in wordSet:
        # print iWord + " " + str(wordList.count(iWord))
        result = result + iWord + ' ' + str(wordList.count(iWord)) + '\n'
    # print 'letters'
    result = result + 'letters' + '\n'
    for iLetters in string.lowercase[:26]:
        count = 0
        for iWord in wordList:
            count += iWord.count(iLetters)
        # print iLetters + " " + str(count)
        result = result + iLetters + " " + str(count) + '\n'
        count = 0
    return result
