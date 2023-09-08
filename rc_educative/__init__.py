from typing import Callable, Any, TypeVar


# Define a Type variable that represents a callable.
# This can be useful to type decorators with wrap generic funcitons.
F = TypeVar('F', bound=Callable[..., Any])
