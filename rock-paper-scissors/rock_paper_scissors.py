def main():
    points = 0
    points_dic = {
        "xwin" : 7,
        "xdraw" : 4,
        "xlose": 1,
        "ywin" : 8,
        "ydraw" : 5,
        "ylose": 2,
        "zwin" : 9,
        "zdraw" : 6,
        "zlose": 3
    }
    with open("input.txt", "r") as f:
        for line in f:
            opponent = line[0]
            mine = line[2]
            if opponent == "A":
                if mine == "X":
                    points += 0 + 3
                elif mine == "Y":
                    points += 3 + 1
                elif mine == "Z":
                    points += 6 + 2
            elif opponent == "B":
                if mine == "X":
                    points += 0 + 1
                elif mine == "Y":
                    points += 3 + 2 
                elif mine == "Z":
                    points += 6 + 3
            elif opponent == "C":
                if mine == "X":
                    points += 0 + 2
                elif mine == "Y":
                    points += 3 + 3 
                elif mine == "Z":
                    points += 6 + 1

    print(points)      



if __name__ == "__main__":
    main()
