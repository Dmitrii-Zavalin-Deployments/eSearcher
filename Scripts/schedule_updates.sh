#!/bin/bash

# Function to run a script and echo its name and the current date
run_script() {
  echo "Running $1: $(date)"
  bash "$1" | while IFS= read -r line; do
    echo "[$(date)] $1: $line"
  done
}

# Main loop
while true; do
  # Run the reviewed_links_update.sh script
  run_script "./reviewed_links_update.sh"

  # Run the update_search_queries.sh script
  run_script "./update_search_queries.sh"

  # Run the queries_clean_up.sh script
  run_script "./queries_clean_up.sh"

  # Wait for 15 minutes before the next update
  echo "Waiting for 15 minutes before the next update..."
  sleep 900 # Sleep for 15 minutes
done


