#!/usr/bin/python3
def remove_char_at(string, n):
    result = list(string)
    if n < len(result) and n > -1:
        del result[n]
    else:
        pass
    return "".join(map(str, result))
