import pytest
from module.upload_server import UploadServer


def test_add():
    assert UploadServer().hoge() == 11