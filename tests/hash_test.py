test_strings = [
    "hello",
    "world",
    "Hello",
    "HELLO",
    "world",
    "hash",
    "function",
    "simple",
    "example",
    "test",
    "another test",
    "123456",
    "abcdef",
    "a",
    "b",
    "c",
    "d"
]


def test_nosh(hash_func):
    print(f"Testing {hash_func.__name__}")
    for s in test_strings:
        print(f"Input: {s}, Output: {hash_func(s)}")
    print('------------------------')


def test_collisions(hash_func):
    print(f"Testing collisions by {hash_func.__name__}")
    hash_set = set()
    for s in test_strings:
        hash_value = hash_func(s)
        if hash_value in hash_set:
            print(f"Collision found for {s}")
            print(f"Collision detected for input '{s}' with hash {hash_value}")
        else:
            hash_set.add(hash_value)
    print('------------------------')

