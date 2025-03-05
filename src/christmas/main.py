from input_view import InputView
from output_view import OutputView
from event_planner import EventPlanner

def main():
    print("안녕하세요! 우테코 식당 12월 이벤트 플래너입니다.")
    
    # 방문 날짜 및 주문 정보 입력
    date = InputView.read_date()
    order = InputView.read_order()

    # 이벤트 플래너 생성 및 할인 적용
    planner = EventPlanner(date, order)
    planner.calculate_event()

    # 결과 출력
    OutputView.print_event_summary(planner)

if __name__ == "__main__":
    main()
