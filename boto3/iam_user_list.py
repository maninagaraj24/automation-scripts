#!/usr/local/bin/python3

import boto3

aws_con = boto3.session.Session(profile_name="root")
iam_con = aws_con.resource('iam')

for each in iam_con.users.all():
    print(each)

