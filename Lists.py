if __name__ == '__main__':
    N = int(raw_input())
    output=[]
    for i in range(0,N):
        al= raw_input().split()
        if al[0]=="print":
            print(output)
        elif al[0]=="insert":
            output.insert(int(al[1]),int(al[2]))  
        elif al[0]=="remove":
            output.remove(int(al[1]))
        elif al[0]=="append":
            output.append(int(al[1]))
        elif al[0]=="sort":
            output.sort()
        elif al[0]=="reverse":
            output.reverse()
        else:
            output.pop()

            
            
            
            
