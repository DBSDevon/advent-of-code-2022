def main():
    #my_file = open("input.txt", 'r')
    #data = my_file.readlines()
    #print(data.type())
    temp = 0
    a1 = a2 = a3 = 0
    with open("input.txt","r") as f:
        for line in f:
            if line is not "\n":
                temp += int(line)
                #ans = max(temp,ans)
            else:
                if temp >= a1:
                    a3 = a2
                    a2 = a1
                    a1 = temp
                elif temp >= a2:
                    a3 = a2 
                    a2 = temp
                elif temp >= a3:
                    a3 = temp
                temp = 0
    if temp >= a1:
        a3 = a2
        a2 = a1
        a1 = temp
    elif temp >= a2:
        a3 = a2 
        a2 = temp
    elif temp >= a3:
        a3 = temp

    print(a3+a2+a1)
    #return ans

if __name__ == "__main__":
    main()