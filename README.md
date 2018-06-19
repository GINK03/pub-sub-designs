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
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
```

## Subscriberを設定

## Publisherを設定

## Subscriberのメッセージの待受
