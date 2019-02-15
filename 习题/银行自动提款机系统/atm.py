from card import Card
from user import User
import random
import time
class ATM(object):
    def __init__(self, allUser):
        self.allUsers = allUser
    def createUser(self):
        #目标：向用户字典中添加一对键值对（卡号-用户）
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")

        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0:
            print("预存款输入有误！开户失败。")
            return -1

        onePasswd = input("请设置密码：")
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！开户失败……")
            return 1

        #所有需要的信息就全了
        cardStr = self.randomCardId()
        card = Card(cardStr, onePasswd, prestoreMoney)
        user = User(name, idCard, phone, card)
        #存到字典

        self.allUsers[cardStr] = user
        print("开户成功！请牢记卡号！(%s)" % cardStr)

    def searchUserInfo(self):
        cardNum = input("请输入您的卡号：")
        #验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！")
            return -1
        #判断是否锁定
        if user.card.cardLock == True:
            print("该卡已经锁定，请解锁后再执行其它操作！")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！该卡已经锁定，请解锁后再执行其它操作！！")
            user.card.cardLock = True
            return -1
        print("账号： %s  余额： %d" % (user.card.cardId,user.card.cardMoney))
    def getMoney(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！")
            return -1
        # 判断是否锁定
        if user.card.cardLock == True:
            print("该卡已经锁定，请解锁后再执行其它操作！")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！该卡已经锁定，请解锁后再执行其它操作！！")
            user.card.cardLock = True
            return -1
        #取款
        money = int(input("请输入取款金额："))
        if money > user.card.cardMoney:
            print("余额不足！取款失败！")
            return -1
        user.card.cardMoney -= money
        print("取款成功！余额：%d" % (user.card.cardMoney))
    def saveMoney(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！")
            return -1
        # 判断是否锁定
        if user.card.cardLock == True:
            print("该卡已经锁定，请解锁后再执行其它操作！")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！该卡已经锁定，请解锁后再执行其它操作！！")
            user.card.cardLock = True
            return -1
        # 存款
        money = int(input("请输入存款金额："))
        if money <= 0:
            print("存款金额不能小于0！存款失败！")
            return -1
        user.card.cardMoney += money
        print("存款成功！余额：%d" % (user.card.cardMoney))
    def transferMoney(self):
        pass
    def changePasswd(self):
        pass
    def lockUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！锁定失败！")
            return -1
        if user.card.cardLock:
            print("该卡已经锁定，请解锁后再使用其它功能")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！锁定失败！")
            return -1
        #tempIdCard = input("请输入您的身份证号码:")
        #if tempIdCard != user.idCard:
            #print("身份证号输入有误！锁定失败！")
            #return -1

        #锁它
        user.card.cardLock = True
        print("锁定成功！")

    def unlockUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！解锁失败！")
            return -1
        if not user.card.cardLock:
            print("该卡没有锁定，无需解锁！")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！解锁失败！")
            return -1
        #tempIdCard = input("请输入您的身份证号码：")
        #if tempIdCard != user.idCard:
            #print("身份证号输入有误！解锁失败！")
            #return -1
        #解锁
        user.card.cardLock = False
        print("解锁成功！")

    def mewCard(self):
        pass
    def killUser(self):
        pass

    #验证密码
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd ==realPasswd:
                return True
        return False

    #生成卡号
    def randomCardId(self):
        while True:

            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1 ))
                str += ch
                #判断是否重复
            if not self.allUsers.get(str):
                return str
                time.sleep(2)






