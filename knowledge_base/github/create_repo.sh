#!/bin/bash

TOKEN=$1
REPO_NAME=$2

curl -X POST https://api.github.com/user/repos -H "Authorization: token $TOKEN" -d "{\"name\":\"$REPO_NAME\"}"
