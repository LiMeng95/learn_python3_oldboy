# -*- coding: utf-8 -*-
# Python: 3.6
# Author: Meng Li

# 作业三：三级菜单程序
"""
任务说明：
- 打印大洲、国家、主要城市三级菜单
- 可返回上一级
- 可随时退出程序
"""

city_catalog = {
    "Asia" : {
        "China":{
            "Beijing":["1.641万平方千米","2170.7万"],
            "Shanghai":["6340平方公里","2418.33万"],
            "Shenzhen": ["1996.85平方公里", "1252.83万"]
        },
        "South Korea": {
            "Seoul":["605.77平方千米","1014万"]
        },
        "Japan": {
            "Tokyo": ["2155平方千米", "3700万"]
        }
    },
    "Europe" : {
        "UK":{
            "London": ["1577平方千米", "828万"]
        },
        "Italy": {
            "Roma": ["1285.306平方公里", "286.8万"]
        }
    },
    "Americas" : {
        "America":{
            "Washington D.C": ["177平方公里", "68.1万"]
        },
        "Argentina": {
            "Buenos Aires": ["203平方公里", "1995万"]
        }
    }
}

# 方法一
"""
exit_flag = False
while not exit_flag:
    for i in city_catalog:                          # 打印第一级
        print(i)  # key

    choice1 = input("选择进入('q'退出)>>：")        # 输入关键字
    if choice1 in city_catalog:                     # 如果有该关键字，进入
        while not exit_flag:
            for j in city_catalog[choice1]:             # 打印第二级
                print("\t", j)
            choice2 = input("选择进入('b'返回，'q'退出)>>：")        # 输入关键字
            if choice2 in city_catalog[choice1]:                    # 如果有该关键字，进入
                while not exit_flag:
                    for k in city_catalog[choice1][choice2]:                # 打印第三级
                        print("\t\t", k)
                    choice3 = input("选择关键字('b'返回，'q'退出)>>：")      # 输入关键字
                    if choice3 in city_catalog[choice1][choice2]:           # 如果有该关键字,打印
                        print('-->',city_catalog[choice1][choice2][choice3])
                    elif choice3 == 'q':                            # 如果'q',退出
                        exit_flag = True
                    elif choice3 == 'b':
                        break
                    else:
                        continue
            elif choice2 == 'q':                            # 如果'q',退出
                exit_flag = True
            elif choice2 == 'b':
                break
            else:
                continue
    elif choice1 == 'q':                            # 如果'q',退出
        exit_flag = True
    else:
        continue
"""

# 方法二
current_layer = city_catalog  # 当前层
layer_cache = [city_catalog]  # 缓存列表

while True:
    if len(layer_cache) == 4:
        print(current_layer)
    else:
        for i in current_layer:
            print(i)
    choice = input("Your choice('q':quit,'b':back)")
    if choice == 'q':
        break
    elif choice == 'b':
        # exit_flag = False
        if len(layer_cache) == 1:
            print('This is the first layer, can not go back...')
        else:
            layer_cache.pop()
            current_layer = layer_cache[-1]
    elif choice in current_layer:
        layer_cache.append(current_layer[choice])
        current_layer = current_layer[choice]
    else:
        continue
