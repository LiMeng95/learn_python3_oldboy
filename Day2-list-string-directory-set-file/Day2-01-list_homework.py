# -*- coding: utf-8 -*-
# Python: 3.6
# Author: Meng Li

# 作业二：购物车
"""
任务说明：
- 启动程序后，让用户输入工资，然后打印商品列表
- 允许用户根据商品编号购买商品
- 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
- 可随时退出，退出时，打印已购买商品和余额
"""

# 商品列表
commodity_list = [['Computer', 5000], ['bicycle', 1000], ['book', 40], ['keyboard', 200], ['bottle', 30]]
salary = input("Please input your salary:")  # 输入工资
shopping_list = []
if salary.isdigit():
    salary = int(salary)

state = 0  # 购物状态
while True:
    print("commodity_list:")
    for index, i in enumerate(commodity_list):                            # 打印商品列表,enumerate用于取出列表下标
        print(index,i)

    commodity_number = input("Please input commodity number (q:quit):")  # 输入购买编号,q为退出

    if commodity_number == 'q':  # 退出
        break
    elif commodity_number.isdigit() and 0 <= int(commodity_number) < len(commodity_list):  # 在商品范围内
        commodity_number = int(commodity_number)
        if salary - commodity_list[commodity_number][1] > 0:      # 余额够
            salary = salary - commodity_list[commodity_number][1]
            for bought in shopping_list:                                     # 查找是否已经买过了
                if bought[1] == commodity_list[commodity_number][0]:
                    bought[3] += 1
                    break
            else:                                                            # 遍历一遍之后没有买过
                bought = [str(state), commodity_list[commodity_number][0], commodity_list[commodity_number][1], 1]
                shopping_list.append(bought)
                state += 1
            print()
        else:                                                             # 余额不够
            print("Your salary is not enough!")
    else:
        print("Invalid input!")
        continue


print("Your balance:", salary)
print("Your shopping list:")
print(['number', 'commodity', 'price', 'quantity'])
for i in shopping_list:
    print(i)
