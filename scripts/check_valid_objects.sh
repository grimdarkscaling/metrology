#!/usr/bin/env bash
for file in data/*
do
    pipenv run ./scripts/validate_schema.py $file
done
