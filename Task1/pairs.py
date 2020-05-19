import sys
def pairs(sum, *args):
    for i in range(len(args)):
        for j in range(i+1,len(args)):
            if int(args[i]) + int(args[j]) == int(sum):
                print(f'{args[i]} + {args[j]}')

# main block
def main():
    pairs(*sys.argv[1:])
    
if __name__ == '__main__':
    main()