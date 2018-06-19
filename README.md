# Google Cloud Pub/Sub

## インストールと環境変数
```console
$ sudo pip3 install google-cloud-pubsub
```
IAMの追加(Cloud Pub/Subの権限はIAMで担保されている)
```console
$ gcloud iam service-accounts create ${NAME}
```
サービスアカウントに権限を付与
```console
$ gcloud projects add-iam-policy-binding ${PROJECT_ID} --member "serviceAccount:${NAME}@${PROJECT_ID}.iam.gserviceaccount.com" --role "roles/owner"
```
キーファイルの作成
```cosnole
$ gcloud iam service-accounts keys create ${FILE_NAME}.json --iam-account ${NAME}@${PROJECT_ID}.iam.gserviceaccount.com
```
クレデンシャルをパスに追加
```console
$ export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
```

## Topicの作成
<div align="center">
  <img width="500px" src="https://www.dropbox.com/s/v898liwfcbj8fbk/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202018-06-20%2004.40.32.png">
</div>

## Subscriptioを作成
Subscriptionを作成
```python
from google.cloud import pubsub_v1

GCP_PROJECT = os.environ['GCP_PROJECT']

subscriber = pubsub_v1.SubscriberClient()
topic_name = 'my-new-topic'
topic = f'projects/{GCP_PROJECT}/topics/{topic_name}'

sub_name = 'my-new-subscription'
subscription_name = f'projects/{GCP_PROJECT}/subscriptions/{sub_name}'

subscriber.create_subscription(subscription_name, topic)
```

## Publisherを設定
特に設定の必要なし

## Subscriberのメッセージの待受
コールバックで待ち受けて実行なので、サーバのようなものが必要となる  
```python
subscriber = pubsub_v1.SubscriberClient()
  
sub_name = 'my-new-subscription'
subscription_name = f'projects/{GCP_PROJECT}/subscriptions/{sub_name}'
  
def callback(message):
  ''' 受け取ったメッセージに応じてなにかする '''
  print(message.data)
  message.ack()
future = subscriber.subscribe(subscription_name, callback)
  
# ここでブロックが行われてコールバックで受け取るメッセージが展開される
future.result()
```
