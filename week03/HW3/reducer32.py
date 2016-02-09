#!/usr/bin/env python

#
# Use counters to count the number of times the reducer is called
#
from itertools import groupby
from operator import itemgetter
import sys

def read(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):    
    # input comes from STDIN (standard input)
    data = read(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            sys.stdout.write("{0}{1}{2}".format(current_word, separator, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            pass

if __name__ == "__main__":
    # increment counter for reducer call, write to STDERR
    sys.stderr.write("reporter:counter:Code Call Counters,reducer,1\n")
    main()