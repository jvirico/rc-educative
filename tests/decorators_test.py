from rc_educative.decorating import print_hello, print_something, print_this


def test__decorators__simple_decorator() -> None:
    print_something()


def test__decorators__params_decorator() -> None:
    print_this("iieeeeepaaa!")


def test__decorators__decorator_with_arguments() -> None:
    print_hello()
