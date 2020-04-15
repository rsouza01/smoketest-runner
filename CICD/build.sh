#!/usr/bin/env bash


clear
# exit when any command fails
set -e

echo "------------------------------------------------------------------"
echo "UNIT TESTS"
echo "------------------------------------------------------------------"
python -m unittest discover ./test/unit -v
