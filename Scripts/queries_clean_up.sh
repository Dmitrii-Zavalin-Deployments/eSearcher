#!/bin/bash

# Function to cleanup before exiting
cleanup() {
  echo "Cleanup complete. Exiting."
  exit 0
}

# Trap SIGINT to call the cleanup function on script termination
trap cleanup SIGINT

# Pull the latest changes from the repository
git pull --rebase origin main

# Navigate to the parent directory of the script
cd "$(dirname "$0")" || { echo "Failed to navigate to the script's directory."; exit 1; }

# Read each query name from queries_to_clean_up.txt and process them
while IFS= read -r QUERY_NAME; do
  # Use jq to update data.json for each query
  jq --arg query_name "$QUERY_NAME" --arg date_time "$(date)" '.[$query_name] = ["This query was cleaned up at \($date_time)"]' ../data/data.json > temp.json && mv temp.json ../data/data.json
done < queries_to_clean_up.txt

# Clear the queries_to_clean_up.txt file after processing all queries
> queries_to_clean_up.txt

# Add, commit, and push changes if there were any
if ! git diff --quiet ../data/data.json queries_to_clean_up.txt; then
  git add ../data/data.json queries_to_clean_up.txt
  git commit -m "Cleaned up queries"
  git push origin main
else
  echo "No changes to commit."
fi


