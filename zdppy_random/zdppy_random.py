import string
import time

from zdppy_log import Log
import random
import uuid


class Random:
    def __init__(self,
                 log_file_path: str = "logs/zdppy/zdppy_random.log",
                 debug: bool = False,
                 ):
        # 日志
        self.__log_file_path = log_file_path
        self.log = Log(log_file_path=log_file_path, debug=debug)

    def random_str(self, n: int = 16):
        """
        生成随机的字符串，相关知识点：
            random.sample(str, num)：从str字符串中随机选取num个字符
            string.ascii_letters：返回26个英文字母的大小写字符串
            string.digits：返回阿拉伯数字的字符串
        :return:
        """
        total_str = ""

        # 使用uuid4()函数生成的UUID是使用真正的Random或Pseudo-Random生成器创建的。
        uuid_str = str(uuid.uuid4()).replace("-", "")

        # 尝试取uuid
        total_str += uuid_str
        if len(total_str) > n:
            return total_str[:n]

        # 根字符串
        root_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

        # 当前时间
        time_str = str(time.time())

        # 尝试去uuid+当前时间
        total_str += time_str
        if len(total_str) > n:
            return total_str[:n]

        # 尝试去uuid+当前时间+随机字符串
        total_str += root_str
        if len(total_str) > n:
            temp_s = random.sample(root_str, n - len(uuid_str) - len(time_str))
            temp_s = "".join(temp_s)
            return f"{uuid_str}{time_str}{temp_s}"

        # 如果还不够
        temp_length = n - len(total_str)
        temp_s = random.sample(root_str, temp_length)
        temp_s = "".join(temp_s)
        return f"{total_str}{temp_s}"
