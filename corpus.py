#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

import csv
import re

"""
Represent a loaded corpus of hill names.

At the moment it supports the CSV format exported by hill-bagging.co.uk:
http://www.hill-bagging.co.uk/downloadfile.php?ftype=csv&ct=E&gp=M34&ty=all&totals=Y

The list of names may contain duplicates if multiple hills have the same name.
The names are not disambiguated by area.
"""
class HillCorpus:
    def __init__(self):
        self.names = []

    def load_file(self, filename):
        # Grab the names from the CSV file.
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)

            # Ignore the first row of column names.
            reader.next()

            self.names = map(self._filter_names,
                             map(lambda row: row[1], reader))

    """
    Filter hill names to remove extraneous formatting, such as area names.

    Three transformations are applied, in order:
     • Removing square bracketed suffixes (‘A [B]’ → ‘A’)
     • Removing bracketed suffixes (‘A (B)’ → ‘A’)
     • Splitting hyphens (‘A - B’ → ‘B’)
    """
    def _filter_names(self, name):
        # Ends in a square bracket?
        name = re.sub('\s\[.*\]$', '', name)

        # Ends in a round bracket?
        name = re.sub('\s\(.*\)$', '', name)

        # Contains a hyphen?
        if ' - ' in name:
            parts = name.split(' - ', 2)
            return parts[1]

        return name
