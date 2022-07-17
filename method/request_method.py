
import requests


class HttpClient:
    # 只要用到这个类就会进入到init这个函数里面去(开启会话
    def __init__(self):
        self.session = requests.session()

    # 封装请求
    # 地址
    # 参数
    # 测试登录 请求post 地址login 参数 admin password 数据类型json
    def send_request(self, method, url, param_type, data=None, **kwargs):
        # 请求方式大写
        method = method.upper()
        # 请求参数大写
        param_type = param_type.upper()
        # 判断get post
        if 'GET' == method:
            # 通过session会话发送请求
            response = self.session.request(method=method, url=url, params=data, **kwargs)
        elif 'POST' == method:
            # 判断提交类型 json data
            if 'FROM' == param_type:
                response = self.session.request(method=method, url=url, params=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif 'DELETE' == method:
            if 'FROM' == param_type:
                response = self.session.request(method=method, url=url, params=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif 'PUT' == method:
            if 'FROM' == param_type:
                response = self.session.request(method=method, url=url, params=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        else:
            raise ValueError
        #
        return response

    # 关闭会话
    def close_session(self):
        self.session.close()
