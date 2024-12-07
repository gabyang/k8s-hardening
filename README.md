# k8s-hardening
This project will be based on the application for code assessment and is inspired by [this blog](https://www.hairizuan.com/building-a-code-assessment-tool-but-in-kubernetes/). The original application is written in Go but staying true to my one and only, the cure to my soul, I shall be using Python to build the code assessment application.

## Local Setup

Build the docker image from the Dockerfile and push it to your own registry.
```
docker build -t myregistry/code-assessment-tool:latest .
docker push myregistry/code-assessment-tool:latest
```
