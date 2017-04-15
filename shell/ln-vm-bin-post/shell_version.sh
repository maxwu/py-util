#!/bin/bash
# For fun, to translate 0|1 string sets to asc text, Apr 2017.--Max
for x in $(cat d_reply.txt|tr ' ' "\n"); do echo "obase=16; ibase=2; $x"| bc| xxd -r -p; done
