# Repeating-key XOR

# We have been given a key, each of whose letters have to be xorred against corresponding
# characters of the given string, and the key has to be repeated until it's length equals len(string).

from pwn import xor
key = b'FIRE'
string = bytearray.fromhex("011a111100326133753b2b722e783c22192a662b192b611a347a2276723d61212a300d3d763b2076221627707727351a72272b722e783c223b")

print(xor(key,string).decode())
