
from google.cloud import pubsub_v1
from concurrent.futures import ProcessPoolExecutor as PPE
from datetime import datetime

def pubr(arg):
  # Instantiates a client
  try:
    print('call at ')
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('dena-ai-training-16-gcp', 'my-new-topic')
    publisher.publish(topic_path, bytes(f'My first message!' + datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 'utf8'), spam='eggs')
  except Exception as ex:
    print(ex)

def pub():
  with PPE(max_workers=16) as exe:
    exe.map(pubr, list(range(1000)))

pub()
