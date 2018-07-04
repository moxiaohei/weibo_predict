#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 18:30
# @Author  : Moxiaofei
# @Site    : 
# @File    : KNN-Width.py
# @Software: PyCharm
# 使用的无关变量越多，预测的结果越不准确  这里取了情感值和粉丝数以及一个小时的转发量来作为预测的特征值
# 在微博传播广度下 使用K临近算法 预测50条数据误差 0.36835476514779714

import pandas as pd
import matplotlib.pyplot as plt
# 导入KNN模型
from sklearn.neighbors import KNeighborsClassifier

# 读取数据
source = pd.read_csv('handle.csv', sep=' ')
# 定义用于训练时的特征
x_col = ["emotional_level", "follow_num", "at_flag", "topic_flag", "url_flag", "content_length",
            "time_step", "fans_num", "width1", "width2", "width3", "width4"]
# 定义自变量和目标变量
x_train = source[x_col][:14717]
y_train = source['repost_num'][:14717]
# 定义需要预测的自变量和目标变量
predict_value = source[x_col][14717:]
true_value = source['repost_num'][14717:]
# 建立模型
model = KNeighborsClassifier()
# 训练模型
model.fit(x_train, y_train)
# 预测测试数据
pre_value = model.predict(predict_value)
# 计算平均绝对百分比误差
avg_error = ((abs(pre_value-true_value)/true_value).sum())/len(pre_value)
print(avg_error)
# 画图展示预测值与真实值之间的关系
plt.figure(figsize=(7, 5))
x1 = x2 = range(0, 50)
y1 = true_value
y2 = pre_value
plt.plot(x1, y1, 'r', label='true value', linewidth=1)
plt.plot(x2, y2, '--b', label='predict value', linewidth=1)
plt.xlabel('microblog number')
plt.ylabel('repost number')
plt.legend()
plt.savefig('KNN-width-50.png', dpi=400, bbox_inches='tight')
# plt.show()
