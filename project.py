array = []  # 建立一個空的列表用來存儲使用者輸入的數據

while True:  # 創建一個無窮循環
    user_input = input("請輸入一個數字，輸入完成請輸入'a'來結束輸入：")  # 使用者輸入數值和停止輸入的方式
    if user_input == 'a':
        if 2 <= len(array) <= 104:
            break
        else:
            print("陣列的長度必須在2到104之間，請再輸入更多數字。")
    else:
        try:
            number = int(user_input)
            if -1e9 <= number <= 1e9:
                array.append(number)
            else:
                print("輸入的數字必須在 -1e9 到 1e9 之間。") 
        except ValueError:  # 如果輸入的不是一個數字
            print("這不是一個有效的數字，請再試一次")

print("你輸入的數字是：", array)  # 讓使用者確認自己目前輸入的陣列數值

while True:# 使用者輸入target
    target = int(input("請輸入一個目標數字："))
    if -1e9 <= target <= 1e9:
        break
    else:
        print("目標數字必須在 -1e9 到 1e9 之間。")

# 建立字典儲存數字和在array中的位置
num_dict = {}

for i, num in enumerate(array):  # 利用enumerate找出位置和數值
    if target - num in num_dict and i != num_dict[target - num]:  # 用target-num找出數值是否存在於num_dict中並且在陣列中位置是不相同的
        print("[{},{}]" .format(num_dict[target - num], i))
        break
    num_dict[num] = i  # 若未找到匹配數字，則設置num在陣列中的索引i，後續查詢會比較快找到
else:
    print("在array中找不到兩個數字的總和等於{}，請重新輸入數值。".format(target))