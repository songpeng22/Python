# -*- coding: utf-8 -*-
# @Time    : 2024/08/12
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py305_tensorflow\01_convolution.py
# @Desc    : tensorflow卷积

import tensorflow as tf

# 定义输入图像（1个通道）
image = tf.constant([[1, 2, 3, 0],
                     [0, 1, 2, 1],
                     [1, 0, 1, 2],
                     [0, 1, 0, 1]], dtype=tf.float32)

image = tf.expand_dims(image, axis=-1)  # 增加通道维度
image = tf.expand_dims(image, axis=0)   # 增加批次维度

# 定义卷积核（2x2，1个输入通道，1个输出通道）
kernel = tf.constant([[1, 0],
                      [0, -1]], dtype=tf.float32)

kernel = tf.expand_dims(kernel, axis=-1)  # 增加输入通道维度
kernel = tf.expand_dims(kernel, axis=-1)  # 增加输出通道维度

# 使用 tf.nn.conv2d 进行卷积
output = tf.nn.conv2d(image, kernel, strides=[1, 1, 1, 1], padding='VALID')

print(tf.squeeze(output).numpy())  # 去掉多余的维度