#!/usr/local/bin/python3

import boto3

aws_con = boto3.session.Session(profile_name="root")
s3_con = aws_con.resource('s3')

for each in s3_con.buckets.all():
    print(each)

