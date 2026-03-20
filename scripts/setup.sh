#!/bin/bash

# Initial Setup and Installation of IT Operations Platform

# Update package index
sudo apt update

# Install necessary packages
sudo apt install -y git docker.io

# Start and enable docker
sudo systemctl start docker
sudo systemctl enable docker

# Clone the IT Operations Platform repository
git clone https://github.com/YourOrg/Operations-Platform.git

# Navigate to the cloned directory
cd Operations-Platform

# Run installation script
./install.sh

# Clean up
cd ..
rm -rf Operations-Platform

echo "Setup completed successfully!"