# 下面是错误类型
PARAM_INVALID = 1  # 参数错误
SESSION_INVALID = 2  # 登录状态错误


class ApiException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
