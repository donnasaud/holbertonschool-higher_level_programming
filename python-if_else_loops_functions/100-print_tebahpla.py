#!/usr/bin/python3
print("{}".format("".join(
    chr(i) if i % 2 == 1 else chr(i + 32)
    for i in range(90, 64, -1)
)), end="")
