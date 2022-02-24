# galton

Sir Francis Galton was an English Victorian polymath, and the grand daddy of "regression towards the mean".

It is in his honour that this challenge has been completed.


# Architecture

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