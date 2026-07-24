#!/bin/bash

# Check if archive directory exists, if not create it
if [ ! -d "archive" ]; then
    mkdir archive
fi

# Generate timestamp
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# Rename and move grades.csv to archive
mv grades.csv archive/grades_${TIMESTAMP}.csv

# Create fresh empty grades.csv
touch grades.csv

# Log the operation
echo "[$TIMESTAMP] Archived grades.csv as grades_${TIMESTAMP}.csv" >> organizer.log

echo "Done. grades.csv archived and fresh file created."
