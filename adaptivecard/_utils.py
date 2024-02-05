from typing import get_origin, get_args, Union, Any
from types import NoneType, UnionType


def check_type(arg_name: str, arg_value: Any, expected_type: tuple):
    # se for None
    if expected_type is NoneType and arg_value is not None:
        raise TypeError(f"argument '{arg_name}' must an instance of {NoneType}")
    # se for Union
    if get_origin(expected_type) is Union or isinstance(expected_type, UnionType):
        expected_type: tuple = get_args(expected_type)
    if isinstance(expected_type, tuple):
        for t in expected_type:
            try:
                return check_type(arg_name, arg_value, t)
            except TypeError:
                continue
        else:
            raise TypeError(f"argument '{arg_name}' must be one of {tuple((tp.__name__ for tp in expected_type))}, got {type(arg_value).__name__} instead")        
    # se for tipo parametrizado. Tipos contêiner só podem ter um parâmetro (com exceção da tupla)
    elif len((type_subscripts := get_args(expected_type))) > 0:
        if len(type_subscripts) > 1:
            raise Exception("Invalid type hint")
        if not isinstance(arg_value, get_origin(expected_type)):
            raise TypeError(f"argument '{arg_name}' must be an instance of {get_origin(expected_type).__name__}, got {type(arg_value).__name__} instead")
        for inner_value in arg_value:
            try:
                check_type(None, inner_value, type_subscripts)
            except:
                allowed_types = get_args(Union[type_subscripts])
                breakpoint()
                allowed_types = tuple([tp.__name__ for tp in allowed_types])
                raise TypeError(f"argument '{arg_name}' can only contain instances of {allowed_types}")
    else:
        if not isinstance(arg_value, expected_type):
            raise TypeError(f"argument '{arg_name}' must be an instance of {expected_type.__name__}, got {type(arg_value).__name__} instead")
