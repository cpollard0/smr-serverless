aws cloudformation deploy --template-file infra.yml --stack-name smr-classic-cmp-test &&
aws cloudformation deploy --template-file api_infrastructure.yml --stack-name smr-classic-cmp-api-test