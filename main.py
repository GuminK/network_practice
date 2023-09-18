'''
# 1번문제


weight = float(input("몸무게를 입력해 주세요 : "))
height = float(input("자신의 키를 입력해 주세요 : "))
BMI = weight/(height*height)

print("BMI 지수 :",BMI)


'''

'''
# 2번 문제

assignment=int(input("과제 : "))
middle=int(input("중간 : "))
final=int(input("기말 : "))
avg = (assignment+middle+final)/3
print("평균 :",avg)
if avg>=90:
    print("A학점 입니다.")
elif avg>=80:
    print("B학점 입니다.")
elif avg>=70:
    print("C학점 입니다.")
elif avg>=60:
    print("D학점 입니다.")
else :
    print("F학점 입니다.")



'''
'''
# 3번 문제

print("for 연습")
print("1.☆\n2.★\n3.#")
mod = input("모드를 선택 하시오 : ")
length = int(input("길이를 입력 하시오 : "))

if mod == '1':
    # ☆ 모양
    print("빈별모양")
    for i in range(length, 0, -1):

        # 앞의 공백

        print("  " * (length), end='')

        print(" " * i, end='')

        # 첫 번째 별

        print("☆", end='')

        # 별 사이의 공백

        if i != length:
            print("  " * (length - i - 1), end='')

            print("☆", end='')

        print()

    for i in range(length // 2 + length % 2):

        print(" " * (length - length // 2), end='')

        if i == 0:

            print("☆" * length, end='')

            print("  " * (length - (length - 3) // 2), end='')

            print("☆" * length, end='')

        else:

            print(" " * ((length // 2 - 1) + i), "☆", " " * ((length // 2 + 1) - i), end='')

            print(" " * (length * 2 - 1), end='')

            print(" " * ((length // 2 + 1) - i), "☆", end='')

        print()

    margin = 0

    for i in range(length, 0, -1):

        print(" " * (length - length // 2), end='')

        print(" " * i, '☆', end='')

        if i != 0:

            if i > 2:

                print(" " * (i - 2), '☆', end='')

            elif i == 1:

                print('', end='')

            else:

                print('☆', end='')

        if i != 0:

            if i == length:

                print(" " * (i - 2), '☆', end='')

            elif i == length - 1:

                print(" " * 1 * 2, end='☆')

            else:

                # print(length-i,end='')

                print(" " * (6 * (length - i - 1) + margin), end='☆')

                margin -= (length - i - 2)

        if i != 0:

            if i == length:
                print()

                continue

            if i > 2:

                print(" " * (i - 2), '☆', end='')

            elif i == 1:

                print('', end='')

            else:

                print('☆', end='')

        print()


elif mod == '2':
    # ★ 모양
    print("꽉찬별모양")
    for i in range(length, 0, -1):

        # 앞의 공백

        print("  " * (length), end='')

        print(" " * i, end='')

        # 첫 번째 별

        print("★", end='')

        # 별 사이의 공백

        if i != length:
            print("★" * (length - i - 1), end='')

            print("★", end='')

        print()

    for i in range(length // 2 + length % 2):

        print(" " * (length - length // 2), end='')

        if i == 0:

            print("★" * length, end='')

            print("★ " * (length - (length - 3) // 2), end='')

            print("★" * length, end='')

        else:

            print(" " * ((length // 2 - 1) + i), "★", " " * ((length // 2 + 1) - i), end='')

            print(" " * (length * 2 - 1), end='')

            print(" " * ((length // 2 + 1) - i), "★", end='')

        print()

    margin = 0

    for i in range(length, 0, -1):

        print(" " * (length - length // 2), end='')

        print(" " * i, '★', end='')

        if i != 0:

            if i > 2:

                print("★" * (i - 2), '★', end='')

            elif i == 1:

                print('', end='')

            else:

                print('★', end='')

        if i != 0:

            if i == length:

                print(" " * (i - 2), '★', end='')

            elif i == length - 1:

                print(" " * 1 * 2, end='★')

            else:

                # print(length-i,end='')

                print(" " * (6 * (length - i - 1) + margin), end='★')

                margin -= (length - i - 2)

        if i != 0:

            if i == length:
                print()

                continue

            if i > 2:

                print(" " * (i - 2), '★', end='')

            elif i == 1:

                print('', end='')

            else:

                print('★', end='')

        print()

elif mod == '3':
    # # 모양
    print("# 모양")
    for i in range(1,length+1):
        if 1 <= i % 2:
            print("  " * (length-i), end='')
            print("#    #", end='')

            print("")
        else :
            print("##" * (length+2))





else :
    print("잘못 입력했음")



'''


# 4번 문제

# list-for
listA = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
listB = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
listC = []
countA = 0
countB = 0
temp = 0
countS = 1
for i in range(0, 20):
    if countA < 10:
        temp = 0
        while temp < countS:
            listC.append(listA[countA])
            countA = countA+1
            i = i+1
            temp = temp+1
    if countB < 10:
        temp = 0
        while temp < countS:
            listC.append(listB[countB])
            countB = countB+1
            i = i+1
            temp = temp+1
        countS = countS + 1
print("listA = ", listA)
print("listB = ", listB)
print("listC = ", listC)


