# 1. Fetch the latest remote information
git fetch origin

# 2. Force your local branch to match the remote's current state
git reset --hard origin/main

# 3. Pull the latest changes (should now be clean)
git pull origin maingit stash
git fetch origin
git reset --hard origin/main
git pull origin main
git stash pop