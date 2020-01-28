#!/usr/bin/env bash

cd /Users/shreyaspatel/blast/db


blastp -db database.fa -query query.fa -outfmt 10 -out op.csv -num_threads 8
