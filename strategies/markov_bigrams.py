#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

import random

"""
Name generation strategy building a Markov chain of the bigrams in the corpus.
"""
class MarkovBigramsStrategy:
    def __init__(self, corpus):
        self.corpus = corpus
        self.chain = MarkovChain()

    """
    Train the strategy by building a Markov chain from the corpus.
    """
    def train(self):
        name_bigrams = map(self._extract_bigrams, self.corpus.names)

        for bigrams in name_bigrams:
            for i in range(1, len(bigrams)):
                self.chain.add_link(bigrams[i - 1], bigrams[i])

    """
    Convert a hill name into an array of its bigrams. The hill name may be
    multiple words.

    http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
    """
    def _extract_bigrams(self, name):
        # TODO: Need to handle spaces between words explicitly.
        input_list = list(name)
        return map(lambda bigram: bigram[0] + bigram[1],
                   zip(input_list, input_list[1:]))

    """
    Minimum and maximum lengths extracted from the corpus.
    """
    def generate(self, min_length = 3, max_length = 26):
        # Name length in characters.
        length = random.randint(min_length, max_length)
        bigram = self.chain.random_node()
        name = bigram

        for i in range(1, length):
            bigram = self.chain.random_successor(bigram)
            if bigram is None:
                break

            name += bigram[1]

        return name


"""
Markov chain.
"""
class MarkovChain:
    def __init__(self):
        self.nodes = {}
        self.total_links = {}

    def add_link(self, node1, node2):
        if node1 not in self.nodes:
            self.nodes[node1] = {}
        if node2 not in self.nodes:
            self.nodes[node2] = {}

        self.nodes[node1][node2] = self.nodes[node1].get(node2, 0) + 1
        self.total_links[node1] = self.total_links.get(node1, 0) + 1
        self.total_links[node2] = self.total_links.get(node2, 0)

    def random_successor(self, node):
        # Does the node have any successors?
        if self.total_links[node] == 0:
            return None

        p = random.randint(1, self.total_links[node])
        links = self.nodes[node].items()
        i = 0;

        while p > links[i][1]:
            p -= links[i][1]
            i += 1

        return links[i][0]

    def random_node(self):
        p = random.randint(0, len(self.nodes) - 1)
        return self.nodes.keys()[p]
