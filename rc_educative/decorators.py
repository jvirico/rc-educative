from functools import wraps
from typing import Callable, Any, Tuple, Dict, TypeVar
from rc_educative import F


def simple_decorator(func: F) -> F:
    @wraps(func)
    def wrapper() -> Any:
        print("Hello from decorator!")
        return func()
    return wrapper


def params_decorator(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Tuple[Any], **kwargs: Dict[str, Any]):
        print("Hello from params decorator!")
        func(*args, **kwargs)

    return wrapper


def decorator_with_args(num: int) -> Callable[[F], F]:
    def wrapper1(func: F) -> F:
        @wraps(func)
        def wrapper2(*args: Tuple[Any], **kwargs: Dict[str, Any]):
            print(str(num))
            func(*args, **kwargs)
        return wrapper2
    return wrapper1


# NOTE: To keep the metadata of the original
# function (like its name, docstring, etc.) when it's decorated,
# you should use functools.wraps.
def some_decorator(func: F) -> F:
    @wraps(func)
    def wrapper(*args: Tuple[Any], **kwargs: Dict[str, Any]):
        print("My decoator!")
        func(*args, **kwargs)
    return wrapper
