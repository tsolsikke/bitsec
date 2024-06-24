import ctypes
import os

# ライブラリのパスを設定
lib_path = os.path.join(os.path.dirname(__file__), '..', 'cpp', 'libfuncs.so')

# ライブラリを読み込む
lib = ctypes.CDLL(lib_path)

# C関数の引数と戻り値の型を指定
lib.Func_001.argtypes = [ctypes.c_int, ctypes.c_int]
lib.Func_001.restype = ctypes.c_int

lib.Func_002.argtypes = [ctypes.c_char_p]
lib.Func_002.restype = None


def func_001(val1, val2):
    return lib.Func_001(val1, val2)


def func_002(msg):
    lib.Func_002(msg.encode('utf-8'))
