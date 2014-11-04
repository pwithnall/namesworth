#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

from generator import HillGenerator
import random

if __name__ == '__main__':
    random.seed()
    generator = HillGenerator('hbdownload.csv', 'markov-bigrams')
    for i in range(1, 10):
        print(generator.generate_name())
