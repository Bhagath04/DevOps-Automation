#!/bin/bash

aws ec2 run-instances --image-id ami-0abcdef12345 --count 1 --instance-type t2.micro --key-name mykey
