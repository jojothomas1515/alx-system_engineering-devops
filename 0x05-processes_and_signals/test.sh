#!/usr/bin/env bash
#wow

cleans ()
{
    echo "trap have been run"
    echo
}

trap cleans 1 2 3 6


while ((1));
do
    echo "hello"
    sleep 2
    
done
