#!/bin/bash

JFROG_URL=$1
TOKEN=$2
FILE=$3

curl -H "Authorization: Bearer $TOKEN" -T $FILE "$JFROG_URL/artifactory/libs-release-local/"
