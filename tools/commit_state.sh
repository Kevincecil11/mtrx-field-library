#!/usr/bin/env bash
# Commit the bot's state files (used by the workflows). "[skip ci]" keeps these commits from triggering builds.
set -e
git config user.name "mtrx-bot"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
for f in bot/state.json bot/selftest.json bot/questions; do
  if [ -e "$f" ]; then git add "$f"; fi
done
if git diff --cached --quiet; then echo "No changes to save."; exit 0; fi
git commit -q -m "$1 [skip ci]"
for i in 1 2 3; do
  if git pull -q --rebase && git push -q; then echo "Saved."; exit 0; fi
  sleep 5
done
echo "Could not push state." && exit 1
