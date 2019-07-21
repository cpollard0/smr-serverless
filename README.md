# smr-serverless
I loved SpaceMerchant growing up! It was a fun game. 

Now, I work in the AWS space and one of my jobs is to help take applications from monolithic on-prem applications to resilient, cloud applications. 

Converting SMR to a serverless application is a great way to get more experience moving a PHP monolith to AWS and refactoring along the away. 

The current plans are to: 

1. Get everything working in AWS on ec2 and RDS MySql
    This requires a little bit of refactoring in and of itself. 
    Includes adding an ALB in front of the site. 
2. Move images to CloudFront
    First, move images to s3. Then; move them to CloudFront
    CDN = Better performance! 
3. Break out functionallity into an API
    Certain things lend themselves directly to DynamoDB tables; such as sectors. This can improve performance and lower costs