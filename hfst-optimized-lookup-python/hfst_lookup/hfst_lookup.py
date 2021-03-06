#!/usr/bin/python

import sys
import os
from shared import Header, Alphabet, LetterTrie
from transducer import Transducer
from transducer import TransducerW

class OlTransducer:
    def __init__(self, filename):
        '''Read a transducer from filename
        '''
        handle = open(filename, "rb")
        self.header = Header(handle)
        self.alphabet = Alphabet(handle, self.header.number_of_symbols)
        if self.header.weighted:
            self.transducer = TransducerW(handle, self.header, self.alphabet)
        else:
            self.transducer = Transducer(handle, self.header, self.alphabet)
        handle.close()
    def analyse(self, string):
        '''Take string to analyse, return a vector of (string, weight) pairs.
        '''
        if self.transducer.analyze(string):
            return self.transducer.displayVector
        else:
            return []
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python HfstRuntimeReader FILE"
        sys.exit()
    transducerfile = open(sys.argv[1], "rb")
    header = Header(transducerfile)
    print "header read"
    alphabet = Alphabet(transducerfile, header.number_of_symbols)
    print "alphabet read"
    if header.weighted:
        transducer = TransducerW(transducerfile, header, alphabet)
    else:
        transducer = Transducer(transducerfile, header, alphabet)
    print "transducer ready"
    print

    while True:
        try:
            string = raw_input()
        except EOFError:
            sys.exit(0)
        print string + ":"
        if transducer.analyze(string):
            transducer.printAnalyses()
            print
        else:
            # tokenization failed
            pass
