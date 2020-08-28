''' This simulates a Merkle Tree, a concept used in Blockchain systems.
    This code generates 1 random string of characters and integers that is split into
    single-character strings. The strings are repeatedly hashed, concatendated, and
    rehashed until a single string remains. This procedure is recursive.
'''


import hashlib
import os
import binascii


def generate_hex(length):  # generates random 16-character string
    x = binascii.b2a_hex(os.urandom(length))
    return list(str(x))[2:-1]  # the string is turned into a list of single-character strings


def rehash(hash1, hash2):  # hashes the concatenation of the two strings/hashes
    h = hashlib.sha256(hash1.encode('utf-8')+hash2.encode('utf-8')).hexdigest()
    return h


def merkle_hash(hashlist):  # hashes a list of strings/hashes into 1 merkle hash

    if len(hashlist) == 1:
        return hashlist[0]

    newhashlist = []
    for x in range(0, len(hashlist)-1, 2):  # will skip last item in list if len is odd
        newhashlist.append(rehash(hashlist[x], hashlist[x+1]))

    if len(hashlist) % 2 == 1:  # hashes the last item to itself
        newhashlist.append(rehash(hashlist[-1], hashlist[-1]))

    return merkle_hash(newhashlist)


stringlist = generate_hex(8)

print(stringlist)

print(merkle_hash(stringlist))


