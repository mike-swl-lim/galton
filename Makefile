deploy-image-repo:
	aws cloudformation deploy --template-file ./cloudformation/galton-scorer-image.cf.yaml --stack-name galton-scorer-image-dev --no-fail-on-empty-changeset

build:
	docker build -t scoring_container_image \
	-f ./dependencies/scorer/Dockerfile .

push-scorer-image:
	aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 744607448056.dkr.ecr.ap-southeast-2.amazonaws.com/scoring_container_image
	docker tag scoring_container_image 744607448056.dkr.ecr.ap-southeast-2.amazonaws.com/scoring_container_image:latest 
	docker push 744607448056.dkr.ecr.ap-southeast-2.amazonaws.com/scoring_container_image


deploy-cf:
	aws cloudformation deploy --template-file ./cloudformation/galton.cf.yaml --stack-name galton-dev --capabilities CAPABILITY_NAMED_IAM --no-fail-on-empty-changeset

run-local: # not working
	sam local invoke -t ./cloudformation/galton.cf.yaml \
		--event ./tests/data/test_lambda_single_event.json 