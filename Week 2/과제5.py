

def showMenu():
    print("===== 2022 coffee menu =====")
    print("0. 주문 종료")
    print("1. %s :  %d원" %(menu1,price1))
    print("2. %s :  %d원\n" %(menu2,price2))
    print("사이즈 : Tall +%d원, Grande +%d원, Venti +%d원"%(tall, grande, venti))
    print("============================")


def selectMenu():
    global coffee,breakFlag,continueFlag    
    menu=int(input("메뉴를 선택하시오 : "))

    if menu==1:
        print("%s를 선택하셨습니다."%menu1)
        coffee +=price1
        
    elif menu==2:
        print("%s를 선택하셨습니다."%menu2)
        coffee +=price2
    elif menu==0:
        print("주문을 종료합니다.")
        breakFlag=True


    else:
        print("올바른 메뉴를 입력하시오.")
        continueFlag==True

    print("현재 주문 금액 : %d\n"%total_price)



def selectSize():
    global tall,venti,grande,coffee,total_price
    size=int(input("사이즈를 선택하시오 (1. Tall 2. Grande 3. Venti) : "))

    if size==1:
        coffee +=tall
        total_price +=coffee
        
    elif size==2:
        coffee +=grande
        total_price +=coffee
        
    elif size==3:
        coffee +=venti
        total_price +=coffee
        
    else:
        print("올바른 사이즈를 입력하세요.")


    print("현재 주문 금액 : %d\n"%total_price)

def payment():
    cash=int(input("현금을 넣어주세요: "))
    change=cash-total_price


    print("잔돈은 %d원입니다. 안녕히 가십시오."%change)
    
    

if __name__ =="__main__":

    menu1="아메리카노"
    menu2="카페라떼"

    price1=4100
    price2=4600

    tall=0
    grande=500
    venti=1000

    total_price=0
    breakFlag=False
    continueFlag=False
    
    
while True:
  
    
    continueFlag==False

    coffee =0
    
    showMenu()
    selectMenu()

    if breakFlag==True:
        break

    if continueFlag==True:
        continue
    
    selectSize()


payment()


   
