# gae-microservices-template
Cheapskate google cloud app engine microservices template. Intended to be a simple repo to manage.


Had difficulties getting golang to play nice with the folder structure. Any and all suggestions are welcome.

## Summary

In order to use this repo setup google cloud and google cloud build. You should be able to just build it with google cloud build (see github google cloud build app).

This repo is intended to illustrate how you can deploy microservices without paying for much storage costs (deletes all docker images after deployment).

The actual projects are pretty simple (golang, python, etc ...). Within the google cloud console, you should be able to see each service individually. For each microservice, an `.yaml` file is required, I have relied on the default gae runtimes (standard python, golang, etc...), this makes it fairly simple to deploy new instances while keeping costs down. The provided 

### Requirements

* google app engine enabled
* google app engine api for cloud build
* default cloud build instance has app engine deployer/ app engine admin permissions

Make sure the google app engine api is enabled for your current project.

See more details at my [blog](https://friendlyuser.github.io).


### References

* https://stackoverflow.com/questions/64236468/cloud-build-fails-to-deploy-to-google-app-engine-you-do-not-have-permission-to
* https://cloud.google.com/appengine/docs/standard
