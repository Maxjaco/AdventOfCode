def main():

    counter1  = 0 #Solution1
    counter2  = 0 #Solution2

    with open('testData/passwords.txt', 'r') as file:
        for i in file:
            input = i.split(': ')
            password = input[-1]
            validatorTxt = input[0].split(' ')

            occurenceRange = validatorTxt[0].split('-')
            letter = validatorTxt[-1]
            passwordCount = password.count(letter)

            #Solution1
            if passwordCount >= int(occurenceRange[0]) and passwordCount <= int(occurenceRange[1]):
                counter1 += 1

            #Solution2
            passwordPos = [password[int(occurenceRange[0])-1], password[int(occurenceRange[1])-1]]
            if passwordPos.count(letter) == 1:
                counter2 += 1


        print('Solution1: ', counter1)
        print('Solution2: ', counter2)

if __name__ == "__main__":
        main()