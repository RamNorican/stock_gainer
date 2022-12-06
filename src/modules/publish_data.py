"""
https://cloud.google.com/pubsub
Google cloud BIG Query
use google cloud client to push data to a topic
create big query table to sink the data
create a temp storage space in cloud bucket

1. Create code to run every 2 minutes
2. Enable cloud based logging
3. Create docker image with some env variabled for production
4. Create github actions to build the docker image and push the image to google cloud docker registry
5. Run compute instance in cloud with image
example flow is given here:
https://github.com/google-github-actions/setup-gcloud/blob/main/example-workflows/gce/README.md
https://medium.com/@vngauv/from-github-to-gce-automate-deployment-with-github-actions-27e89ba6add8
"""
