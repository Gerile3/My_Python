#!/bin/sh

cat /dev/null > test.txt
cat  < /dev/ttyUSB0 >> test.txt
