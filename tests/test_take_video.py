import pytest

from module.take_video import TakeVideo


def test_classinitial():
    obj = TakeVideo()
    assert obj.hoge() == 11
    