#부모 클래스
class Passbook:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,money):
        self.balance+=money
        print(f"입금된 금액:{money}₩")
        print(f"잔액:{self.balance}₩")
    def withdraw(self,money):
        if money <= self.balance:
            self.balance-=money
            print(f"출급된 금액:{money}₩")
            print(f"잔액:{self.balance}₩")
        else:
            print("잔액 부족")
    def showInfo(self):
        print(f"예금주:{self.owner}")
        print(f"잔액:{self.balance}₩")
#자식 클래스
class MinusPassbook(Passbook): #상속
    #재정의(오버라이딩)
    def withdraw(self,money):

        if (self.balance-money)>= -1000000:
            self.balance-=money
            print(f"출급된 금액:{money}₩")
            print(f"잔액:{self.balance}₩")
        else:
            print("마이너스 한도 초과")

#실행
account1=Passbook("홍길동", 100000)
account1.showInfo()
account1.deposit(50000)
account1.withdraw(120000)
account1.withdraw(70000)

account2=MinusPassbook("김철수", 100000)
account2.showInfo()
account2.withdraw(120000) #자식클래스 호출
account2.withdraw(9000000)