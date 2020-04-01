# Json Validator to run on AWS Lambda

## Overview
This is a test script to test [json schema](https://openid.net/schemas/verified_claims_request-09.json) of [OpenID eKYC-IDA](https://openid.net/specs/openid-connect-4-identity-assurance-1_0-09.html) `verified_claims` requests.
It creates package zip file to be uploaded to AWS Lambda and run.

## How to use

### Docker way

- build docker image to build AWS package (using [LambCI](https://hub.docker.com/r/lambci/lambda/) )
  - `docker build -t json_validator .`
- run docker image to locally install `jsonschema`
  - `docker run -v "$PWD":/var/task json_validator`
- now you have `deploy_package.zip` which you can upload to AWS Lambda and run.
- OR, run (another) docker image to run the validation script locally
  - `docker run -v "$PWD":/var/task lambci/lambda:python3.6 lambda_function.lambda_handler`
  
### Simply running jsonschema on terminal

 `pip install jsonschema`
 
 `jsonschema -i eKYC-IDA-5.1.c_too_short.json verified_claims_request-09.json`
 
 `jsonschema -i eKYC-IDA-5.1.c_too_long.json verified_claims_request-09.json`
 
 `jsonschema -i eKYC-IDA-5.1.c_wrong_essencial_type.json verified_claims_request-09.json`
  