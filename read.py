f=open('c://vscode//abi.txt','r')
for i in f:
    tokens=i.split("  ")
print(len(tokens))

f.close()
