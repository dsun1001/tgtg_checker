Notes

docker build -f Dockerfile.txt -t tgtg-check .
docker tag tgtg-check:latest 211494723049.dkr.ecr.us-east-1.amazonaws.com/tgtg-check:latest
docker push 211494723049.dkr.ecr.us-east-1.amazonaws.com/tgtg-check:latest
