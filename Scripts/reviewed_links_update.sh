#!/bin/bash

# Pull the latest changes from the repository
git pull

# Add all changes to the staging area
git add .

# Commit the changes with the specified message
git commit -m "Added reviewed links"

# Push the changes to the remote repository
git push


