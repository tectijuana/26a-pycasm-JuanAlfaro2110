CC = gcc
CFLAGS = -Wall -O2 -fPIC -g
LDFLAGS = -shared

SRC = codigo/bridge.c codigo/ops.s
OUT = build/libops.so

all:
	mkdir -p build
	$(CC) $(CFLAGS) $(SRC) $(LDFLAGS) -o $(OUT)

clean:
	rm -rf build/*
