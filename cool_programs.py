name = input("enter your name :")

print("\nhey! whatsup ", name, "?\n")

select_program = (input('''what u wanna do now .. select from this[enter number before the program]\n
1.open calculator
2.calculate discount
3.fun_status
4.calculate the power of i [iota] 
5.calculate age and see how many months/weeks/days...you lived! \n'''))

if select_program == "1":
    num_1 = float(input("enter first number :\n"))
    operator = input("enter operator [+],[-],[*],[/] :\n")
    num_2 = float(input("enter second number :\n"))

    if operator == '+':
       print("ans is :", num_1+num_2)

    elif operator == '-':
      print("ans is :", num_1-num_2)

    elif operator == '*':
      print("ans is :", num_1*num_2)

    elif operator == '/':
      print("ans is :", num_1/num_2)

    else:
      print("invalid operator!   \n\t select only from this :  [+],[-],[*],[/]")
    
elif select_program=="2":
    price=float(input("enter the actual price :"))

    discount=float(input("enter the discount[%] :"))

    print("you final price will be :", (price-((discount/100)*price)))

elif select_program=="3":
    

    print("hello! " , name ,"how are you ?\n")
    status=str(input("fine,sad,depressed,happy,angry :"))

    if status=="fine":
       print("you are doing great ",name ,"  keep it up!\n")

    elif status=="sad": 
        print("dont worry! ",name ,"  it will be fine soon!\n")

    elif status=="depressed":
        print("dont be depressed ",name," .....everything will be fine!\n")

    elif status=="happy":
        print("glad to hear ",name, " .......be happy always!\n")

    elif status=="angry":
        print("cool down! ",name, " ....spit anger and try to find solution!\n")

    else:
        print(" Thats invalid status! ",name," .....Please enter only from this [fine,sad,depressed,happy,angry] \n") 

elif select_program=="4":
    iota=int(input("enter power of iota[i^?] : \n"))

    p = iota % 4

    if p==0:
      print("Ans is : 1\n")

    elif p==1:
       print("Ans is : i\n")

    elif p==2:
      print("Ans is : -1\n")

    elif p==3:
       print("Ans is : -i\n")  

elif select_program=="5":
  dob=int(input("enter your birth year [yyyyy]  :"))
  current_year=int(input("\nenter the current year [yyyy] :"))
  age=current_year-dob
  print("\nyour current age is :",age)

  print("you lived about ",age*12," months [approx]")
  print("you lived about ",age*12*4," weeks [approx]")
  print("you lived about ",age*12*30," days [approx]")
  print("you lived about ",age*12*30*24," hours [approx]")
  print("you lived about ",age*12*30*24*60," minutes [approx]")
  print("you lived about ",age*12*30*24*60*60," seconds [approx]")
  print("you lived about ",age*12*30*24*60*60*1000," milliseconds [approx]")
  print("\nfun fact :  you could have travelled from earth to sun and back ",33692*age,"times. \nif your speed=speed of light")


else:
    print('''you have entered invalid program!.....be sure to select only from this
    1.open calculator
    2.calculate discount
    3.fun_status
    4.calculate the power of i [iota]
    5.calculate age and see how many months/weeks/days...you lived!
    Run THE PROGRAM FROM STARING...!''')



exit=input()