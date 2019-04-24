def load(raw_string):
    lines = raw_string.split("\n")
    return [
        _parse_line(line) for line in lines
    ]


def store(list_of_maps):
    lines = [
        _print_map(map) for map in list_of_maps
    ]
    return "\n".join(lines)


def _print_map(map):
    return ";".join([
        "{key}={value}".format(key=key, value=value) for key, value in map.items()
    ])


def _parse_line(raw_line):
    result = dict()
    if not raw_line:
        return result

    key_values = raw_line.split(";")

    for key_value in key_values:
        split = key_value.split("=")
        if len(split) != 2:
            raise ValueError("Malformed key-value {}".format(key_value))

        [key, value] = split
        result[key] = value

    return result
