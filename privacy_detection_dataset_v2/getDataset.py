import requests
import pandas as pd
test_img_num = 0
test_label_list = []
test_urls_dataframe = pd.read_csv("test_urls.csv")
test_urls_data = test_urls_dataframe.values
test_img_label_dataframe = pd.read_csv("test_split_1_labels_only.csv", header=None)
test_img_label = test_img_label_dataframe.values
# print(len(test_img_label))
# print(test_img_label_dataframe)
# print(len(test_urls_data))
# print(test_urls_dataframe)
for i in range(len(test_urls_data)):
# for i in range(2):
    print("download:{}".format(test_urls_data[i][0]))
    print("is privacy:{}".format(test_img_label[i][0]))
    url = test_urls_data[i][0]
    filename = "./test/{}.jpg".format(test_img_num)  # 记得加上文件名称
    # 方法二
    # 获得图片二进制，速度比方法一快了4倍
    image = requests.get(url).content
    if(image != b"These aren't the droids you're looking for."):
        test_img_num += 1
        test_label_list.append(test_img_label[i])
        with open(filename,'wb') as f:
            f.write(image)
    else:
        print("error")

pd.DataFrame(test_label_list).to_csv("./label/test_split_label_only.csv",header=None, index=None)



train_img_num = 0
train_label_list = []
train_urls_dataframe = pd.read_csv("train_urls.csv")
train_urls_data = train_urls_dataframe.values
train_img_label_dataframe = pd.read_csv("train_split_1_labels_only.csv", header=None)
train_img_label = train_img_label_dataframe.values

for i in range(len(train_urls_data)):
# for i in range(2):
    print("download:{}".format(train_urls_data[i][0]))
    print("is privacy:{}".format(train_img_label[i][0]))
    url = train_urls_data[i][0]
    filename = "./train/{}.jpg".format(train_img_num)  # 记得加上文件名称
    # 方法二
    # 获得图片二进制，速度比方法一快了4倍
    image = requests.get(url).content
    if(image != b"These aren't the droids you're looking for."):
        train_img_num += 1
        train_label_list.append(train_img_label[i])
        with open(filename,'wb') as f:
            f.write(image)
    else:
        print("error")

pd.DataFrame(train_label_list).to_csv("./label/train_split_label_only.csv",header=None, index=None)


val_img_num = 0
val_label_list = []
val_urls_dataframe = pd.read_csv("val_urls.csv")
val_urls_data = val_urls_dataframe.values
val_img_label_dataframe = pd.read_csv("val_split_1_labels_only.csv", header=None)
val_img_label = val_img_label_dataframe.values

for i in range(len(val_urls_data)):
# for i in range(2):
    print("download:{}".format(val_urls_data[i][0]))
    print("is privacy:{}".format(val_img_label[i][0]))
    url = val_urls_data[i][0]
    filename = "./val/{}.jpg".format(val_img_num)  # 记得加上文件名称
    # 方法二
    # 获得图片二进制，速度比方法一快了4倍
    image = requests.get(url).content
    if(image != b"These aren't the droids you're looking for."):
        val_img_num += 1
        val_label_list.append(val_img_label[i])
        with open(filename,'wb') as f:
            f.write(image)
    else:
        print("error")

pd.DataFrame(val_label_list).to_csv("./label/val_split_label_only.csv",header=None, index=None)