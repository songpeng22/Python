# -*- coding: utf-8 -*-
# @Time    : 2024/08/16
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py103_random\01_random_tutorial.py
# @Desc    : random模块的tutorial

import random

def ranom_turtorial():
    # random in list or tuple
    print(f"random in list:")
    list1 = [1, 2, 3, 4, 5, 6]
    print(random.choice(list1))
    string = "geeks"
    print(random.choice(string))
    tuple1 = (1, 2, 3, 4, 5)
    print(random.choice(tuple1))
    # sample in list
    print(f"sample in list:")
    list2 = (4, 5, 6, 7, 8)
    print(random.sample(list2,3))
    list3 = "45678"
    print(random.sample(list3,3))

    # shuffle list（洗牌）
    print("\nshuffle list:")
    sample_list = [1, 2, 3, 4, 5]
    print("Original list : ")
    print(sample_list)
    random.shuffle(sample_list)
    print("After the first shuffle : ")
    print(sample_list)
    random.shuffle(sample_list)
    print("After the second shuffle : ")
    print(sample_list)

    # random int value
    print(f"\nrandom number with seed:")
    r1 = random.randint(5, 15)
    print("Random number between 5 and 15 is % s" % (r1))
    r2 = random.randint(-10, -2)
    print("Random number between -10 and -2 is % d" % (r2))

    # random floating-point number between 0 and 1
    print(f"\nrandom floating number between 0 and 1:")
    f1 = random.random()
    print(f"f1:{f1}")

    # seed ensuring reproducibility
    print(f"\nrandom number with seed:")
    random.seed(42)  # 设置种子为42
    print(random.random())  # 输出一个随机数
    random.seed(42)  # 再次设置种子为42
    print(random.random())  # 输出与上次相同的随机数
    random.seed(5)
    print(random.random())
    print(random.random())

if __name__ == "__main__":
    ranom_turtorial()

    