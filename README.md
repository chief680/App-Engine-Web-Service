# App Engine Web Service
This is a walk through on creating a json to xml service on GCloud with AppEngine and Flask

# GCloud SDK
- download the GCloud SDK
- extract the files, then run ./google-cloud-sdk/install.sh
- when done, run "gcloud init: to initilize the sdk

# Create a project
- gcloud project create project-base-id

# Create an app
- gcloud app create

# Write the web service
- name your main module main.py
- create app.yaml, this is your config file for Flask
- create requirements.txt, make sure Flask is in it

# Deploy the service
- gcloud deploy
