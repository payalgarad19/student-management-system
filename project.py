from datetime import date
db={101:{'name':'Payal Garad','city':'pune','course':'python','t_fee':4000,'p_fee':2000,'r_fee':2000,'add_date':'20/05/2025'}}
course_fees={'python':4000,'java':5000,'aws':3000}

print('-'*100)
print('TheKiranAcademy'.center(100,' '))
print('-'*100)
while True:
    print('''
    1.Add Student Details
    2.Display Student Details
    3.Update Student Details
    4.Delete Student Details
    5.Filter
    6.Exit
    ''')
    ch=int(input("enter your choice: "))
    if ch==1:
        name=input("enter student name: ")
        city=input("enter city name: ")
        course=input("enter course name: ")
        dis=eval(input("enter discount in per: "))
        t_fee=course_fees[course]-course_fees[course]*dis/100
        print("your fee:",t_fee)
        p_fee=eval(input("enter fee amount: "))
        r_fee=t_fee-p_fee
        r_no=101+len(db)
        #var[key]=value
        db[r_no]={'name':name,'city':city,'course':course,'t_fee':t_fee,'p_fee':p_fee,'r_fee':r_fee,'add_date':str(date.today())}
       

    elif ch==2:
        print('-'*117)
        print('|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|'.format('Reg','Name','City','Course','T_fee','P_fee','R_fee','Date'))
        print('-'*117)
        for reg in db:
            print('|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['course'],db[reg]['t_fee'],db[reg]['p_fee'],db[reg]['r_fee'],db[reg]['add_date']))
            print('-'*117)

    elif ch==3:
        reg=eval(input("enter reg: "))
        print('''
            1.course
            2.fee
        ''')
        ch=int(input("enter your choice: "))
        if ch==1:
            u_course=input("enter course name: ")
            #var[key]=uvalue
            db[reg]['course']=u_course
            print("done")
        elif ch==2:
            print('your r_fee is',db[reg]['r_fee'])
            amount=eval(input("enter amount: "))
            db[reg]['p_fee']=db[reg]['p_fee']+amount
            db[reg]['r_fee']=db[reg]['r_fee']-amount
            print('your r_fee is',db[reg]['r_fee'])
            print("done")

        else:
            print('invalid input...')
    elif ch==4:
        reg=eval(input("enter reg no: "))
        db.pop(reg)
        print('done')
        

    elif ch==5:
        print('''
        1.course
        2.city
    ''')
        ch=eval(input("enter your choice: "))
        if ch==1:
            course=input("course: ")
            print('|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|'.format('Reg','Name','City','Course','T_fee','P_fee','R_fee','Date'))
            print('-'*117)
            for reg in db:
                if db[reg]['course']==course:
                    print('|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['course'],db[reg]['t_fee'],db[reg]['p_fee'],db[reg]['r_fee'],db[reg]['add_date']))
                    print('-'*117)
        elif ch==2:
            pass
        else:
            print('invalid input...')
    elif ch==6:
            break
    else:
           print('invalid input plz enter the valid input......')
    
