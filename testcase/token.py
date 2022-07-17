import json


import pytest
import requests
from common.yaml_util import read_yaml1, read_yaml2


class TestApi:
    access_token = "None"

    @pytest.mark.parametrize("caseinfo",read_yaml1())
    def test_01_get_token(self,caseinfo):
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url']
        headers = caseinfo['headers']
        params = caseinfo['params']
        validate = caseinfo['validate']
        res = requests.get(url=url,params=params)
        result = res.json()
        if "access_token" in json.dumps(result):
            TestApi.access_token = result['access_token']
            print(result)

    @pytest.mark.parametrize("caseinfo", read_yaml2())
    def test_02_tjhys(self, caseinfo):
        name = caseinfo['name']
        method = caseinfo['method']
        url = caseinfo['url'] + TestApi.access_token
        headers = caseinfo['headers']
        json = caseinfo['json']
        validate = caseinfo['validate']
        res = requests.post(url=url, json=json)
        print(res.json())


if __name__ == '__main__':
    pytest.main()

