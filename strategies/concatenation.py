#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

import random

"""
Name generation strategy concatenating individual words from the corpus.
"""
class ConcatenationStrategy:
    def __init__(self, corpus):
        self.corpus = corpus
        self.words = []

    """
    Train the strategy by splitting the corpus up into individual words.
    """
    def train(self):
        self.words = []
        map(self.words.extend, map(self._extract_words, self.corpus.names))

    """
    Convert a hill name into an array of its words.
    """
    def _extract_words(self, name):
        return filter(None, name.split())

    """
    Minimum and maximum lengths extracted from the corpus.
    """
    def generate(self, min_length = 3, max_length = 26):
        # Name length in words.
        n_words = random.randint(1, 3)
        name = []

        for i in range(1, n_words + 1):
            name.append(random.choice(self.words))

        return ' '.join(name)
