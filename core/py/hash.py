
def nosh1(input_string):
    hash_value = 0

    for char in input_string:
        hash_value += ord(char)
        hash_value = (hash_value * 31) % 1024

    return hash_value


def nosh32(input_string):
    hash_value = 0x811c9dc5  # by FNV-1a

    for char in input_string:
        hash_value ^= ord(char)
        hash_value = (hash_value * 16777619) & 0xffffffff

    return hash_value
