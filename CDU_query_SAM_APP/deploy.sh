aws s3 cp layer.zip s3://cdu-query-lambda-layer
sam package --template-file cdu-query-layer.yaml --s3-bucket cdu-query-lambda-layer --output-template-file cdu-layer-out.yaml
sam deploy  --template-file cdu-layer-out.yaml --stack-name cdu-query-lambda-layer --capabilities CAPABILITY_IAM