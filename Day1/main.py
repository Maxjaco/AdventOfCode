from itertools import combinations

def main():

    lines = []
    for s in open("testdata/expenseReport.txt"):
        s = int(s.strip())
        lines.append(s)

    sum1 = 0
    sum2 = 0

    for a in lines:
        for b in lines:
            if (a+b==2020):
                sum1 = a*b
            for c in lines:
                if a+b+c == 2020:
                    sum2 = a*b*c
        
    print(sum1)
    print(sum2)


if __name__ == "__main__":
    main()