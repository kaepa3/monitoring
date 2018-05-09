# -*- coding: utf-8 -*-
import pytest

from module.s3_server import S3Server


def test_classinitial():
    obj = S3Server("tests/test.toml")
    assert obj.config["bucket_name"] == "test_bucket"
    
def test_upload():
    upload_test_file = "conftest.py"
    obj = S3Server("s3.toml")
    # 追加確認
    obj.upload_file(upload_test_file)
    list = obj.list_file()
    flg = False
    if list:
        for v in list:
            if upload_test_file == v.get("Key"):
                flg = True

    assert flg == True
    # 削除確認
    obj.delete_file(upload_test_file)

    