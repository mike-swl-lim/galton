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


# CICD

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