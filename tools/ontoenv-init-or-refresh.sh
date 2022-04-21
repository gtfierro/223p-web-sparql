#!/bin/bash

if [ ! -d ".ontoenv" ] ; then
    ontoenv init
else
    ontoenv refresh
fi
