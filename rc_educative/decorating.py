from rc_educative.decorators import decorator_with_args, params_decorator, simple_decorator, some_decorator


@simple_decorator
def print_something() -> None:
    print("iiieeeeee!")


@params_decorator
def print_this(this: str) -> None:
    print(this)


@decorator_with_args(num=5)
def print_hello() -> None:
    print("Hello!")


@simple_decorator
@decorator_with_args(10)
def stacking_decorator() -> None:
    print("Works just fine :)")


@some_decorator
def using_functools():
    """This method uses a decorator which respects method metadata"""
    print("Aserejé!")


# NOTE: run this code with 'poetry run python -m rc_educative.decorating'
print_something()
print_this("pachamama")
print_hello()
stacking_decorator()
using_functools()
print(using_functools.__name__)
print(using_functools.__doc__)
