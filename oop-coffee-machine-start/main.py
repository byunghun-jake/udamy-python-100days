from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    choice = input(f"음료를 선택하세요 ({menu.get_items()[:-1]}): ")

    # 기계 종료
    if choice == "off":
        break
    # report 출력
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # 메뉴 선택
    elif choice in menu.get_items().split("/"):
        drink = menu.find_drink(choice)

        # 재고 확인
        if not coffee_maker.is_resource_sufficient(drink):
            continue

        # 동전 투입 & 금액 확인 & 차액 환불
        if not money_machine.make_payment(drink.cost):
            continue

        # 커피 추출
        coffee_maker.make_coffee(drink)
