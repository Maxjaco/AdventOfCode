from itertools import combinations

def main():

    lines = []
    for s in open("Day1/testdata/expenseReport.txt"):
        s = int(s.strip())
        lines.append(s)

    sum1 = 0
    sum2 = 0

    for a in lines:
        for b in lines:
            #Part1
            if (a+b==2020):
                sum1 = a*b
            #Part2
            for c in lines:
                if a+b+c == 2020:
                    sum2 = a*b*c
    
    #Solution1
    print('Solution1: ', sum1)
    #Solution1
    print('Solution2: ', sum2)


if __name__ == "__main__":
    main()