# galton

Sir Francis Galton was an English Victorian polymath, and the grand daddy of "regression towards the mean".

It is in his honour that this challenge has been completed.

# Model 
The algorithm here is a simple linear regression that has been optimised using gradient descent.

Note the gradient descent implemented here is not technically "stochastic" as a shuffled sub sample of the dataset is not being used to update weights.
```
iterations = 2000
learning_rate = 0.002
```
## Performance

![image](https://user-images.githubusercontent.com/29474816/155529999-6362034a-ff17-4f64-9d4a-20299dc542a1.png)

# Architecture
* A pretty simple architecture
* Dont need training in cloud for this use case as model is super small and simple, did not feel the need to upload artifact to object storage
* Model is saved as part of container that is then pushed for lambda to use
* ApiGateway makes it super simple to configure load balance and rate limited based on throughput and traffic

![Untitled Diagram drawio](https://user-images.githubusercontent.com/29474816/155542063-fbede8aa-6968-41f7-8ef7-5e3b844cd54f.png)


# CICD
* Uses github actions (yay free tier)
* Broad flow is setup, test, lint, deploy to AWS

# Deployment
```
make deploy-image-repo && \
make build && \
make push-scorer-image && \
make deploy-cf
```

# Flask Web Api Implementation
This has only been implemented in local mode due to time constraints
```
flask run
```
## Batch Invocation
```
curl --location --request POST 'http://127.0.0.1:5000/batch' \
--header 'payload: 100' \
--header 'Content-Type: application/json' \
--data-raw '{
    "payload": [10, 20 ,30]
}'
```
## Stream 
```
curl --location --request POST 'http://127.0.0.1:5000/stream' \
--header 'payload: 100' \
--header 'Content-Type: application/json' \
--data-raw '{
    "payload": 100
}'
```

# Deployed Scoring API

## Endpoint
```
https://8nu7ujeqq6.execute-api.ap-southeast-2.amazonaws.com/score/
```
## Example
```
curl --location --request POST 'https://8nu7ujeqq6.execute-api.ap-southeast-2.amazonaws.com/score/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "payload": [10,20]
}'
```
The above should return:
```
{"predictions": [9530.899058493378, 18908.879046675287]}
```
# Enterprise machine learning system
* Feature Store - to access your engineered features that come from processing your source data
    * batch
    * "online"
* Training  - a module that provides an interface to easily train models via the cloud
    * should support wide variety of ML libraries and tooling
* Model manager - a module that provides utilities to manage collections of models that have been trained
* Automated inference - a pipeline that provides for the automated deployment of both batch and online scoring use cases with minimal boilerplate
* Configuration  - at scale, having a separate module to compare and build configuration with their own versioning is well worth the effort to ensure configs are transparent and easily accessible

# Checklist
- [x] Take the code and upload to git repo
- [x] Provide high level overview of systems designs
- [x] Create simple linear regression model
- [x] Update main.py to create invokable http api (renamed to app.py)
- [x] Package your code into a library
- [x] Package your code into a container and deploy to container registry
- [x] Create a CICD pipeline using the technology of your choice to deploy your code to production
- [x] Document what components an enterprise machine learning system should have

# If I had time
* Implement cloudformation for ApiGateway properly instead of going the quick and dirty console method
* Implement security for this Api
    * JWT
    * Authentication Key
    * Key & Secret Rotation
    * Encryption 
* Unit tests for every function for 100% coverage
* Run tests via container in pipeline
* Deploy package to some sort of artifcat repository and pull from there
* Monitoring has not been considered for this implementation, but I would default to something simple like Amazon CloudWatch. If I'm running big clusters and lots of machines something like Grafana would be ideal.