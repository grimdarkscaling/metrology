#!/usr/bin/env bash
for file in data/*
do
    ./scripts/validate_schema.py $file
done
