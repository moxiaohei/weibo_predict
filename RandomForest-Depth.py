#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Moxiaofei
# @Site    : 
# @File    : RandomForest-Width.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
# 导入随机森林模型   0.37765424663849173
from sklearn.ensemble import RandomForestClassifier
# 在微博转发深度下 随机森林 预测50条数据误差  0.22297886762360442
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
n_estimators_options = list(range(1, 10))
# 存储列表
result = []
for n_estimators_size in n_estimators_options:
    rfc = RandomForestClassifier(n_estimators=n_estimators_size)  # 构建随机森林
    # 使用的是depth9=9737之前的数据和9737之后的数据进行训练
    rfc.fit(source[x_col][:9737], source['depth9'][:9737])
    # 预测depth9=9737之后的数据走向
    predict = rfc.predict(source[x_col][9737:])
    #  计算平均绝对百分比误差 (使用预测值和真实值预测误差)
    a = ((abs(predict-true_value)/true_value).sum())/len(predict)
    # 将训练模型参数取值，预测值，误差以三元组的形式存入列表中
    result.append((n_estimators_size, predict, a))
# result的形式为：
#       0                       1                   2
# n_estimators_size     array数组类型的预测值       误差值
#  取出result列表中误差最小的一组预测值(取出的就是a的最小值)
min_predict = min(result, key=lambda x: x[2])
print(min_predict[2])
#  取出误差最小的一组预测值（即取出array,然后拿来与真实值进行对比）
pre_value = min_predict[1]

# 绘图显示误差关系
plt.figure(figsize=(7, 5))
# 绘制50条数据
x1 = x2 = range(0, 50)
y1 = true_value
y2 = pre_value
plt.plot(x1, y1, 'r', linewidth=1, label='true value')
plt.plot(x2, y2, '--b', linewidth=1, label='predict value')
plt.xlabel('microblog number')
plt.ylabel('depth')
plt.legend()
plt.savefig('RF-depth-50.png', dpi=400, bbox_inches='tight')
plt.show()
