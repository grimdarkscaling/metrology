#!/usr/bin/env bash
for file in $1/*
do
    echo "Checking $file is valid JSON"
    jq . $file
done
