#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 18:55
# @Author  : Moxiaofei
# @Site    : 
# @File    : DecisionTree-Width.py
# @Software: PyCharm

# 在微博转发深度下 使用决策树算法 预测50条数据误差  0.3598165869218501

import pandas as pd
import matplotlib.pyplot as plt
# 导入决策树模型
from sklearn.tree import DecisionTreeClassifier

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
# 构建决策树模型
model = DecisionTreeClassifier()
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
plt.savefig('DT-depth-50.png', dpi=400, bbox_inches='tight')
plt.show()
