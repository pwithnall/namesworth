#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

from corpus import HillCorpus

if __name__ == '__main__':
    corpus = HillCorpus()
    corpus.load_file('hbdownload.csv')
    for row in corpus.names:
        print(row)
