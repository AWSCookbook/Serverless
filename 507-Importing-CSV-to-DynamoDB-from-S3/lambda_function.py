import json
import boto3
import os
import csv
import codecs
import sys

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

bucket = os.environ['bucket']
key = 'sample_data.csv'
tableName = 'AWSCookbook507'

def lambda_handler(event, context):

   try:
       obj = s3.Object(bucket, key).get()['Body']
   except:
       print("Error: S3 error")

   batch_size = 100
   batch = []

   for row in csv.DictReader(codecs.getreader('utf-8')(obj)):
      if len(batch) >= batch_size:
         write_table(batch)
         batch.clear()

      batch.append(row)

   if batch:
      write_table(batch)

   return {
      'statusCode': 200,
      'body': json.dumps('Success: Import complete')
   }


def write_table(rows):
   try:
      table = dynamodb.Table(tableName)
   except:
      print("Error: Table error")

   try:
      with table.batch_writer() as batch:
         for i in range(len(rows)):
            batch.put_item(
               Item=rows[i]
            )
   except:
      print("Error: Import failed")