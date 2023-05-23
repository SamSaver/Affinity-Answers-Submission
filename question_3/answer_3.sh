#!/bin/bash

# Download the file
wget -q https://www.amfiindia.com/spages/NAVAll.txt

# Extract the Scheme Name and Asset Value fields only and ignore the fields that don't have 6 values seperated by ';'
cat NAVAll.txt | awk -F ';' '{if (NF == 6) print $4","$5}' > output.csv

# Remove the downloaded file
rm NAVAll.txt