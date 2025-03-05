from unittest.mock import patch
from io import StringIO
from christmas.main import main


def run_io_fun(inputs):
    """
    inputs: 리스트 형태로, 각 줄에 입력할 값을 순서대로 담는다.
    예) ["3", "티본스테이크-1,바비큐립-1,초코케이크-2,제로콜라-1"]
    """
    with patch("builtins.input", side_effect=inputs):
        buffer = StringIO()
        with patch("sys.stdout", new=buffer):
            main()
        outputs = buffer.getvalue()
    return outputs


def test_모든_타이틀_출력():
    outputs = run_io_fun(["3", "티본스테이크-1,바비큐립-1,초코케이크-2,제로콜라-1"])
    assert all(
        expected_output in outputs
        for expected_output in [
            "12월 3일에 우테코 식당에서 받을 이벤트 혜택 미리 보기!",
            "<주문 메뉴>\n티본스테이크 1개\n바비큐립 1개\n초코케이크 2개\n제로콜라 1개",
            "<할인 전 총주문 금액>\n142,000원",
            "<증정 메뉴>\n샴페인 1개",
            "<혜택 내역>\n크리스마스 디데이 할인: -1,200원\n평일 할인: -4,046원\n특별 할인: -1,000원\n증정 이벤트: -25,000원",
            "<총혜택 금액>\n-31,246원",
            "<할인 후 예상 결제 금액>\n110,754원",
            "<12월 이벤트 배지>\n산타",
        ]
    )


def test_혜택_내역_없음_출력():
    outputs = run_io_fun(["26", "타파스-1,제로콜라-1"])
    assert "<혜택 내역>\n없음" in outputs


def test_날짜_입력_흐름():
    """잘못된 입력 후 재입력하여 정상적인 흐름이 유지되는지 확인"""

    outputs = run_io_fun(["a", "32", "0", "3", "티본스테이크-1"])

    # 에러 메시지가 3번 출력되고, 정상 입력 이후 주문 단계로 넘어가는지 확인
    assert outputs.count("[ERROR] 유효하지 않은 날짜입니다. 다시 입력해 주세요.") == 3

def test_주문_예외_테스트():
    """잘못된 주문 입력 후 정상적인 입력으로 재입력되는지 확인"""

    outputs = run_io_fun(["3", "티본스테이크-a", "티본스테이크-1"])

    assert outputs.count("[ERROR] 잘못된 수량 입력입니다: 티본스테이크 (a). 숫자로 입력해 주세요.") == 1
    assert "티본스테이크 1개" in outputs


def test_메뉴판_없는_주문():
    """메뉴판에 없는 메뉴를 주문할 경우 예외가 발생하는지 확인"""
    
    outputs = run_io_fun(["3", "초콜릿-1", "티본스테이크-1"])

    assert "[ERROR] 메뉴판에 없는 주문입니다: 초콜릿. 다시 입력해 주세요." in outputs
    assert "티본스테이크 1개" in outputs


def test_중복_주문_예외():
    """같은 메뉴를 중복 입력할 경우 예외가 발생하는지 확인"""

    outputs = run_io_fun(["3", "티본스테이크-1,티본스테이크-1", "티본스테이크-1,바비큐립-1"])

    assert "[ERROR] 중복되는 주문입니다: 티본스테이크. 다시 입력해 주세요." in outputs
    assert "티본스테이크 1개\n바비큐립 1개" in outputs  # 정상적인 입력 이후 정상 진행되는지 확인


def test_잘못된_수량_주문():
    """수량을 1 미만으로 입력할 경우 예외가 발생하는지 확인"""

    outputs = run_io_fun(["3", "티본스테이크-0", "바비큐립-1"])

    assert "[ERROR] 잘못된 수량입니다: 티본스테이크 (0). 1 이상의 숫자를 입력해 주세요." in outputs
    assert "바비큐립 1개" in outputs  # 정상적인 입력 이후 정상 진행되는지 확인


def test_음료만_주문_예외():
    """음료만 주문할 경우 예외가 발생하는지 확인"""

    outputs = run_io_fun(["3", "제로콜라-1,레드와인-1", "티본스테이크-1,제로콜라-1"])

    assert "[ERROR] 음료만 주문할 수 없습니다. 다시 입력해 주세요." in outputs
    assert "티본스테이크 1개\n제로콜라 1개" in outputs  # 정상적인 입력 이후 정상 진행되는지 확인


def test_주문_최대개수_초과():
    """주문 개수가 20개를 초과할 경우 예외가 발생하는지 확인"""

    outputs = run_io_fun(["3", "티본스테이크-10,바비큐립-11", "바비큐립-1"])

    assert "[ERROR] 최대 20개까지만 주문할 수 있습니다. 다시 입력해 주세요." in outputs
    assert "바비큐립 1개" in outputs  # 정상적인 입력 이후 정상 진행되는지 확인
