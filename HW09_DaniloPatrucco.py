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
    return counts


stats = file_stats('test.txt')

print('\n', 'nr of lines', stats[0], '\n', 'nr of words', stats[1], '\n', 'nr of chars', stats[2])

print("\r\nProblem 3: \r\n")


def repeat_words(in_file, out_file):
    infile = open(in_file, 'r')
    readInFile = infile.read()
    lowText = readInFile.lower()
    nrLines = lowText.splitlines()
    newListlines = []
    outlist = []
    for i in nrLines:
        newListlines.append(re.sub(r'[^A-Za-z0-9 ]+', '', i))
    for i in newListlines:
        emptString = ''
        newListwords = i.split()
        for l in newListwords:
            if newListwords.count(l) > 1 and l not in emptString:
                emptString = emptString + l + " "
        outlist.append(emptString)

    return outlist


cont = repeat_words('infile2.txt', 'outfile2.txt')
for i in range(len(cont)):
    if cont[i] != '':
        print("Line ", i ," repeating words = ", cont[i])
