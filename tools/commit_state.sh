#!/usr/bin/env bash
# Save the bot's state files back to the repo (used by both bot workflows).
# The bot is the only writer of these files and the workflow's concurrency group allows one
# consumer at a time, so the files this run changed always win: fetch the newest branch, put our
# copies on top, push. No rebase, so no merge conflicts.
# Why (9 Oct 2026): a queued run started from an old commit, rebased its state.json onto a newer
# one, hit a conflict, failed, and the failed save skipped the successor handoff. The bot went quiet.
set -u
MSG="${1:-bot state}"
BRANCH="${BRANCH_NAME:-main}"
git config user.name "mtrx-bot"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git rebase --abort >/dev/null 2>&1 || true
CHANGED=$(git status --porcelain --untracked-files=all -- bot/state.json bot/selftest.json bot/selftest-sources.json bot/questions | sed 's/^...//' | sed 's/.* -> //')
if [ -z "$CHANGED" ]; then echo "No changes to save."; exit 0; fi
TMP=$(mktemp -d)
for f in $CHANGED; do if [ -e "$f" ]; then mkdir -p "$TMP/$(dirname "$f")"; cp "$f" "$TMP/$f"; fi; done
for i in 1 2 3 4 5; do
  if ! git fetch -q origin "$BRANCH"; then sleep $((i * 3)); continue; fi
  git reset -q --hard "origin/$BRANCH"
  for f in $CHANGED; do if [ -e "$TMP/$f" ]; then mkdir -p "$(dirname "$f")"; cp "$TMP/$f" "$f"; git add "$f"; fi; done
  if git diff --cached --quiet; then echo "No changes to save."; exit 0; fi
  git commit -q -m "$MSG [skip ci]"
  if git push -q origin "HEAD:$BRANCH"; then echo "Saved ($i)."; exit 0; fi
  sleep $((i * 3))
done
echo "Could not push state."
exit 1
