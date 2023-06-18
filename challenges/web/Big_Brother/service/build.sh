#!/bin/sh
docker build -t brother .
docker run --restart always --memory 128M -d -p 4000:4000 --name big_brother brother