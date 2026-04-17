CC = gcc
CFLAGS = -fPIC -O2 -Wall -g
LDFLAGS = -shared

TARGET = build/libops.so

all: $(TARGET)

$(TARGET): bridge.o ops.o
	$(CC) $(LDFLAGS) -o $@ $^

bridge.o: bridge.c
	$(CC) $(CFLAGS) -c bridge.c

ops.o: ops.s
	$(CC) $(CFLAGS) -c ops.s

clean:
	rm -f *.o $(TARGET)