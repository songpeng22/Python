class CallableClass:
    def __call__(self, data: dict) -> dict:
        # 对传入的字典进行处理，例如添加一个新的键值对
        data['key3'] = 'value3'
        return data

# 创建一个类的实例
callable_instance = CallableClass()

# 调用实例，就像调用函数一样
input_data = {'key1': 'value1', 'key2': 'value2'}
output_data = callable_instance(input_data)

print(output_data)
# 输出结果将会是：{'key1': 'value1', 'key2': 'value2', 'new_key': 'new_value'}

