#! /usr/bin/env bash

BASE_DIR="$(dirname $0)/.."

YEAR=$(date +%Y)
DAY=$(date +%d)

while getopts "y:d:" opt; do
    case $opt in
        y) YEAR=$OPTARG ;;
        d) DAY=$OPTARG ;;
        \?) echo "Invalid option -$OPTARG" >&2 ;;
    esac
done

mkdir -p $BASE_DIR/data/$YEAR
mkdir -p $BASE_DIR/docs/$YEAR

touch $BASE_DIR/docs/$YEAR/$(printf "%02d" $DAY).md
touch $BASE_DIR/data/$YEAR/$(printf "%02d" $DAY).data
touch $BASE_DIR/data/$YEAR/$(printf "%02d" $DAY)_test.data
cp -i $BASE_DIR/src/aoc/year_$YEAR/day_xx.py $BASE_DIR/src/aoc/year_$YEAR/day_$(printf "%02d" $DAY).py
