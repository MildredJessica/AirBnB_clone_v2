#!/usr/bin/env bash
# Sets up web server for deployment of web_static

folder1="data"
folder2="web_static"
folder3="releases"
folder4="shared"
folder5="tests"

if [ ! -d "/$folder1/$folder2/$folder3/$folder4" ]
then 
    mkdir -p "/$folder1/$folder2/$folder3/$folder4"
fi

