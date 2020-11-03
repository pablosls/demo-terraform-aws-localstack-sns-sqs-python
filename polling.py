import boto3

sqs = boto3.resource('sqs', endpoint_url="http://localhost:4576")

queue = sqs.get_queue_by_name(QueueName='user-updates-queue')

while 1:
    messages = queue.receive_messages(WaitTimeSeconds=5)
    for message in messages:
        print("Message received: {0}".format(message.body))
        message.delete()