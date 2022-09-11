a = int(input('Введите сумму, которую желаете вывести со счёта.\n'))
k=0
b=100000
i=0
c=1
while k!=6:
    c = a // b
    
    if (c == 1 and (k == 0 or k == 3)):
        print('сто ', end='')
        i=3
    elif (c == 2 and (k == 0 or k == 3)):
        print('двести ', end='')
        i=3
    elif (c == 3 and (k == 0 or k == 3)):
        print('триста ', end='')
        i=3
    elif (c == 4 and (k == 0 or k == 3)):
        print('четыреста ', end='')
        i=3
    elif (c == 5 and (k == 0 or k == 3)):
        print('пятьсот ', end='')
        i=3
    elif (c == 6 and (k == 0 or k == 3)):
        print('шестьсот ', end='')
        i=3
    elif (c == 7 and (k == 0 or k == 3)):
        print('семьсот ', end='')
        i=3
    elif (c == 8 and (k == 0 or k == 3)):
        print('восемьсот ', end='')
        i=3
    elif (c == 9 and (k == 0 or k == 3)):
        print('девятьсот ', end='')
        i=3

    if (c == 1 and (k == 1 or k == 4)):
        i=4
    elif (c == 2 and (k == 1 or k == 4)):
        print('двадцать ', end='')
        i=3
    elif (c == 3 and (k == 1 or k == 4)):
        print('тридцать ', end='')
        i=3
    elif (c == 4 and (k == 1 or k == 4)):
        print('сорок ', end='')
        i=3
    elif (c == 5 and (k == 1 or k == 4)):
        print('пятьдесят ', end='')
        i=3
    elif (c == 6 and (k == 1 or k == 4)):
        print('шестьдесят ', end='')
        i=3
    elif (c == 7 and (k == 1 or k == 4)):
        print('семьдесят ', end='')
        i=3
    elif (c == 8 and (k == 1 or k == 4)):
        print('восемьдесят ', end='')
        i=3
    elif (c == 9 and (k == 1 or k == 4)):
        print('девяносто ', end='')
        i=3

    if (c == 1 and k == 2 and i!=4):
        print('одна ', end='')
        i=1
    elif (c == 1 and k == 5 and i!=4):
        print('один ', end='')
        i=1
    elif (c == 2 and k == 2 and i!=4):
        print('две ', end='')
        i=2
    elif (c == 2 and k == 5 and i!=4):
        print('два ', end='')
        i=2
    elif (c == 3 and (k == 2 or k == 5)and i!=4):
        print('три ', end='')
        i=2
    elif (c == 4 and (k == 2 or k == 5)and i!=4):
        print('четыре ', end='')
        i=2
    elif (c == 5 and (k == 2 or k == 5)and i!=4):
        print('пять ', end='')
        i=3
    elif (c == 6 and (k == 2 or k == 5)and i!=4):
        print('шесть ', end='')
        i=3
    elif (c == 7 and (k == 2 or k == 5)and i!=4):
        print('семь ', end='')
        i=3
    elif (c == 8 and (k == 2 or k == 5)and i!=4):
        print('восемь ', end='')
        i=3
    elif (c == 9 and (k == 2 or k == 5) and i!=4):
        print('девять ', end='')
        i=3
    elif (i==4 and (k==2 or k==5)):
        if (c == 1):
            print('одинадцать ', end='')
            i=3
        elif (c == 2):
            print('двенадцать ', end='')
            i=3
        elif (c == 3):
            print('тринадцать ', end='')
            i=3
        elif (c == 4):
            print('четырнадцать ', end='')
            i=3
        elif (c == 5):
            print('пятнадцать ', end='')
            i=3 
        elif (c == 6):
            print('шестнадцать ', end='')
            i=3
        elif (c == 7):
            print('семьнадцать ', end='')
            i=3
        elif (c == 8):
            print('восемьнадцать ', end='')
            i=3
        elif (c == 9):
            print('девятнадцать ', end='')
            i=3
        elif (c == 0):
            print('десять ', end='')
            i=3
    
    if (k == 5):
        if (i==1):
            print('рубль')
        elif (i==2):
            print('рубля')
        elif (i==3):
            print('рублей')

    if (k == 2):
        if (i==1):
            print('тысяча ', end='')
            i=3
        elif (i==2):
            print('тысячи ', end='')
            i=3
        elif (i==3):
            print('тысяч ', end='')
            i=3

    a=a-(c*b)    
    b = b / 10        
    k=k+1
