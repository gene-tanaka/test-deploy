# Cognite function template
This repository can be used as a template to use Cognite Functions with a CI/CD pipeline leveraging GitHub actions. This repository uses a GitHub action from github.com/andeplane/deploy-function-python which gives you
 - Unit tests on the functions
 - Integration tests on deployed functions
 - Deployed functions for each pull request that integration tests are being performed on
 - A function deployed with latest master.

This is currently a work in progress, but works like a proof of concept on how a CI/CD pipeline can be built with GitHub actions on top of Cognite Functions.