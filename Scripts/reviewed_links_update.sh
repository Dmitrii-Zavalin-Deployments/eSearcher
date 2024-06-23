#!/bin/bash

# Pull the latest changes from the repository
git pull

# Add only the reviewed_links.txt file to the staging area
git add data/reviewed_links.txt

# Commit the changes with the specified message
git commit -m "Added reviewed links"

# Push the changes to the remote repository
git push


