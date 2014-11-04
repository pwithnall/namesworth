#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

from strategies.markov_bigrams import MarkovBigramsStrategy
from corpus import HillCorpus

"""
Generate hill names.
"""
class HillGenerator:
    def __init__(self, corpus_filename, strategy):
        # Currently only support this strategy.
        if strategy != 'markov-bigrams':
            raise AssertionError

        self.corpus = HillCorpus()
        self.corpus.load_file(corpus_filename)
        self.strategy = MarkovBigramsStrategy(self.corpus)
        self.strategy.train()

    def generate_name(self):
        return self._format_name(self.strategy.generate())

    def _format_name(self, name):
        return ' '.join(i.capitalize() for i in name.split(' '))
