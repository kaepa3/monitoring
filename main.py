import datetime
from module.s3_server import S3Server
from module.take_video import TakeVideo

if __name__ == '__main__':
    end_date = datetime.datetime.now() + datetime.timedelta(minutes=1)
    s3 = S3Server("s3.toml")
    video = TakeVideo(10)
    # 修理時刻までループ
    cnt = 0
    while (end_date > datetime.datetime.now()):
        file = video.start_recording("{}".format(cnt))
        s3.upload_file(file)
        cnt++

        
        

