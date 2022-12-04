from enum import Enum


def startwith(s: str, f: Enum) -> str:
    return f"{f.value}{s}"
