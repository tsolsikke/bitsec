CC = gcc
CFLAGS = -shared -fPIC -o libfuncs.so

all: funcs

funcs: funcs.cpp funcs.h
	$(CC) $(CFLAGS) funcs.cpp -o libfuncs.so
