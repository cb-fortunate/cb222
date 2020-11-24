"""
作者：陈斌
程序目标：
"""
import random
#0=="石头"
#1=="史波克"
#2=="布"
#3=="蜥蜴"
#4=="剪刀"
def name_to_number(name):
    if name=="石头":
        number=0
    elif name=="史波克":
        number=1
    elif name=="布":
        number=2
    elif name=="蜥蜴":
        number=3
    elif name=="剪刀":
        number=4
    else :
        print("Error: No Correct Name")
    return number
def number_to_name(number):
    if number==0:
        name="石头"
    elif number==1:
        name="史波克"
    elif number==2:
        name="布"
    elif number==3:
        name="蜥蜴"
    elif number==4:
        name="剪刀"
    return name
def rpsls(player_choice):
    player_choice_number=name_to_number(player_choice)
    computer_choice_number=random.randint(0,4)
    computer_choice=number_to_name(computer_choice_number)
    print("计算机的选择是%s"%(computer_choice))
    if player_choice_number==0:
        if computer_choice_number==0:
            print("您和计算机选得一样呢")
        elif computer_choice_number==3 or computer_choice_number==4:
            print("您赢了")
        else:
            print("您输了")
        return
    if player_choice_number==1:
        if computer_choice_number==1:
            print("您和计算机选得一样呢")
        elif computer_choice_number==0 or computer_choice_number==4:
            print("您赢了")
        else:
            print("您输了")
        return
    if player_choice_number==2:
        if computer_choice_number==2:
            print("您和计算机选得一样呢")
        elif computer_choice_number==0 or computer_choice_number==1:
            print("您赢了")
        else:
            print("您输了")
        return
    if player_choice_number==3:
        if computer_choice_number==3:
            print("您和计算机选得一样呢")
        elif computer_choice_number==1 or computer_choice_number==2:
            print("您赢了")
        else:
            print("您输了")
        return
    if player_choice_number==4:
        if computer_choice_number==4:
            print("您和计算机选得一样呢")
        elif computer_choice_number==3 or computer_choice_number==2:
            print("您赢了")
        else:
            print("您输了")
        return
print("欢迎使用RPSLS游戏")
print('-----------------')
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)




