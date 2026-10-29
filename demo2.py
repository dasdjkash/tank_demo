import random
#猜数字游戏
# 随机数生成：用random.randint(1, 100)生成 1-100 的随机数，作为目标数字；
# 循环判断：通过while True无限循环，直到用户猜对才用break退出；
# 输入校验：用try-except捕获用户输入非数字的情况，避免程序崩溃；

# 限制猜测次数（比如最多 10 次，超时提示失败）；
# 猜对后询问是否重新开始游戏；
# 调整随机数范围（比如 1-50，或自定义范围）。

def test_c():   #无限模式，猜对为止
    # 1. 生成1-？？？之间的随机整数（括号里传范围，不能漏）
        try:
            x = int(input("请设置区间数 1-？？？ ："))
            random_num = random.randint(1, x)
            cishu = 0
            print(f"我生成了一个随机数，在1-{x}之间")
            while True:
                try:
                    cishu += 1
                    sui_ji = int(input(f"请输入你猜测的数字（第{cishu}次）\n"))
                    # 2. 先校验范围，超出1-x直接重来，不计次数
                    if not 1 <= sui_ji <= x:
                        print(f"请输入1-{x}之间的整数，这次不计入次数")
                        cishu -= 1
                        continue
                    # 3. 判断大小
                    if sui_ji > random_num:
                        print("太大啦！再往小猜猜～")
                    elif sui_ji < random_num:
                        print("太小啦！再往大猜猜～")
                    else:
                        print("===恭喜你，猜对啦！===")
                        print(f"随机数是{random_num}")
                        print(f"你一共猜了{cishu}次")
                        break  # 4. 猜对必须 break 退出循环
                # 5. 只捕获"输入不是数字"的情况，不把英文报错甩给玩家
                except ValueError:
                    print("输入无效，请输入整数，这次不计入次数")
                    cishu -= 1
        except ValueError:
            print("输入无效，请输入整数")

def test_d():   #自己设置次数
    try:
        # 1. 生成1-x之间的随机整数（括号里传范围，不能漏）
        x = int(input("请设置区间数 1-？？？ ："))
    except ValueError:
        print("输入无效，请输入整数!")

        random_num = random.randint(1, x)
        zongshu = int(input("请设置次数"))
        cishu = 0
        print(f"我生成了一个随机数，在1-{x}之间")
        while True:
            try:
                sui_ji = int(input(f"请输入你猜测的数字（剩余{zongshu-cishu}次）\n"))
                cishu += 1
                # 2. 先校验范围，超出1-x直接重来，不计次数
                if not 1 <= sui_ji <= x:
                    print(f"请输入1-{x}之间的整数，这次不计入次数")
                    cishu -= 1
                    continue
                # 3. 判断大小
                if sui_ji > random_num:
                    print("太大啦！再往小猜猜～")
                elif sui_ji < random_num:
                    print("太小啦！再往大猜猜～")
                else:
                    print("===恭喜你，猜对啦！===")
                    print(f"随机数是{random_num}")
                    print(f"你一共猜了{cishu}次")
                    break  # 4. 猜对必须 break 退出循环
                if zongshu == cishu:
                    print("游戏结束！")
                    print(f"随机数是{random_num}")
                    print(f"你一共猜了{cishu}次")
                    break
            # 5. 只捕获"输入不是数字"的情况，不把英文报错甩给玩家
            except ValueError:
                print("输入无效，请输入整数，这次不计入次数")
                cishu -= 1
def gemas():
    print("===欢迎进入猜数字游戏===")
    print("1、无限模式")
    print("2、有限模式")
    while True:
        try:
            number = int(input("请输入：1或2\n"))
            if number == 1:
                test_c()
                break
            elif number == 2:
                test_d()
                break
            else:
                print("输入无效，请重新输入!")
                continue
        except ValueError:
            print("输入无效，请输入整数!")
            continue
gemas()