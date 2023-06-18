
# YCEP 2023 Challenge Submissions

This repository contains a database of challenges, container configurations and CTFd hosting scripts for YCEP 2023.

## Local Deployment

For local-testing of challenges, run:

```bash
gh login auth -w
git clone https://github.com/SPGryphons/YCEP-Challenges-2023
cd ./YCEP-Challenges-2023/"$c"/service/
docker run --rm -it $(docker build -q .)
```
    
## Deployment

For porting/hosting on challenge server, run:

```bash
gh login auth -w
git clone https://github.com/SPGryphons/YCEP-Challenges-2023
cd ./YCEP-Challenges-2023
docker compose up -d
```
