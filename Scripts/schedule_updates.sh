#!/bin/bash

# Path to the reviewed_links_update.sh script
SCRIPT_PATH="./reviewed_links_update.sh"

# Function to call the reviewed_links_update.sh script
run_update_script() {
  bash "$SCRIPT_PATH"
}

# Main loop
while true; do
  echo "Running reviewed_links_update.sh: $(date)"
  run_update_script
  echo "Waiting for 15 minutes before the next update..."
  sleep 900 # Sleep for 15 minutes
done


