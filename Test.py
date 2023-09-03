s = "python"
# ctrl shift f10 运行
# for i in s:
#   print(i)
# for i in range(10):
# print(i)

import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\caizi\Desktop\Intro to Machine Learning\hw1\handout\heart_train.tsv", sep='\t')
# 分隔符！！！！！！！四个空格就是四个空格，不能省略
# print(df.head(3)) # 打印前几行（不包括索引

a = df['heart_disease']
count1 = 0
count0 = 0
for item in a:
    if item == 1:
        count1 += 1
    else:
        count0 += 1

flag = 0
if count1 >= count0:
    flag = 1
total1 = count1 + count0

pre_ans = pd.Series()
for item in range(0, total1):
    pre_ans[item] = flag
correct = 0
total = 0
for i in a:
    if i == pre_ans[i]:
        correct += 1
    total += 1
accuracy1 = 1 - correct / total
print(round(accuracy1, 6))

df2 = pd.read_csv(r"C:\Users\caizi\Desktop\Intro to Machine Learning\hw1\handout\heart_test.tsv", sep='\t')

correct = 0
total = 0
a2 = df2['heart_disease']
for item in a2:
    if item == pre_ans[item]:
        correct += 1
    total += 1

accuracy_test = 1 - correct / total
print(round(accuracy_test, 6))

# df.columns=list('AB')
# print(df['A'])


# 如果是excel就是read_excel

# print(df)
# with open(education_train.tsv,)
# tsvFile = file("education_train.tsv")

# for s in tsvFile:
#  print(s)
