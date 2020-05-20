import sys
'''
This module accepts the given sum and sequence of numbers from command separated by
space and outputs the corresponding pairs into console
'''

def pairs(sum, *args):
    for i in range(len(args)):
        for j in range(i+1,len(args)):
            if int(args[i]) + int(args[j]) == int(sum):
                print(f'{args[i]} + {args[j]}')

# main block
if __name__ == '__main__':
    if (sys.argv[1:]):
        pairs(*sys.argv[1:])
    else:
        arguments = (input("Please enter sum and sequence of numbers separated by space:")).split(" ")
        pairs(*arguments)