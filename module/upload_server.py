import boto3

class UploadServer(object):
    def __init__(self, *args):
        super(UploadServer, self).__init__(*args)
        self.bucket_name = "my-bucket-name"
        self.s3 = boto3.resource('s3')
 

    def upload_file(self, file_name):
        self.s3.Bucket(self.bucket_name).upload_file(file_name, file_name)
        

    def hoge(self):
        return 11