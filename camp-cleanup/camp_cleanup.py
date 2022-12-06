import re

def fullycontained(first_start, first_end, second_start, second_end):

    if first_start >= second_start and first_end<= second_end:
        #print("Second is contained in first")
        return 1
    elif second_start >= first_start and second_end <= first_end:
        #print("First is contained in second")
        return 1
    else:
        return 0

def overlap(first_start, first_end, second_start, second_end):
    if second_start >= first_start and second_start <= first_end:
        print("a")
        return 1
    elif second_end>= first_start and second_start <= first_end:
        print("b")
        return 1
    elif first_start >= second_start and first_start <= second_end:
        print("c")
        return 1
    elif first_end >= second_start and first_end <= second_end:
        print("d")
        return 1
    else:
        return 0
def part1():
    input = [line.rstrip() for line in open("example_input.txt", "r")]
    overlap = 0
    #print(len(input))
    #print(input)
    for line in input:
        a = re.split(r',|-',  line)
        print(a)
        f_start =int(a[0])
        f_end = int(a[1])
        s_start = int(a[2])
        s_end = int(a[3])
        overlap += fullycontained(f_start, f_end, s_start, s_end)
    print(overlap)
    return(overlap)

def part2():
    input = [line.rstrip() for line in open("input.txt", "r")]
    ans = 0
    #print(len(input))
    #print(input)
    for line in input:
        a = re.split(r',|-',  line)
        f_start =int(a[0])
        f_end = int(a[1])
        s_start = int(a[2])
        s_end = int(a[3])
        ans += overlap(f_start, f_end, s_start, s_end)
    print(ans)
    return(ans)


def main():
    part2()
if __name__ == "__main__":
    main()

    