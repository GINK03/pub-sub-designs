# Imports the Google Cloud client library
import os
from google.cloud import pubsub_v1

GCP_PROJECT = os.environ['GCP_PROJECT']
def sub():
  subscriber = pubsub_v1.SubscriberClient()
  topic_name = 'my-new-topic'
  topic = f'projects/{GCP_PROJECT}/topics/{topic_name}'
  print(topic)
  
  sub_name = 'my-new-subscription'
  subscription_name = f'projects/{GCP_PROJECT}/subscriptions/{sub_name}'
  
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
