__all__ = ("A", "test_a")  # контейнер с компонентами в виде строк,
                           # которые могут быть использованы извне

__a = 10
__b = 10


def test_a():
    print("test_a from module some")


def test_b():
    print("test_b")


class A:
    pass


class B:
    pass
