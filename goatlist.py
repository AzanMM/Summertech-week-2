goatlist=[]
while True:
    print('WELCOME THIS IS THE GOAT LIST WHAT DO U WANT TO DO')
    user_input=input('1. add 2. remove 3. replace 4. get position 5. quit ' )
    if user_input==('1'):
        goat=input('Who is the G.O.A.T ')
        goatlist.append(goat)
        print(goatlist) 
        #This is the add 
    elif user_input=='2':
        ngoat=input('Who do u want to remove ')
        goatlist.remove(ngoat)
        print(goatlist)
        #This is remove
    elif user_input=='3':
        rgoat=input('Who do u want to replace ')
        wgoat=input('Who do u want to add in there place ')
        goatlist.remove(rgoat)
        goatlist.append(wgoat)
        print(goatlist)
        #This is replace
    elif user_input=='4':
        position=input('What player/s position do u wanna get ')
        print(goatlist.index(position))
        #This is get position
    elif user_input=='5':
        print('Thankyou for playing;]')
        print(goatlist)
        break
        #This is quit
