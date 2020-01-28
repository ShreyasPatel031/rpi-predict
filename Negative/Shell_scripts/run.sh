#!/usr/bin/env bash

cd /Users/shreyaspatel/blast/db


blastn -db database.fa -query query.fa -outfmt 10 -out op.csv -num_threads 8
