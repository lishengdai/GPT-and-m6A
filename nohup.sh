#!/bin/bash

for line in $(cat data/m6a_char/prompt.txt); do python sample.py --out_dir=out-m6a-char --start=${line} | grep -m 1 "@#" >>out-m6a-char/prediction.txt;done
