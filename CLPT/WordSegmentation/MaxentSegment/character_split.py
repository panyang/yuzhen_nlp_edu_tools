#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 52nlpcn@gmail.com
# Copyright 2014 @ YuZhen Technology
#
# split chinese characters to single charachter and add space between them

import codecs
import sys

def character_split(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    for line in input_data.readlines():
        for word in line.strip():
            output_data.write(word + " ")
        output_data.write("\n")
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Please use: python character_split.py input output"
        sys.exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    character_split(input_file, output_file)
