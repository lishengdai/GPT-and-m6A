
import random
import sys
import os
import subprocess

# def generate_random_string(n, chars):
#     """Generate a random string of length n with characters from chars."""
#     lst = [''] * n
#     print('dsfgdgskjfas;hj')
#     assert len(lst) == n
#     print('askdfajfasdkjfas;hj')
#     for i in range(n):
#         # print(i, 'sdkjfas;hj')
#         c = random.choice(chars)
#         lst[i] = c
#     print(lst)
#     return ''.join(lst)


def generate_random_string(n, chars):
    """
    Generates a random string of length n with characters from the given character set.
    
    Args:
        n (int): The length of the string to generate.
        chars (str): A string of characters to choose from.
    
    Returns:
        str: A string of length n with randomly chosen characters from the chars set.
    """
    random_string = []
    for i in range(n):
        j = random.randrange(0, len(chars))
        # print(j)
        assert j < len(chars)
        c = chars[j]
        # print("c", c)
        random_string += [c]
    # print(random_string)
    r2 = ''.join(random_string)
    # print("r2:", r2)
    return r2


def test_generate_random_string():
    n = 20
    chars='ACGU'
    seq = generate_random_string(n=n, chars=chars)
    assert len(seq) == n
    for i in range(len(seq)):
        assert seq[i] in chars


def test_generate_random_string2(BINARY='/Users/eckart/programs/ViennaRNA-2.5.1/src/bin/RNAfold'):
    for i in range(100000):
        n = random.randrange(10,50)
        seq = generate_random_string(n=n, chars='ACGU')
        # print(seq)
        tmpout = 'tmp_itsabouttime.txt'
        command = 'echo ' + seq + "|" + BINARY  + ">" + tmpout
        # print(command)
        os.system(command) # os.system(command)
        output = None
        with open(tmpout, "r") as f:
            output = f.read()
        lines = output.split('\n')
        for j in range(len(lines)):
            lines[j] = lines[j].split(' ')[0]
        print('!',lines[0],'?', sep='', end='')
        print('^',lines[1],'$',sep='')
        print()


def run_all_tests():
    test_generate_random_string()
    test_generate_random_string2()


if __name__ == '__main__':
    run_all_tests()

