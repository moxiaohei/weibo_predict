#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 0:04
# @Author  : Moxiaofei
# @Site    : 
# @File    : draw.py
# @Software: PyCharm
# 微博传播时间序列峰值预测研究
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

''''''''''''''''''''''''''''''''''''''''''''
                 # 广度
''''''''''''''''''''''''''''''''''''''''''''

train = pd.read_csv("handle.csv", sep=' ')
# # 将特征和类型分开
# x_col = [x for x in train.columns if x != 'repost_num']
#
# X = train[x_col]
# Y = train['repost_num']
#
# # ------用户粉丝数与转发数的关系散点图  width------  #
# plt.figure(figsize=(7, 5))
# fans_num = train['fans_num']
# repost_num = train['repost_num']
# plt.scatter(fans_num, repost_num)
# plt.title('The relationship between fans_num and repost_num')
# plt.xlabel('the number of the fans')
# plt.ylabel('the number of the repost')
# plt.savefig('repost_fans.png', dpi=400, bbox_inches='tight')
# # plt.show()
#
# # 峰值  重要！！！！ 我需要根据时间和转发次数来进行峰值的监测
# # 但是这里给出的数据都是每隔15分钟采取的总的转发次数
# # 所谓的峰值对于我而言(不想重新做数据的话)是需要知道在
# # 某个时刻点转发的次数最多，需要计算时刻点(15分钟)之间的差值
# # 来获取峰值。
# # 可以利用差值来确定某个时间段是否出现峰值
#
# # ------重要！ 计算在某个时间段内转发次数最多的,绘制成图显示峰值------  #
# res = []
# # # i的取值为[1,11]
# for i in range(1, 12):
#     res.append(train['width'+str(i+1)] - train['width'+str(i)])
# time_repost_num = []
# MAX_TIME_DICT = []
# for j in range(0, 14767):
#     # [32, 85, 1, 267, 95, 74, 18, 8, 103, 33, 17]  所有的差值
#     line = [x[j] for x in res]
#     # print(line)
#     # 最大值所出现的时刻
#     max_sub_time = line.index(max(line)) + int(1)
#     MAX_TIME_DICT.append(max_sub_time)
#     # 在差值里面统计时刻和最大差值
# time_count = []
# for i in range(1, 12):
#     # 输出出现最大差值的时刻的数量
#     time_count.append(MAX_TIME_DICT.count(i))
# plt.figure(figsize=(7, 5))
# time = range(1, 12)
# plt.plot(time, time_count)
# plt.title('The relationship between time and D-value')
# plt.xlabel('the number of the time')
# plt.ylabel('the number of the D-value')
# # plt.savefig('top.png', dpi=400, bbox_inches='tight')
# plt.show()
#
# # 可以比对转发总数和各个时间点之间的关系，来确定是否有峰值的出现
#
# # 峰值 微博转发次数随着时间变化的曲线   未完成
# # ------峰值 微博转发次数随着时间变化的曲线------  #
# # 随机取出前5条数据绘制转发数与时间（3小时）之间的折线图
# widths = []
# for i in range(1, 13):
#     widths.append('width'+str(i))
# data = train[widths]
# x1 = range(0, 12)
# y1 = data.iloc[0]
# y2 = data.iloc[1]
# y3 = data.iloc[2]
# y4 = data.iloc[3]
# y5 = data.iloc[4]
# y6 = data.iloc[5]
# y7 = data.iloc[6]
# y8 = data.iloc[7]
# y9 = data.iloc[8]
# y10 = data.iloc[9]
# plt.figure(figsize=(7, 5))
# plt.plot(x1, y1, '--b', linewidth=1, marker='o', markerfacecolor='blue', markersize=3, label='one')
# plt.plot(x1, y2, '--r', linewidth=1, marker='o', markerfacecolor='red', markersize=3, label='two')
# plt.plot(x1, y3, '--c', linewidth=1, marker='o', markerfacecolor='cyan', markersize=3, label='three')
# plt.plot(x1, y4, '--g', linewidth=1, marker='o', markerfacecolor='green', markersize=3, label='four')
# plt.plot(x1, y5, '--y', linewidth=1, marker='o', markerfacecolor='yellow', markersize=3, label='five')
# plt.plot(x1, y6, '--b', linewidth=1, marker='o', markerfacecolor='black', markersize=3, label='six')
# plt.plot(x1, y7, '--m', linewidth=1, marker='o', markerfacecolor='magenta', markersize=3, label='seven')
# plt.plot(x1, y8, '--y', linewidth=1, marker='o', markerfacecolor='yellow', markersize=3, label='eight')
# plt.plot(x1, y9, '--b', linewidth=1, marker='o', markerfacecolor='blue', markersize=3, label='nine')
# plt.plot(x1, y10, '--g', linewidth=1, marker='o', markerfacecolor='blue', markersize=3, label='ten')
# plt.xlabel('the number of time')
# plt.ylabel('the number of repost')
# plt.savefig('ten_data.png', dpi=400, bbox_inches='tight')
# plt.show()

