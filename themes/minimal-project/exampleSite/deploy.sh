#!/bin/sh

# Need to be in main for building webpage
git checkout main

# Add changes to git.
git add .

# Commit changes.
read -p "Enter 'main' commit message: " msg
git commit -m "$msg"
git push origin main

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

# Build the project.
hugo # if using a theme, replace with `hugo -t <YOURTHEME>`

# Change branch to gh-pages
# Assumes that there already exists a gh-pages branch
git checkout gh-pages

# Copy everything from public folder
cp -r public/* .

# Remove the public/ folder
sudo rm -r public/

# Add changes to git.
git add .

# Commit changes.
git commit -m "$msg"

# Push source and build repos.
git push origin gh-pages

# Change the branch back
git checkout main