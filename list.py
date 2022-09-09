if __name__ == '__main__':
    get = int(input())
    lis=[];
    for i in range(0,get):
        cmd=input().split();
        if cmd[0] == "insert":
            lis.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            lis.append(int(cmd[1]))
        elif cmd[0] == "pop":
            lis.pop();
        elif cmd[0] == "print":
            print(lis)
        elif cmd[0] == "remove":
            lis.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            lis.sort();
        else:
            lis.reverse();
