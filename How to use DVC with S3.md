## Introduction

The steps below are necessary to use DVC with a S3 bucket.

### Requirements

You need to install the s3 library for DVC
    pip install dvc[s3]

### Setup

1. Set the remote pointing to the bucket you want to use

    dvc remote add -d wasabi s3://test-bucket-dvc

2. Set the access key

    dvc remote modify wasabi access_key_id  XXXXXX

3. Set the secret key

dvc remote modify wasabi secret_access_key XXXXXX

4. Set the endpoint

dvc remote modify wasabi endpointurl https://XXXXXX

#### Checks

You can check the remote has been created

    dvc remote list

#### Pushing data

If you run the push command, you should see the data saved in the bucket

    dvc push