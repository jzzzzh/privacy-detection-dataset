import os
import pandas as pd
test_img_path = "./test"
train_img_path = "./train"
val_img_path = "./val"
test_img_label = './label/test_split_label_only.csv'
train_img_label = './label/train_split_label_only.csv'
val_img_label = './label/val_split_label_only.csv'
final_test_label ='./finallabel/test_split_label_only.csv'
final_train_label ='./finallabel/train_split_label_only.csv'
final_val_label ='./finallabel/val_split_label_only.csv'

def getFileSize(filePath, size=0):
    size = os.path.getsize(filePath)
    return size

def is_null(filePath):
    if(getFileSize(filePath) < 500):
        return True
    else:
        return False
    
# test_img_label_dataframe = pd.read_csv(test_img_label,header=None)
# test_img_label_data = test_img_label_dataframe.values
# # print(len(test_img_label_data))
# test_null_num = 0
# test_num = 0
# test_label_list_not_null = []
# for i in range(len(test_img_label_data)):
#     img_path = test_img_path + "/{}.jpg".format(i)
#     change_img_path = test_img_path + "/{}.jpg".format(test_num)
#     size = getFileSize(img_path)
#     if(is_null(img_path)):
#         print(size)
#         os.remove(img_path)
#         test_null_num+=1
#     else:
#         test_label_list_not_null.append(test_img_label_data[i])
#         os.rename(img_path, change_img_path)
#         test_num+=1

# pd.DataFrame(test_label_list_not_null).to_csv(final_test_label,header=None, index=None)
# print(test_null_num)



# val_img_label_dataframe = pd.read_csv(val_img_label,header=None)
# val_img_label_data = val_img_label_dataframe.values
# # print(len(val_img_label_data))
# val_null_num = 0
# val_num = 0
# val_label_list_not_null = []
# for i in range(len(val_img_label_data)):
#     img_path = val_img_path + "/{}.jpg".format(i)
#     change_img_path = val_img_path + "/{}.jpg".format(val_num)
#     size = getFileSize(img_path)
#     if(is_null(img_path)):
#         print(size)
#         os.remove(img_path)
#         val_null_num+=1
#     else:
#         val_label_list_not_null.append(val_img_label_data[i])
#         os.rename(img_path, change_img_path)
#         val_num+=1

# pd.DataFrame(val_label_list_not_null).to_csv(final_val_label,header=None, index=None)
# print(val_null_num)

train_img_label_dataframe = pd.read_csv(train_img_label,header=None)
train_img_label_data = train_img_label_dataframe.values
# print(len(train_img_label_data))
train_null_num = 0
train_num = 0
train_label_list_not_null = []
for i in range(len(train_img_label_data)):
    img_path = train_img_path + "/{}.jpg".format(i)
    change_img_path = train_img_path + "/{}.jpg".format(train_num)
    size = getFileSize(img_path)
    if(is_null(img_path)):
        print(size)
        os.remove(img_path)
        train_null_num+=1
    else:
        train_label_list_not_null.append(train_img_label_data[i])
        os.rename(img_path, change_img_path)
        train_num+=1

pd.DataFrame(train_label_list_not_null).to_csv(final_train_label,header=None, index=None)
print(train_null_num)