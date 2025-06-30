keep_running=True
while keep_running==True:
    print('Do you want to do addition, subtraction, multiplication, Or division')
    print('A. addition, S. subtraction, M. multiplication, D. division E. exit' )
    calc_ulator=input('choose ')

    if calc_ulator==("A") or calc_ulator=='a':
        first_num=input('What is the first number? ')
        second_num=input('What is the second number? ')
        print(int(first_num) + int(second_num))

    elif calc_ulator==('S') or calc_ulator=='s':
        first_num=input('What is the first number? ')
        second_num=input('What is the second number? ')
        print(int(first_num) - int(second_num))

    elif calc_ulator==('M') or calc_ulator=='m':
        first_num=input('What is the first number? ')
        second_num=input('What is the second number? ')
        print(int(first_num) * int(second_num))

    elif calc_ulator==('D') or calc_ulator=='d':
        first_num=input('What is the first number? ')
        second_num=input('What is the second number? ')
        print(int(first_num) / int(second_num))

    elif calc_ulator==('E') or calc_ulator=='e':
        print('Have A nice day!!')
        keep_running=False
    else:
        print('Sorry wrong try again')