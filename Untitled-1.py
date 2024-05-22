#Jerry's code Q3
count=512
count_list=[512]
Zero=0
#loop
while True:
    try:
        robot=int(input('Enter your input: '))
        if count < robot:
            count_list.append('beep')
        elif count>=robot:
           count_list.append('boop')
        elif count < Zero:
            break
        else:
            count_list.append(count)
    except ValueError:
      print('This is no a valid number.')
#printout
for i in count_list:
    print(i)



   



    

