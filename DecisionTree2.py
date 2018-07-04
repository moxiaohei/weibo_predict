#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 18:55
# @Author  : Moxiaofei
# @Site    : 
# @File    : DecisionTree-Width.py
# @Software: PyCharm

# 使用决策树算法  0.46645755375076475
# 此方法采用GridSearchCV网格搜索自动调参的方式来进行最佳参数的获取，虽然可以通过该方法获取到最佳参数并提升了一点点性能，
# 但是时间消耗太大，占用内存太多，如若可以，不使用该方法。
'''
{'max_depth': 5, 'min_samples_leaf': 1, 'min_samples_split': 2}
0.422742249194142 0.3972626199669239
'''
''''
{'max_depth': 4, 'min_samples_leaf': 9, 'min_samples_split': 5}
0.7306271102311661 0.3995362345573362
'''


import pandas as pd
import matplotlib.pyplot as plt
# 导入决策树模型
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
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

decision_tree_classifier = DecisionTreeClassifier(max_features='sqrt')
parameter_grid = {'max_depth': list(range(1, 10)),
                  'min_samples_split': list(range(2, 10)),
                  'min_samples_leaf': list(range(1, 10))}

gridsearch = GridSearchCV(decision_tree_classifier, param_grid=parameter_grid,  cv=5)
gridsearch.fit(x_train, y_train)
# 得分最高的参数值，并构建最佳的决策树
best_param = gridsearch.best_params_
print(best_param)
best_decision_tree_classifier = DecisionTreeClassifier(max_depth=best_param['max_depth'],
                                                       min_samples_split=best_param['min_samples_split'],
                                                       min_samples_leaf=best_param['min_samples_leaf'])
# 训练数据集  使用预测值训练真实值
decision_tree_classifier.fit(x_train, y_train)
best_decision_tree_classifier.fit(x_train, y_train)
# 预测数据集
pre_value = decision_tree_classifier.predict(predict_value)
best_pre_value = best_decision_tree_classifier.predict(predict_value)
# 计算真实值与预测值之间的平均百分比
avg_error = ((abs(pre_value-true_value)/true_value).sum())/len(pre_value)
best_avg_error = ((abs(best_pre_value-true_value)/true_value).sum())/len(best_pre_value)

print(avg_error, best_avg_error)

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
plt.show()

plt.figure(figsize=(7, 5))
# 绘制50条数据
x1 = x2 = range(0, 50)
y1 = true_value
y2 = best_pre_value
plt.plot(x1, y1, 'r', linewidth=1, label='true value')
plt.plot(x2, y2, '--b', linewidth=1, label='predict value')
plt.xlabel('microblog number')
plt.ylabel('repost number')
plt.legend()
plt.show()
