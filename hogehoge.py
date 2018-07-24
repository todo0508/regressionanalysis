#!/usr/bin/python
# coding: UTF-8

import csv

c = open('some.csv', 'w') 
f = open('tehe.txt')
line = f.readline()
while line:
    if len(line)>1:
        line = line.strip()
        writer = csv.writer(c, lineterminator='\n')
        writer.writerow(line)
        print(line)
    line = f.readline()
f.close()
c.close()

