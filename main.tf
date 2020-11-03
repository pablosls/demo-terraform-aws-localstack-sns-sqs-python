resource "aws_sns_topic" "user_updates" {
  name = "user-updates-topic"
}

output "arn_sns" {
    value = aws_sns_topic.user_updates.arn
}


resource "aws_sqs_queue" "user_updates_queue" {
  name = "user-updates-queue"
}

output "sqs_queue_url" {
    value = aws_sqs_queue.user_updates_queue.id
}

resource "aws_sns_topic_subscription" "user_updates_sqs_target" {
  topic_arn = aws_sns_topic.user_updates.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.user_updates_queue.arn
}