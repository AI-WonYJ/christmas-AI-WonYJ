"""
12월 이벤트 플래너 프로그램의 입력 기능.
"""


class InputView:
    """사용자 입력을 처리하는 클래스"""

    @staticmethod
    def read_date():
        """사용자가 방문할 날짜를 입력받는다. 1~31 사이의 숫자만 허용된다."""
        while True:
            try:
                print("12월 중 식당 예상 방문 날짜는 언제인가요? (숫자만 입력해 주세요!)")
                date = int(
                    input()
                )
                if 1 <= date <= 31:
                    return date
                raise ValueError
            except ValueError:
                print("[ERROR] 유효하지 않은 날짜입니다. 다시 입력해 주세요.")

    @staticmethod
    def read_order():
        """사용자가 주문할 메뉴와 개수를 입력받는다. 올바른 형식인지 검증 후 반환한다."""
        while True:
            try:
                print(
                    "주문하실 메뉴를 메뉴와 개수를 알려 주세요. "
                    "(e.g. 해산물파스타-2,레드와인-1,초코케이크-1)")
                order_input = input()
                return InputView.validate_order(order_input)
            except ValueError as e:
                print(e)

    @staticmethod
    def validate_order(order_input):
        """입력된 주문 정보를 검증하고 딕셔너리 형태로 변환한다."""
        menu = {
            "양송이수프": 6000, "타파스": 5500, "시저샐러드": 8000,
            "티본스테이크": 55000, "바비큐립": 54000, "해산물파스타": 35000,
            "크리스마스파스타": 25000, "초코케이크": 15000, "아이스크림": 5000,
            "제로콜라": 3000, "레드와인": 60000, "샴페인": 25000
        }

        items = order_input.split(",")
        order = {}

        for item in items:
            InputView.process_order_item(item, order, menu)

        InputView.validate_not_only_drinks(order)
        InputView.validate_max_order_count(order)

        return order

    @staticmethod
    def process_order_item(item, order, menu):
        """개별 주문 항목을 검증하고 order 딕셔너리에 추가한다."""
        InputView.validate_item_format(item)
        name, quantity = item.replace(" ", "").split("-")
        InputView.validate_numeric_quantity(name, quantity)
        quantity = int(quantity)
        InputView.validate_menu_exists(name, menu)
        InputView.validate_no_duplicates(name, order)
        InputView.validate_quantity(name, quantity)

        order[name] = quantity

    @staticmethod
    def validate_item_format(item):
        """주문 형식이 올바른지 검증한다. (예: '해산물파스타-2')"""
        if "-" not in item:
            raise ValueError("[ERROR] 유효하지 않은 주문입니다. 다시 입력해 주세요.")

    @staticmethod
    def validate_numeric_quantity(name, quantity):
        """주문 개수가 숫자인지 확인한다."""
        if not quantity.isdigit():
            raise ValueError(
                f"[ERROR] 잘못된 수량 입력입니다: {name} ({quantity}). "
                "숫자로 입력해 주세요."
            )

    @staticmethod
    def validate_menu_exists(name, menu):
        """주문한 메뉴가 유효한 메뉴인지 확인한다."""
        if name not in menu:
            raise ValueError(f"[ERROR] 메뉴판에 없는 주문입니다: {name}. 다시 입력해 주세요.")

    @staticmethod
    def validate_no_duplicates(name, order):
        """중복된 주문이 있는지 확인한다."""
        if name in order:
            raise ValueError(
                f"[ERROR] 중복되는 주문입니다: {name}. 다시 입력해 주세요."
            )

    @staticmethod
    def validate_quantity(name, quantity):
        """메뉴 개수가 1개 이상인지 확인한다."""
        if quantity < 1:
            raise ValueError(
                f"[ERROR] 잘못된 수량입니다: {name} ({quantity}). "
                "1 이상의 숫자를 입력해 주세요."
            )

    @staticmethod
    def validate_not_only_drinks(order):
        """음료만 주문했는지 확인한다."""
        drinks = ["제로콜라", "레드와인", "샴페인"]
        if all(k in drinks for k in order):
            raise ValueError("[ERROR] 음료만 주문할 수 없습니다. 다시 입력해 주세요.")

    @staticmethod
    def validate_max_order_count(order):
        """주문 개수가 20개 이하인지 확인한다."""
        if sum(order.values()) > 20:
            raise ValueError("[ERROR] 최대 20개까지만 주문할 수 있습니다. 다시 입력해 주세요.")
