#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

from strategies.markov_bigrams import MarkovBigramsStrategy
from strategies.concatenation import ConcatenationStrategy
from corpus import HillCorpus

"""
Generate hill names.
"""
class HillGenerator:
    def __init__(self, corpus_filename, strategy):
        self.corpus = HillCorpus()
        self.corpus.load_file(corpus_filename)
        if strategy == 'markov-bigrams':
            self.strategy = MarkovBigramsStrategy(self.corpus)
        elif strategy == 'concatenation':
            self.strategy = ConcatenationStrategy(self.corpus)
        else:
            raise AssertionError
        self.strategy.train()

    def generate_name(self):
        return self._format_name(self.strategy.generate())

    def _format_name(self, name):
        return ' '.join(i.capitalize() for i in name.split(' '))
