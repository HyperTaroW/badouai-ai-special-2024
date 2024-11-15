# -*- coding: utf-8 -*-
# time: 2024/11/14 16:14
# file: tf_graph_cpu.py
# author: flame
import tensorflow as tf

""" 使用TensorFlow库进行张量操作和矩阵运算。首先在CPU上创建两个常量张量a和b，并进行元素级乘法操作。然后在会话中运行计算图并输出结果。接着创建两个新的常量张量a1和b1，并进行矩阵乘法操作，最后输出结果。 """
'''
逐元素乘法的要求：matmul
逐元素乘法要求两个张量的形状完全相同。例如，两个 [2, 3] 形状的张量可以进行逐元素乘法。
由于 [2, 3] 和 [3, 2] 的形状不同，无法直接进行逐元素乘法。
矩阵乘法的要求：multiply
矩阵乘法要求第一个矩阵的列数等于第二个矩阵的行数。例如，一个 [2, 3] 形状的矩阵可以与一个 [3, 2] 形状的矩阵相乘，结果是一个 [2, 2] 形状的矩阵。
'''
""" 使用tf.device上下文管理器将计算设备指定为CPU，以优化性能。 """
with tf.device('/cpu:0'):
    """ 创建一个形状为[2, 3]的常量张量a，包含值[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]，并命名为'a'。 """
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')

    """ 创建一个形状为[2, 3]的常量张量b，包含值[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]，并命名为'b'。 """
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='b')

    """ 对张量a和b进行元素级乘法操作，并将结果命名为'mul'。 """
    c = tf.multiply(a, b, name='mul')

    """ 创建一个TensorFlow会话，允许软放置（自动选择设备）并记录设备放置日志。 """
    sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))

    """ 在会话中运行计算图，获取张量c的结果，并将其存储在变量result中。 """
    result = sess.run(c)

    """ 打印计算结果。 """
    print(result)

    """ 关闭会话，释放资源。 """
    sess.close()

""" 创建一个形状为[2, 3]的常量张量a1，包含值[[1, 2, 3], [4, 5, 6]]。 """
a1 = tf.constant([[1, 2, 3], [4, 5, 6]])  # 形状为 [2, 3]

""" 创建一个形状为[3, 2]的常量张量b1，包含值[[7, 8], [9, 10], [11, 12]]。 """
b1 = tf.constant([[7, 8], [9, 10], [11, 12]])  # 形状为 [3, 2]

""" 对张量a1和b1进行矩阵乘法操作，并将结果存储在变量result1中。 """
result1 = tf.matmul(a1, b1)  # 矩阵乘法

""" 打印矩阵乘法的结果。 """
print(result1)
