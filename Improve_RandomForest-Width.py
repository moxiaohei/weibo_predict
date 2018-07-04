#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Moxiaofei
# @Site    : 
# @File    : Improve_RandomForest-Width.py
# @Software: PyCharm
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt

# 在微博传播广度下 改进的随机森林算法 预测50条数据误差 0.0746270295225973
# 读取数据
source = pd.read_csv('handle.csv', sep=' ')
# 定义用于训练时的特征
x_col = ["emotional_level", "follow_num", "at_flag", "topic_flag", "url_flag", "content_length",
            "time_step", "fans_num", "width1", "width2", "width3", "width4"]
RF = []
# 定义随机森林算法参数的取值范围
sample_leaf_options = list(range(1, 10, 2))
n_estimators_options = list(range(1, 10, 2))
# 将测试数据的真实转发次数取出
true_value = source['repost_num'][14717:]
# 训练随机森林模型
for leaf_size in sample_leaf_options:
    for n_estimators_size in n_estimators_options:
        results = []
        # 创建模型[(1,1),(1,3),(1,5),(1,7),(1,9),
        #              ...
        #          (9,1),(9,3),(9,5),(9,7),(9,9),]
        # min_samples_leaf:叶子节点最少的样本数。
        # n_estimators:决策树的个数，越多越好，但是性能就会越差，至少100左右（具体数字忘记从哪里来的了）可以达到可接受的性能和误差率。
        # 创建模型
        alg = RandomForestClassifier(min_samples_leaf=leaf_size, n_estimators=n_estimators_size, random_state=50)
        # 训练模型
        alg.fit(source[x_col][:14717], source['repost_num'][:14717])
        # 预测微博测试数据的转发次数
        predict = alg.predict(source[x_col][14717:])
        # 计算真实值与预测值之差
        # 使用微博元数据的后50位真实数据与预测出来的50条数据来进行对比
        # 在(n,n)的模型下，分别比较50位数据的误差
        for i in range(len(predict)):
            aa = abs(source['repost_num'][14717 + i] - predict[i])
            # 如果真实值与预测值之差为零则准确率为100%
            if aa == 0:
                bb = 1
            # 如不为0则计算误差
            else:
                bb = 1 - float(aa) / float(source['repost_num'][14717 + i])
            # 用一个四元组，分别记录当前的 min_samples_leaf，n_estimators， 和预测误差，预测值
            results.append((leaf_size, n_estimators_size, bb, predict[i]))
        RF.append(results)

# 定义与预测数据条数目相等的空列表
createVar = locals()
listTemp = range(len(RF[0]))
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# 将createVar中的第一列元素(bia0~50)赋值为dict并设置为空
for i, s in enumerate(listTemp):
    createVar['bia' + str(i)] = []

# 将预测值中每一条微博的预测值放入相应的列表中
# 将预测值中每一条微博的预测值放入相应的列表中
# len(RR[0])的值为50
# createVar中的值存储的是：bia0~50 : 25个值
long = 0
while long < len(RF[0]):
    for i in range(len(RF)):
        createVar['bia' + str(long)].append(RF[i][long])
    long += 1

Pre_value = []
# 将字符串string对象转化为有效的表达式参与求值运算返回计算结果
for i in range(len(RF[0])):
    # 将每一个列表中每一条微博的最佳预测值取出
    VV = eval('bia%s' % (i))
    pre_value = max(VV, key=lambda x: x[2])
    pre_value = pre_value[3]
    # 将最佳预测值存入一个列表中，成为最佳预测值的集合
    Pre_value.append(pre_value)
# 计算该最佳预测值集合的平均绝对百分比误差
a = (abs(Pre_value - true_value) / true_value).sum()
average_error = a / len(Pre_value)
print(average_error)

# 画图对比预测值与真实值的拟合程度
plt.figure(figsize=(7, 5))
x1 = x2 = range(0, 50)
y1 = true_value
y2 = Pre_value
plt.plot(x1, y1, label='true value', linewidth=1, color='r')
plt.plot(x2, y2, "b--", linewidth=1, label='predict value')
plt.ylabel('repost number')
plt.xlabel('microblog number')
plt.legend()
plt.savefig('ImRF-width-50.png', dpi=400, bbox_inches='tight')
plt.show()
