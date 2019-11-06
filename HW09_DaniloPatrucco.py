# Danilo Patrucco
# CS 100 2019F Section 103
# HW 09, November 04, 2019

import re
import string

print("\r\nProblem 1: \r\n")


def file_copy(in_file, out_file):
    copy_f = open(in_file, 'r')
    write_f = open(out_file, 'w')
    read_copy = copy_f.read()
    write_f.write(read_copy)
    copy_f.close()
    write_f.close()
    return 'Costello!'


print(file_copy('infile.txt', 'outfile.txt'))

print("\r\nProblem 2: \r\n")


def file_stats(in_file):
    infile = open(in_file, 'r')
    in_line = infile.read()
    counts = []
    nr_lines = in_line.splitlines()
    counts.append(len(nr_lines))
    nr_words = re.split('\n| ', in_line)
    counts.append(len(nr_words))
    counts.append(len(in_line))
    infile.close()
    return counts


stats = file_stats('test.txt')

print('\n', 'nr of lines', stats[0], '\n', 'nr of words', stats[1], '\n', 'nr of chars', stats[2])

print("\r\nProblem 3: \r\n")


def repeat_words(in_file, out_file):
    inFile = open(in_file, 'r')
    outFile = open(out_file, 'w')
    readInFile = inFile.read()
    lowText = readInFile.lower()
    nrLines = lowText.splitlines()
    newListlines = []
    for i in nrLines:
        newListlines.append(re.sub(r'[^A-Za-z0-9 ]+', '', i))
    for i in newListlines:
        emptList = []
        newListwords = i.split()
        for l in newListwords:
            if newListwords.count(l) > 1 and l not in emptList:
                emptList.append(l)
        for a in range(len(emptList)):
            if len(emptList[a]) != 0:
                outFile.write(emptList[a])
                outFile.write(' ')
            if len(emptList)-1 == a:
                outFile.write('\n')
    outFile.close()

    return


repeat_words('infile2.txt', 'outfile2.txt')


#problem 3 in class
# WITH LIST

def repeat_words(in_file, out_file):
    inf = open(in_file, 'r')
    outf = open(out_file, 'w')
    lines = inf.readlines()
    for line in lines:
        line = line.lower()
        words = line.split()
        clean_words = []
        for word in words:
            clean_word = word.strip(string.punctuation)
            clean_words.append(clean_word)
        dups = []
        for word in clean_words:
            if word not in dups and clean_words.count(word) > 1:
                dups.append(word)
        for word in dups:
            outf.write(word + ' ')
        outf.write('\n')
        inf.close()
        outf.close()


# WITH DICTIONARIES

def repeat_words(in_file, out_file):
    inf = open(in_file, 'r')
    outf = open(out_file, 'w')
    lines = inf.readlines()
    for line in lines:
        line = line.lower()
        words = line.split()
        clean_words = []
        for word in words:
            clean_word = word.strip(string.punctuation)
            clean_words.append(clean_word)
        d = {}
        for word in clean_words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        for word in d:
            if d[word] > 1:
                outf.write(word + ' ')
        outf.write('\n')

    inf.close()
    outf.close()

