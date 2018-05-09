# -*- coding: utf-8 -*-
import boto3
import toml

class S3Server(object):
    def __init__(self, name, *args):
        super(S3Server, self).__init__(*args)
        self.config = toml.load(open(name))
        self.s3 = boto3.client('s3')
        
    def upload_file(self, file_name):
        self.s3.upload_file(file_name, self.config["bucket_name"], file_name)

    def list_file(self):
        name = self.config["bucket_name"]
        return self.s3.list_objects(Bucket=name).get("Contents")


    def delete_file(self, file_name):
        self.s3.delete_object(Bucket=self.config["bucket_name"], Key=file_name)