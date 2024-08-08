import sys

class Tee:
    def __init__(self, filename):
        self.file = open(filename, 'a')  # 以追加模式打开文件
        self.stdout = sys.stdout

    def write(self, message):
        self.stdout.write(message)  # 输出到控制台
        self.file.write(message)     # 输出到文件

    def flush(self):
        self.stdout.flush()
        self.file.flush()