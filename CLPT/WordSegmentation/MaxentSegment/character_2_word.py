#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 52nlpcn@gmail.com
# Copyright 2014 @ YuZhen Technology
#
# Combining characters based the 4-tag tagging info

import codecs
import sys

def character_2_word(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')
    # 4 tags for character tagging: B(Begin), E(End), M(Middle), S(Single)
    for line in input_data.readlines():
        char_tag_list = line.strip().split()
        for char_tag in char_tag_list:
            char_tag_pair = char_tag.split('/')
            char = char_tag_pair[0]
            tag = char_tag_pair[1]
            if tag == 'B':
                output_data.write(' ' + char)
            elif tag == 'M':
                output_data.write(char)
            elif tag == 'E':
                output_data.write(char + ' ')
            else: # tag == 'S'
                output_data.write(' ' + char + ' ')
        output_data.write("\n")
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Please use: python character_2_word.py input output"
        sys.exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    character_2_word(input_file, output_file)
