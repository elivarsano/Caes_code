def caes():
    low_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    up_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    pw = input('Enter a password using letters: \n')
    enc = int(input('Enter a number of times to jump to an encrypted letter: \n'))
    direction = input('Enter the enc direction ("R" for right and "L" for left): \n')
    fin_pw = []
    for c in pw:
        if c.islower():
            for n in low_case:
                if c == n:
                    if direction == 'L':
                        fin_pw.append(low_case[low_case.index(n) - enc])
                    elif direction == 'R':
                        fin_pw.append(low_case[low_case.index(n) + enc])
        elif c.isupper():
            for n in up_case:
                if c == n:
                    if direction == 'L':
                        fin_pw.append(up_case.index(n) - enc)
                    elif direction == 'R':
                        fin_pw.append(low_case.index(n) + enc)

    return ''.join(fin_pw)


print(caes())
