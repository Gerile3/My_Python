#!/bin/sh

while sleep 3;do
  cat /dev/null > test.txt
  cat  < /dev/ttyUSB0 >> test.txt
  echo "starting"
done

if grep -Fxq 'test' /home/pi/test.txt
  then
    echo "done here"
  else
    echo "nothing here"
fi
