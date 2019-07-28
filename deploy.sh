# aws cloudformation deploy --template-file infra.yml --stack-name smr-classic-cmp-test &&
# aws s3 cp ./smr/htdocs s3://images.cmp.smr.cpollard.dev/ --recursive --exclude *.php --exclude *.inc &&
aws cloudformation deploy \
    --template-file api_infrastructure.yml \
    --stack-name smr-classic-cmp-api-test \
    --capabilities CAPABILITY_IAM
