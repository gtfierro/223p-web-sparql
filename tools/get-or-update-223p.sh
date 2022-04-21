#!/bin/bash

if [ ! -d "223standard" ] ; then
    git clone https://bas-im.emcs.cornell.edu/223/223standard
fi

cd 223standard && git pull && cd ..
