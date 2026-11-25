#!/usr/bin/env bash



if git check-ignore -q .env; then
    echo "PASS: .env is ignored."
else
    echo "FAIL: .env is NOT ignored! (Security issue)"
fi


if git diff --cached --name-only | grep -q .venv; then
    echo "FAIL: .venv files are staged!"
else
    echo "PASS: .venv files are not staged."
fi

LAST_COMMIT_MSG=$(git log -1 --format=%s)
EXPECTED_MSG="docs(week-01): add day-4 notes"
if [ "$LAST_COMMIT_MSG" == "$EXPECTED_MSG" ]; then
    echo "PASS: Commit message is correct."
else
    echo "FAIL: Commit message is wrong . Got: '$LAST_COMMIT_MSG'"
fi

if git ls-remote origin main | grep -q "refs/heads/main"; then
    echo "PASS: Successfully pushed to 'main' branch."
else
    echo "FAIL: Could not find 'main' branch on remote. (Did it push to 'master'?)"
fi

echo "=== Tests Finished ==="
