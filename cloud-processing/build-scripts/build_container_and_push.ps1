# PREREQS
#
# 1. sign in on gcloud
#   gcloud auth login
#
# 2. setup docker
#   gcloud auth configure-docker
#
# 3. set your project
#   $project = "your-project-here"

param(
[string]$version
)

$project = "gps-van-tracker"
$ErrorActionPreference = "Stop"

# run with:
# ./build_container_and_push.ps1 v1.0.0

echo generating version: $version

# a little naive, we should really fully resolve the path here via python or similar
cd ..
cd process-gps-points
# This builds the app into a tagged docker container.
# The tag is important, it specifics which google project contaienr storage to push to.
docker build -f Dockerfile -t gcr.io/${project}/gps-points-processing:${version} .

# The container is now pushed to the cloud container repository
docker push gcr.io/${project}/gps-points-processing:${version}

# this deploys the app. Note the "beta" - at some point this will become deprecated, and the command will become
# more like "gcloud run deploy ..."
gcloud beta run deploy cloud-processing --image gcr.io/gps-van-tracker/gps-points-processing:${version} --region europe-west1 --platform managed --project=${project} # --allow-unauthenticated

# back to the build directory
cd ..
cd build-scripts