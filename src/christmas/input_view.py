class InputView:
    @staticmethod
    def read_date():
        while True:
            try:
                date = int(input("12월 중 식당 예상 방문 날짜는 언제인가요? (숫자만 입력해 주세요!)\n"))
                if 1 <= date <= 31:
                    return date
                raise ValueError
            except ValueError:
                print("[ERROR] 유호하지 않은 날짜입니다. 다시 입력해 주세요.")

    @staticmethod
    def read_order():
        while True:
            try:
                order_input = input("주문하실 메뉴를 메뉴와 개수를 알려 주세요. (e.g. 해산물파스타-2,레드와인-1,초코케이크-1)\n")
                return InputView.validate_order(order_input)
            except ValueError as e:
                print(e)

    @staticmethod
    def validate_order(order_input):
        menu = {
            "양송이수프": 6000, "타파스": 5500, "시저샐러드": 8000,
            "티본스테이크": 55000, "바비큐립": 54000, "해산물파스타": 35000, "크리스마스파스타": 25000,
            "초코케이크": 15000, "아이스크림": 5000,
            "제로콜라": 3000, "레드와인": 60000, "샴페인": 25000
        }
        items = order_input.split(",")
        order = {}

        for item in items:
            InputView.validate_item_format(item)
            name, quantity = item.split("-")

            InputView.validate_numeric_quantity(name, quantity)
            quantity = int(quantity)

            InputView.validate_menu_exists(name, menu)
            InputView.validate_no_duplicates(name, order)
            InputView.validate_quantity(name, quantity)

            order[name] = quantity

        InputView.validate_not_only_drinks(order)
        InputView.validate_max_order_count(order)

        return order

    @staticmethod
    def validate_item_format(item):
        if "-" not in item:
            raise ValueError("[ERROR] 유효하지 않은 주문 형식입니다. 다시 입력해 주세요.")

    @staticmethod
    def validate_numeric_quantity(name, quantity):
        if not quantity.isdigit():
            raise ValueError(f"[ERROR] 잘못된 수량 입력입니다: {name} ({quantity}). 숫자로 입력해 주세요.")

    @staticmethod
    def validate_menu_exists(name, menu):
        if name not in menu:
            raise ValueError(f"[ERROR] 메뉴판에 없는 주문입니다: {name}. 다시 입력해 주세요.")

    @staticmethod
    def validate_no_duplicates(name, order):
        if name in order :
            raise ValueError(f"[ERROR] 중복되는 주문입니다.: {name} 다시 입력해 주세요.")

    @staticmethod
    def validate_quantity(name, quantity):
        if quantity < 1:
            raise ValueError(f"[ERROR] 잘못된 수량입니다: {name} ({quantity}). 1 이상의 숫자를 입력해 주세요.")

    @staticmethod
    def validate_not_only_drinks(order):
        if all(k in ["제로콜라", "레드와인", "샴페인"] for k in order):
            raise ValueError("[ERROR] 음료만 주문할 수 없습니다. 다시 입력해 주세요.")

    @staticmethod
    def validate_max_order_count(order):
        if sum(order.values()) > 20:
            raise ValueError("[ERROR] 최대 20개까지만 주문할 수 있습니다. 다시 입력해 주세요.")