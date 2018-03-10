#!/usr/bin/env python3

import os
import sys
import csv

class Analyzer:
    def __init__(self):
        self.hn = ''
        self.idxs = {'meal'     : -1,
                     'drink'    : -1,
                     'snack'    : -1,
                     'internet' : -1,
                     'venue'    : -1,
                     'judging'  : -1,
                     'opening'  : -1,
                     'closing'  : -1,
                     'happening': -1,
                     'excited'  : -1,
                     'recommend': -1}
        self.data = {'meal'     : [],
                     'drink'    : [],
                     'snack'    : [],
                     'internet' : [],
                     'venue'    : [],
                     'judging'  : [],
                     'opening'  : [],
                     'closing'  : [],
                     'happening': [],
                     'excited'  : [],
                     'recommend': []}
        self.grades = ['F', 
                       'D-', 'D', 'D+', 
                       'C-', 'C', 'C+', 
                       'B-', 'B', 'B+', 
                       'A-', 'A', 'A+']
        self.grade_ranges = [59.5, 62.5, 66.5, 
                             69.5, 72.5, 76.5, 
                             79.5, 82.5, 86.5, 
                             89.5, 92.5, 96.5]

    def load_data(self, hackathon_name):
        self.hn = hackathon_name
        with open(self.hn + '.csv') as f:
            # Extract dialect
            dialect = csv.Sniffer().sniff(f.read(1024))
            f.seek(0)
            reader = csv.reader(f, dialect)

            # Extract headers from CSV file
            headers = next(reader)

            # Get indexes of keys
            for key in self.idxs:
                self.idxs[key] = self.find_index(key, headers)

            # Load data for each key
            for row in reader:
                for key in self.data:
                    temp = row[self.idxs[key]]
                    if type()


    def find_index(self, target, questions):
        i = 0
        for question in questions:
            if target in question.lower():
                return i
            i += 1
        return -1

    def analyze(self):
        # compile scores for each question
        # assign grades for each
        # Assign overall grade