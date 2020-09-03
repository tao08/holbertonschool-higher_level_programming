#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    barrera = 0
    for i in range(1, len(sys.argv)):
        barrera = int(sys.argv[i]) + barrera
    print("{:d}".format(barrera))
