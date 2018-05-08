import pytest

from module.upload_server import UploadServer

def test_classinitial():
    name = "sv_name"
    obj = UploadServer(name)
    assert obj.bucket_name == name
    