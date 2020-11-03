import boto3

# Create an SNS client
sns = boto3.client('sns', endpoint_url="http://localhost:4575")


# Publish a simple message to the specified SNS topic
response = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:000000000000:user-updates-topic',    
    Message='Hello World! fdsfsdfsfsdfsdf'     
)

# Print out the response
print(response)
  
