
# YCEP 2023 Challenge Submissions (Pre-Rejection)
This repository contains every challenge submitted to YCEP before they were vetted and removed. 

## Local Deployment

For local-testing of challenges, run:

```bash
gh login auth -w
git clone https://github.com/DISMGryphons/YCEP-Challenges-2023
cd ./YCEP-Challenges-2023/"$c"/service/
docker run --rm -it $(docker build -q .)
```
    
## Deployment

For porting/hosting on challenge server, run:

```bash
gh login auth -w
git clone https://github.com/DISMGryphons/YCEP-Challenges-2023
cd ./YCEP-Challenges-2023
docker compose up -d
```

## Contributing

Fork the `hotfix` branch and *never* commit directly to the master branch. 

Please ensure that your changes do not conflict with previous commits, and open a pull-request.

```bash
git checkout hotfix
git commit -m "$m"
git push 
```
