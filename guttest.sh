#!/usr/bin/env bash

if godot --path $PWD --no-window -s addons/gut/gut_cmdln.gd ; then
    echo OK
else
    echo False
    
fi
