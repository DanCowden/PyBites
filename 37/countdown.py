"""
countdown_for function produces output:
10
9
8
7
6
5
4
3
2
1
time is up

Mimic the same output using recursion
"""

def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    if start == 0:
        print('time is up')
    else:
        print(start)
        countdown_recursive(start - 1)


if __name__ == '__main__':

    countdown_for()

    countdown_recursive()
