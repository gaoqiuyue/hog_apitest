import requests

class TestApi():
    def test_print(self):
        print("test")
    def test_one(self):
        print("test2")
    def validate(self,key,value):
        assert key==value
        #循环调用
        return self
    def test_get(self):
        requests.get("http://www.baidu.com").validate()