#!/usr/bin/env python3
#coding: utf-8

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    if fields[0].isdigit():
        fields[2] = fields[1]
        print(*fields, sep='\t')
    else:
        print(line)
