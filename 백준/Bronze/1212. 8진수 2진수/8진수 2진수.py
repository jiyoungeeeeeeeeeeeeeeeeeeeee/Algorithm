import sys

octal = sys.stdin.readline().strip()
binary = ''.join(bin(int(d))[2:].zfill(3) for d in octal)
print(binary.lstrip('0') or '0')