# #  ------峰值 微博3小时传播次数和总传播次数的散点图------  #
# plt.figure(figsize=(7, 5))
# x1 = train['width12']
# y1 = train['repost_num']
# plt.scatter(x1, y1)
# plt.title('The relationship between spread_num and repost_num')
# plt.xlabel('the number of the spread_num')
# plt.ylabel('the number of the repost_num')
# plt.savefig('3_all.png', dpi=400, bbox_inches='tight')
# # plt.show()

# 绘制1天的广度变化图 横坐标为15分钟的 随着时间的变化微博传播广度的变化
# source = pd.read_csv('repostWidthCount.csv', sep=',')
# res = []
# for i in range(1, 97):
#     res.append('w'+str(i))
# data = source[res]
# y1 = data.iloc[0]  # 第一列数据
# y2 = data.iloc[1]  # 第一列数据
# y3 = data.iloc[2]  # 第一列数据
# y4 = data.iloc[3]  # 第一列数据
# y5 = data.iloc[4]  # 第一列数据
# y6 = data.iloc[5]  # 第一列数据
# y7 = data.iloc[6]  # 第一列数据
# y8 = data.iloc[7]  # 第一列数据
# y9 = data.iloc[8]  # 第一列数据
# y10 = data.iloc[9]  # 第一列数据
# time = range(0, 1440, 15)
# plt.figure(figsize=(7, 5))
# plt.plot(time, y1, '--b', linewidth=1, marker='o', markerfacecolor='blue', markersize=3)
# plt.plot(time, y2, '--g', linewidth=1, marker='+', markerfacecolor='green', markersize=3)
# plt.plot(time, y3, '--r', linewidth=1, marker='^', markerfacecolor='red', markersize=3)
# plt.plot(time, y4, '--c', linewidth=1, marker='v', markerfacecolor='cyan', markersize=3)
# plt.plot(time, y5, '--m', linewidth=1, marker='s', markerfacecolor='magenta', markersize=3)
# plt.plot(time, y6, '--y', linewidth=1, marker='D', markerfacecolor='yellow', markersize=3)
# plt.plot(time, y7, '--k', linewidth=1, marker='d', markerfacecolor='black', markersize=3)
# plt.plot(time, y8, '--g', linewidth=1, marker='<', markerfacecolor='green', markersize=3)
# plt.plot(time, y9, '--y', linewidth=1, marker='>', markerfacecolor='yellow', markersize=3)
# plt.plot(time, y10, '--r', linewidth=1, marker='o', markerfacecolor='cyan', markersize=3)
# plt.xlabel('the number of the time')
# plt.ylabel('the number of the width')
# plt.savefig('oneday_width.png', dpi=400, bbox_inches='tight')
# plt.show()

# ''''''''''''''''''''''''''''''''''''''''''''
#                  # 深度
# ''''''''''''''''''''''''''''''''''''''''''''
# #  ------微博转发路径长度比率图------  #
# test = pd.read_csv("depthlast.csv", sep=' ')
#
# plt.figure(figsize=(7, 5))
# depth = test['depth9']
# depth_dict = []
# for i in test['depth9']:
#     depth_dict.append(i)
# depths = set(depth_dict)
# result = []
# for d in depths:
#     rate = (int(depth_dict.count(d))) / len(depth_dict)
#     # 转发深度   总数   比率
#     # 筛选  除去比较离谱的值
#     if d < 150 and rate < 0.15:
#         result.append((d, str(depth_dict.count(d)), rate))
# # 取出比率
# depthz = [x[0] for x in result]
# rates = [x[2] for x in result]
# plt.scatter(depthz, rates)
# plt.title('The relationship between depth and depth_rate')
# plt.xlabel('the number of depth')  # 转发深度
# plt.ylabel('the number of depth_rate')  # 转发深度所占的总比率
# plt.savefig('depth_rating.png', dpi=400, bbox_inches='tight')
# # plt.show()
#
# #  ------所有微博转发深度和关注数的分布图------  #
# plt.figure(figsize=(7, 5))
# x = test['fans_num']
# y = test['depth9']
# follow_num = []
# depth_num = []
# # follow_num  depth_num
# for i in x:
#     if i < 1500000:
#         follow_num.append(i)
# for j in y:
#     if j < 110:
#         depth_num.append(j)
# # print(len(follow_num))
# # print(len(depth_num))
# plt.scatter(follow_num, depth_num, marker='o')
# plt.ylabel('the number of depth')
# plt.xlabel('the number of fans')
# plt.savefig('depth_fans.png', dpi=400, bbox_inches='tight')
# # plt.show()

