#!/bin/bash

cd /root/ci-cd--herovired-1

git pull

sudo rm -rf /usr/share/nginx/html/*

sudo cp -r ./2117_infinite_loop/* /usr/share/nginx/html/

sudo systemctl restart nginx
