#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 18:40
# @Author  : Moxiaofei
# @Site    : 
# @File    : Gaussian-Width.py
# @Software: PyCharm
# 在微博传播广度下 使用朴素贝叶斯算法 预测50条数据误差 0.5729653845486182  这个的预测的结果不是很理想，有点太不准确

# 导入逻辑回归模型
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
source = pd.read_csv('handle.csv', sep=' ')
# 定义用于训练时的特征
x_col = ["emotional_level", "follow_num", "at_flag", "topic_flag", "url_flag", "content_length",
            "time_step", "fans_num", "width1", "width2", "width3", "width4"]
# 定义训练数据的自变量和因变量
x_train = source[x_col][:14717]
y_train = source['repost_num'][:14717]
# 定义测试数据的自变量和因变量
predict_value = source[x_col][14717:]
true_value = source['repost_num'][14717:]
# 构建朴素贝叶斯模型
model = GaussianNB()
# 训练数据集  使用预测值训练真实值
model.fit(x_train, y_train)
# 预测数据集
pre_value = model.predict(predict_value)
# 计算真实值与预测值之间的平均百分比
avg_error = ((abs(pre_value-true_value)/true_value).sum())/len(pre_value)
print(avg_error)

# 绘图显示误差关系
plt.figure(figsize=(7, 5))
# 绘制50条数据
x1 = x2 = range(0, 50)
y1 = true_value
y2 = pre_value
plt.plot(x1, y1, 'r', linewidth=1, label='true value')
plt.plot(x2, y2, '--b', linewidth=1, label='predict value')
plt.xlabel('microblog number')
plt.ylabel('repost number')
plt.legend()
plt.savefig('Gaussian-width-50.png', dpi=400, bbox_inches='tight')
plt.show()
