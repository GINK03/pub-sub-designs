# Imports the Google Cloud client library
from google.cloud import pubsub_v1

def sub():
  subscriber = pubsub_v1.SubscriberClient()
  topic_name = 'my-new-topic'
  topic = f'projects/dena-ai-training-16-gcp/topics/{topic_name}'
  print(topic)
  
  sub_name = 'my-new-subscription'
  subscription_name = f'projects/dena-ai-training-16-gcp/subscriptions/{sub_name}'
  
  try:
    subscriber.create_subscription(subscription_name, topic)
  except Exception as ex:
    ...

  def callback(message):
     ''' 受け取ったメッセージに応じてなにかする '''
     print(message.data)
     message.ack()
  future = subscriber.subscribe(subscription_name, callback)
  
  # ここでブロックが行われてコールバックで受け取るメッセージが展開されるらしい
  future.result()

sub()
