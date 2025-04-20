#!/bin/bash
echo "Updating brreview..."
git pull || exit 1
sudo docker-compose build || exit 1
sudo docker-compose up -d || exit 1
echo "Update complete."
