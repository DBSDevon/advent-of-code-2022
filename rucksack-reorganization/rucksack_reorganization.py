def part1():
    priority = {}
    points = 0
    with open("input.txt", "r") as f:
        for line in f:
            length = len(line)
            midpoint = length//2
            first_ruck = line[:midpoint]
            second_ruck = line[midpoint:]
            
            temp = set()
            for char in first_ruck:
                temp.add(char)
            for char in second_ruck:
                if char in temp:
                    if char.isupper():
                        points += ord(char) - 38
                    else:
                        points += ord(char) - 96
                    break
    
    print(points)

def part2():
    points = 0
    input = [line.rstrip() for line in open("input.txt", "r")] 
    i = 0
    while(i < len(input)):
        first_ruck = input[i]
        second_ruck = input[i+1]
        third_ruck = input[i+2]
        temp=set()
        temp1=set()
        print(first_ruck)
        print(second_ruck)
        print(third_ruck)
        i += 3
        for char in first_ruck:
            temp.add(char)
        for char in second_ruck:
            if char in temp:
                temp1.add(char)
        for char in third_ruck:
            if char in temp1:
                if char.isupper():
                    points += ord(char) - 38
                else:
                    points += ord(char) - 96
                break
    print(points)

def main():
    part2()


if __name__ == "__main__":
    main()
