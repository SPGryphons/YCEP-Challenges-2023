#!/bin/sh
docker build -t ilovepythontoo .
docker run -d -it -p 1234:1234 ilovepythontoo