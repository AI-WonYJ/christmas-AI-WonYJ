from input_view import InputView
from output_view import OutputView
from event_planner import EventPlanner

def main():
    print("안녕하세요! 우테코 식당 12월 이벤트 플래너입니다.")

    date = InputView.read_date()
    order = InputView.read_order()

    planner = EventPlanner(date, order)
    planner.calculate_total_price()

    OutputView.print_event_summary(planner)

if __name__ == "__main__":
    main()
