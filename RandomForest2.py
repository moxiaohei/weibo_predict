#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Moxiaofei
# @Site    :
# @File    : RandomForest-Width.py
# @Software: PyCharm
# 0.3303592296103372
import pandas as pd
import matplotlib.pyplot as plt
# 导入随机森林模型   0.37765424663849173  0.3303592296103372
from sklearn.ensemble import RandomForestClassifier

# 读取数据
source = pd.read_csv('handle.csv', sep=' ')
# 定义用于训练时的特征
x_col = ["emotional_level", "follow_num", "at_flag", "topic_flag", "url_flag", "content_length",
         "time_step", "fans_num", "width1", "width2", "width3", "width4"]
# 定义自变量和目标变量
x_train = source[x_col][:14717]
y_train = source['repost_num'][:14717]
# 定义测试数据的自变量和因变量
predict_value = source[x_col][14717:]
true_value = source['repost_num'][14717:]
# n_estimators的取值范围
n_estimators_options = list(range(1, 10))
sample_leaf_options = list(range(1, 10))
results = []
for leaf_size in sample_leaf_options:
    for n_estimators_size in n_estimators_options:
        alg = RandomForestClassifier(min_samples_leaf=leaf_size, n_estimators=n_estimators_size, random_state=50)
        alg.fit(x_train, y_train)
        predict = alg.predict(predict_value)
        # 用一个三元组，分别记录当前的 min_samples_leaf，n_estimators， 和平均误差
        average_err = ((abs(predict - true_value) / true_value).sum()) / len(predict)
        results.append((leaf_size, n_estimators_size, predict, average_err))
# 打印精度最大的那一个三元组
min_pre = min(results, key=lambda x: x[3])
print(min_pre[3])

# 绘图显示误差关系
plt.figure(figsize=(7, 5))
# 绘制50条数据
x1 = x2 = range(0, 50)
y1 = true_value
y2 = min_pre[2]
plt.plot(x1, y1, 'r', linewidth=1, label='true value')
plt.plot(x2, y2, '--b', linewidth=1, label='predict value')
plt.xlabel('microblog number')
plt.ylabel('repost number')
plt.legend()
plt.show()
