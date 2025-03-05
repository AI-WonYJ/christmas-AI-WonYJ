class OutputView:
    @staticmethod
    def print_event_summary(planner):
        print(f"\n🎉 12월 {planner.date}일에 우테코 식당에서 받을 이벤트 혜택 미리 보기! 🎉\n")
        
        print("<주문 메뉴>")
        for item, quantity in planner.order.items():
            print(f"{item} {quantity}개")
        
        print("\n<할인 전 총주문 금액>")
        print(f"{planner.total_price}원")
        
        print("\n<증정 메뉴>")
        print("샴페인 1개" if planner.gift else "없음")
        
        print("\n<혜택 내역>")
        if planner.benefits:
            for benefit, amount in planner.benefits.items():
                print(f"{benefit}: -{amount}원")
        if not planner.benefits:
            print("없음")
        
        print("\n<총혜택 금액>")
        print(f"-{planner.total_benefits}원")

        print("\n<할인 후 예상 결제 금액>")
        print(f"{planner.final_price}원")

        print("\n<12월 이벤트 배지>")
        print(planner.badge if planner.badge else "없음")
