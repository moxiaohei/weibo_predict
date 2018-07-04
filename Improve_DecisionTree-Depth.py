#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Moxiaofei
# @Site    : 
# @File    : Improve_DecisionTree-Width.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
# 导入决策树模型
from sklearn.tree import DecisionTreeClassifier

# 通过设置决策树模型中的参数的取值来使用决策树模型，取出最佳的决策树参数和最小的误差
# 在微博转发深度下 改进的决策树 预测50条数据误差 0.2419875256322625
# 读取数据
source = pd.read_csv('depthlast.csv', sep=' ')
# 定义用于训练时的特征
x_col = ["emotional_level", "fans_num", "at_flag", "topic_flag", "url_flag", "content_length", "time_step", 'depth1',
         'depth2']
# 定义自变量和目标变量
x_train = source[x_col][:9737]
y_train = source['depth9'][:9737]
# 定义需要预测的自变量和目标变量
predict_value = source[x_col][9737:]
true_value = source['depth9'][9737:]
# n_estimators的取值范围
max_depth_options = list(range(1, 10))
sample_leaf_options = list(range(1, 10))
results = []
for leaf_size in sample_leaf_options:
    for max_depth_size in max_depth_options:
        alg = DecisionTreeClassifier(min_samples_leaf=leaf_size, max_depth=max_depth_size, random_state=50)
        alg.fit(x_train, y_train)
        predict = alg.predict(predict_value)
        # 用一个三元组，分别记录当前的 min_samples_leaf，n_estimators， 和平均误差
        average_err = ((abs(predict - true_value) / true_value).sum()) / len(predict)
        results.append((leaf_size, max_depth_size, predict, average_err))
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
plt.ylabel('depth')
plt.legend()
plt.savefig('ImDT-depth-50.png', dpi=400, bbox_inches='tight')
plt.show()
