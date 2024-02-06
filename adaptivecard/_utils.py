from typing import get_origin, get_args, Union, Literal, Any, Iterable, Sequence
from types import NoneType, UnionType


def check_type(arg_name: str, arg_value: Any, expected_type: tuple):
    if expected_type is Any:
        return
    # se for Literal
    if get_origin(expected_type) is Literal:
        literals = get_args(expected_type)
        if arg_value not in literals:
            raise TypeError(f"argument '{arg_name}' must be equal to one of {tuple(literals)}, got {arg_value} instead")
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
    # se for tipo contêiner parametrizado. Tipos contêiner só podem ter um parâmetro (com exceção da tupla)
    elif len((type_subscripts := get_args(expected_type))) > 0 and isinstance(arg_value, Iterable):
        if not isinstance(arg_value, get_origin(expected_type)):
            raise TypeError(f"argument '{arg_name}' must be an instance of {get_origin(expected_type).__name__}, got {type(arg_value).__name__} instead")
        for inner_value in arg_value:
            try:
                check_type(None, inner_value, type_subscripts)
            except:
                allowed_types = (get_args(tp) if get_origin(tp) is Union or isinstance(tp, UnionType) else tp for tp in type_subscripts)
                allowed_types = tuple([tp.__name__ for tp in allowed_types])
                raise TypeError(f"argument '{arg_name}' can only contain instances of {allowed_types}")
    else:
        try:
            isinstance(arg_value, expected_type)
        except TypeError:
            raise TypeError("Invalid type")
        if not isinstance(arg_value, expected_type) or (expected_type is Sequence and isinstance(arg_name, str)):
            raise TypeError(f"argument '{arg_name}' must be an instance of {expected_type.__name__}, got {type(arg_value).__name__} instead")
        

def camel_to_snake(s: str):
    l = list(s)
    for i, char in enumerate(l):
        if (lower_char := char.lower()) != char:
            l[i] = "_" + lower_char if i > 0 else lower_char
    return "".join(l)

def snake_to_camel(s: str):
    l = s.split("_")
    for i, word in enumerate(l):
        if i > 0:
            l[i] = word.capitalize()
    return "".join(l)


