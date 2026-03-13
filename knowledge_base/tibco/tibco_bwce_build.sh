#!/bin/bash

mvn clean install

docker build -t tibco-app .

docker push myregistry/tibco-app
