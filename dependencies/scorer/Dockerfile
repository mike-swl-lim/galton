FROM public.ecr.aws/lambda/python:3.8

COPY . /var/task/
RUN python3.8 -m pip install -r requirements.txt
RUN python3.8 -m pip install -e .
RUN python scripts/train.py

COPY lambda_function/scoring_function/ .

CMD ["scoring_function.lambda_handler"]
