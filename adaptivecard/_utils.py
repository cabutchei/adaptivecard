from json import dump


def raise_invalid_pixel_error(arg_name: str, arg_value: str):
    msg = f"argument '{arg_name}' must be numeric or a number ending with 'px', got '{arg_value}' instead"
    raise ValueError(msg)


def convert_to_pixel_string(s):
    if isinstance(s, str):
        if not s.replace('px', '').isdecimal():
            raise ValueError
        s = s.replace('px', '') + 'px'
    elif isinstance(s, int):
        s = str(s) + 'px'
    return s


def camel_to_snake(s: str):
    l = list(s)
    for i, char in enumerate(l):
        if (lower_char := char.lower()) != char:
            l[i] = "_" + lower_char if i > 0 else lower_char
    return "".join(l)

def snake_to_camel(s: str):
    """Returns a snake-cased version of the string."""
    l = s.split("_")
    for i, word in enumerate(l):
        if i > 0:
            l[i] = word.capitalize()
    return "".join(l)


def get_schema_path(definition: dict):
    if "anyOf" in definition:
        for x in definition["anyOf"]:
            p = get_schema_path(x)
            if p is not None:
                return p
    elif "properties" in definition:
        return definition["properties"]


def save_json(path: str, obj: dict, indent: int = 4):
    if not isinstance(indent, int):
        raise TypeError
    with open(path, 'w') as f:
        dump(obj, f, indent=indent)
