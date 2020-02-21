# PREREQS
#
# 1. sign in on gcloud
#   gcloud auth login
#
# 2. setup docker
#   gcloud auth configure-docker
#
param(
[string]$version
)

$ErrorActionPreference = "Stop"

# run with:
# .\buildme.ps1 v0.0.1

echo generating version: $version

docker build -f Dockerfile -t gcr.io/gps-van-tracker/gps-listener:${version} .
gcloud docker -- push gcr.io/gps-van-tracker/gps-listener:${version}
# gcloud beta run deploy van-tracker --image gcr.io/gps-van-tracker/gps-listener:latest --region europe-west1 --allow-unauthenticated --platform managed
