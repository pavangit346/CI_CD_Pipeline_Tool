#!/bin/bash

cd /root/ci-cd--herovired-1

git log | grep "commit" | head -n 1 | cut -d " " -f2
