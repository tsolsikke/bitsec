from core.py.hash import nosh1, nosh32
from tests.hash_test import test_nosh, test_collisions

if __name__ == "__main__":
    test_nosh(nosh1)
    test_nosh(nosh32)
    test_collisions(nosh1)
    test_collisions(nosh32)
    print("Done")
