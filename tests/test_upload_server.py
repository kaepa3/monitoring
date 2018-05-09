# -*- coding: utf-8 -*-
import pytest

from module.upload_server import UploadServer


def test_classinitial():
    obj = UploadServer("tests/test.toml")
    assert obj.config["bucket_name"] == "test_bucket"
    
def test_upload():
    upload_test_file = "conftest.py"
    obj = UploadServer("s3.toml")
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

    