# 绘制1天的深度变化图  随着时间的变化微博传播深度的变化
# source = pd.read_csv('repostDepthCount.csv', sep=',')
# res = []
# for i in range(1, 97):
#     res.append('w'+str(i))
# data = source[res]
# y1 = data.iloc[0]  # 第一列数据
# y2 = data.iloc[1]  # 第一列数据
# y3 = data.iloc[2]  # 第一列数据
# y4 = data.iloc[3]  # 第一列数据
# y5 = data.iloc[4]  # 第一列数据
# y6 = data.iloc[5]  # 第一列数据
# y7 = data.iloc[6]  # 第一列数据
# y8 = data.iloc[7]  # 第一列数据
# y9 = data.iloc[8]  # 第一列数据
# y10 = data.iloc[9]  # 第一列数据
# time = range(0, 1440, 15)
# plt.figure(figsize=(7, 5))
# plt.plot(time, y1, '--b', linewidth=1, marker='o', markerfacecolor='blue', markersize=3)
# plt.plot(time, y2, '--g', linewidth=1, marker='+', markerfacecolor='green', markersize=3)
# plt.plot(time, y3, '--r', linewidth=1, marker='^', markerfacecolor='red', markersize=3)
# plt.plot(time, y4, '--c', linewidth=1, marker='v', markerfacecolor='cyan', markersize=3)
# plt.plot(time, y5, '--m', linewidth=1, marker='s', markerfacecolor='magenta', markersize=3)
# plt.plot(time, y6, '--y', linewidth=1, marker='D', markerfacecolor='yellow', markersize=3)
# plt.plot(time, y7, '--k', linewidth=1, marker='d', markerfacecolor='black', markersize=3)
# plt.plot(time, y8, '--g', linewidth=1, marker='<', markerfacecolor='green', markersize=3)
# plt.plot(time, y9, '--y', linewidth=1, marker='>', markerfacecolor='yellow', markersize=3)
# plt.plot(time, y10, '--r', linewidth=1, marker='o', markerfacecolor='cyan', markersize=3)
# plt.xlabel('the number of the time')
# plt.ylabel('the number of the depth')
# plt.savefig('oneday_depth.png', dpi=400, bbox_inches='tight')
# plt.show()
# ''''''''''''''''''''''''''''''''''''''''''''
#                  # 算法优劣比较
# ''''''''''''''''''''''''''''''''''''''''''''
# # 比较七种模型的预测准确率柱状图
# plt.figure(figsize=(7, 5))
# plt.xlabel('Algorithm')
# plt.ylabel('average presicion')
# labels = ['KNN', 'Ada', 'Gaussian', 'DecisionTree', 'Improve_DecisionTree', 'RandomForest', 'Improve_RandomForest']
# precision_list = [1-0.368, 1-0.463, 1-0.572, 1-0.641, 1-0.378, 1-0.380, 1-0.07]
# for x, y in zip(range(len(precision_list)), precision_list):
#     plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
# plt.xticks(rotation=10)
# plt.bar(range(len(precision_list)), precision_list, tick_label=labels, width=0.5)
# plt.savefig('seven.png', dpi=400, bbox_inches='tight')
# # plt.show()
#
# # 改进的随机森林模型预测不同数量的微博与误差的关系图
# plt.figure(figsize=(7, 5))
# x1 = [50, 100, 1000, 2000, 3000, 4000, 4430]
# y1 = [0.074, 0.081, 0.10, 0.095, 0.099, 0.094, 0.092]
# plt.plot(x1, y1, linewidth=1, color='r', marker='o', markerfacecolor='blue', markersize=8)
# plt.ylabel('prediction error')
# plt.xlabel('the quantity of microblog')
# plt.savefig('imRF_difNUM.png', dpi=400, bbox_inches='tight')
# # plt.show()

