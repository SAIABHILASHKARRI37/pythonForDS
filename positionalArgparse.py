import argparse
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--number1",help='number')
    parser.add_argument("--number2",help='number')
    parser.add_argument("--operation",help='operation')
    args=parser.parse_args()
    print(args.number1)
    print(args.number2)
    n=int(args.number1)
    n1=int(args.number2)
    if args.operation=='add':
        r=n+n1
        print(r)
    else:
        print('unsupported operation')
    
