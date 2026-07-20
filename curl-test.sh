#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:5001}"
ENDPOINT="$BASE_URL/api/timeline_post"

command -v jq >/dev/null || { echo "jq is required: brew install jq"; exit 1; }
fail() { echo "FAIL: $1"; exit 1; }

SUFFIX="$RANDOM$RANDOM"
NAME="test-user-$SUFFIX"
EMAIL="test-$SUFFIX@example.com"
CONTENT="test post $SUFFIX"

echo "POST $ENDPOINT"
CREATED=$(curl -sf -X POST "$ENDPOINT" \
  -d "name=$NAME" -d "email=$EMAIL" -d "content=$CONTENT") \
  || fail "POST request failed"

POST_ID=$(echo "$CREATED" | jq -r '.id')
[ -n "$POST_ID" ] && [ "$POST_ID" != "null" ] || fail "no id returned from POST"
echo "  created id=$POST_ID"

echo "GET $ENDPOINT"
POSTS=$(curl -sf "$ENDPOINT") || fail "GET request failed"
FOUND=$(echo "$POSTS" | jq --arg c "$CONTENT" \
  '[.timeline_posts[] | select(.content == $c)] | length')
[ "$FOUND" -eq 1 ] || fail "created post not found in GET response"
echo "  PASS: post present"

echo "DELETE $ENDPOINT/$POST_ID"
curl -sf -X DELETE "$ENDPOINT/$POST_ID" >/dev/null || fail "DELETE request failed"

AFTER=$(curl -sf "$ENDPOINT") || fail "GET after delete failed"
LEFT=$(echo "$AFTER" | jq --arg c "$CONTENT" \
  '[.timeline_posts[] | select(.content == $c)] | length')
[ "$LEFT" -eq 0 ] || fail "post survived DELETE"
echo "  PASS: cleanup verified"

echo "All tests passed"
