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

# Add only the reviewed_links.txt file to the staging area
git add data/reviewed_links.txt

# Check if there are any changes to commit
if git diff --staged --quiet; then
  echo "$(date): No changes to commit."
else
  # Commit the changes with the specified message
  git commit -m "Added reviewed links"

  # Push the changes to the remote repository
  git push origin main
  echo "$(date): Changes committed and pushed."
fi


