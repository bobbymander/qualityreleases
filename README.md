# qualityreleases

## Intro

This final project in the Udacity Azure court involves creating a pipeline for an App Service with a full testing CICD process.  Testing includes Postman, JMeter, and Selenium.

## Contents

- automatedtesting/:  All testing scripts and configuration
- screenhots/:  All evidence of pipeline results and output
- terraform/:  All configuration for creating the App Service and associated components
- azure-pipelines:  The pipeline YAML used by Azure

## Notes

- Running pipelines requires extensive iteration.  For this project, I iterated the pipeline over 200 times which does take time.
- There is a learning curve to all testing tools with Selenium being the hardest, followed by JMeter, and then Postman.
- Terraform is tricky and locks can be a problem if pipelines fail.  Luckily Azure has tools to clear those locks using the Portal.
- Azure DevOps and Azure Portal are very powerful UIs with so many features, the problem is finding them.
