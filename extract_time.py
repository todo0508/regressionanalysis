import csv

# ファイルをオープンする
test_data = open("sample.txt", "r")
f = open('result.csv', mode='ab')
csvWriter = csv.writer(f)

# 行ごとにすべて読み込んでリストデータにする
lines = test_data.readlines()
list = []
i=0
result = []

# 一行ずつ表示する
for line in lines:
  #print(line)
  list.append(line)
  i=i+1
  if i == 12:
    #print(list)
    #print(max(list))
    result.append(float(max(list)))
    list = []
    i=0

#print(result)
#csvWriter.writerows(result)

# ファイルをクローズする
test_data.close()


for hoge in result:
  print(hoge)

