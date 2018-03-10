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
        try:
            if hackathon_name[-4:] == '.csv':
                self.hn = hackathon_name[:-4]
            else:
                self.hn = hackathon_name
        except IndexError:
            self.hn = hackathon_name

        with open(self.hn + '.csv') as f:
            # Extract dialect
            # dialect = csv.Sniffer().sniff(f.read(1024))
            # f.seek(0)
            # reader = csv.reader(f, dialect)
            reader = csv.reader(f, quotechar='"', delimiter=',')

            # Extract headers from CSV file
            headers = next(reader)

            # Get indexes of keys
            for key in self.idxs:
                self.idxs[key] = self.find_index(key, headers)

            # Load data for each key
            for row in reader:
                for key in self.data:
                    temp = row[self.idxs[key]]
                    try:
                        temp = int(temp)
                    except ValueError:
                        if temp == 'Strongly agree':
                            temp = 5
                        elif temp == 'Somewhat agree':
                            temp = 4
                        elif temp == 'Neither agree nor disagree':
                            temp = 3
                        elif temp == 'Somewhat disagree':
                            temp = 2
                        elif temp == 'Strongly disagree':
                            temp = 1
                        else:
                            # Why would there be an error?
                            sys.exit('Found invalid value in column {}: {}'.format(key, temp))
                    if temp not in list(range(1, 11)):
                        continue
                    self.data[key].append(temp)

    def find_index(self, target, questions):
        i = 0
        # Iterate through the questions in headers to look for indexes of target
        for question in questions:
            if target in question.lower():
                return i
            i += 1
        return -1

    def get_grade(self, percentage):
        return self.grades[sum((i / 100.0) < percentage for i in self.grade_ranges)]

    def analyze(self):
        print('\nReport Card for {}:'.format(self.hn))
        print('---')
        # compile scores for each question
        question_grades = {}
        for key in self.data:
            temp = self.data[key]
            if len(temp) == 0:
                # Didn't find any values entered for this question
                continue
            question_grades[key] = sum(temp) / float(len(temp))

        # assign grades for each
        total = 0
        for key in question_grades:
            temp = question_grades[key] / 5
            if key == 'recommend':
                temp /= 2
            print('{}: {}'.format(key, self.get_grade(temp)))
            total += temp

        # Assign overall grade
        print('---')
        temp = question_grades.values()
        avg_score = total / float(len(temp))
        print('Your overall grade is: {}\n'.format(self.get_grade(avg_score)))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit('Usage: ./analyze.py [hackathon_name]')

    hackathon_name = sys.argv[1]

    analyzer = Analyzer()

    #try:
    analyzer.load_data(hackathon_name)
    #except:
    #    sys.exit('Invalid hackathon name: {}'.format(hackathon_name))

    analyzer.analyze()
