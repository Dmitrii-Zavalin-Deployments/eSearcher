#!/bin/bash

# Function to cleanup before exiting
cleanup() {
  echo "Cleanup complete. Exiting."
  exit 0
}

# Trap SIGINT to call the cleanup function on script termination
trap cleanup SIGINT

# Read the query name from queries_to_clean_up.txt
QUERY_NAME=$(<queries_to_clean_up.txt)

# Pull the latest changes from the repository
git pull --rebase origin main

# Navigate to the parent directory of the script
cd "$(dirname "$0")" || { echo "Failed to navigate to the script's directory."; exit 1; }

# Use jq to update data.json
jq --arg query_name "$QUERY_NAME" --arg date_time "$(date)" '.[$query_name] = ["This query was cleaned up at \($date_time)"]' ../data/data.json > temp.json && mv temp.json ../data/data.json

# Clear the queries_to_clean_up.txt file
> queries_to_clean_up.txt

# Check if there are changes in the data.json file
if git diff --quiet ../data/data.json; then
  echo "No changes in data.json"
else
  git add ../data/data.json
fi

# Check if there are changes in the queries_to_clean_up.txt file
if git diff --quiet queries_to_clean_up.txt; then
  echo "No changes in queries_to_clean_up.txt"
else
  git add queries_to_clean_up.txt
fi

# Commit and push only if there were changes
if ! git diff --staged --quiet; then
  git commit -m "Cleaned up query: $QUERY_NAME"
  git push origin main
else
  echo "No changes to commit."
fi


