# cool_programs
name = input("enter your name :")

print("\nhey! whatsup ", name, "?\n")

print('''\nwhat u wanna do now .. select from this[enter number before the program]\n
1 -> open calculator
2 -> calculate discount
3 -> fun_status
4 -> calculate the power of i [iota] 
5 -> calculate age and see how many months/weeks/days...you lived! 
6 -> guess the symbol/alphabet \n''')

select_program=input("Enter the program number from above : ")

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
  print("\nfun fact : \n\nyou could have travelled from earth to sun and back ",33692*age,"times. \nif your speed=speed of light")

elif select_program=="6":
  print("think of any 2 digit number\n")
  print('''for example : if the number is 36 ,add 3+6 which is 9 ,
  now subsctract from the original number ie 36-9=27,
  now search for the symbol/alphabet after 27''')

  enter=input("after thinking and getting number press enter ")

  print('''99	O	98	i	97	h	96	a	95	T	94	i	93	x	92	N	91	R	90	v
  89	o	88	J	87	6	86	U	85	v	84	I	83	z	82	R	81	m	80	d
  79	u	78	{	77	T	76	d	75	v	74	S	73	S	72	m	71	I	70	{
  69	n	68	J	67	i	66	v	65	6	64	U	63	m	62	b	61	R	60	O
  59	J	58	b	57	l	56	h	55	u	54	m	53	m	52	l	51	b	50	6
  49	z	48	S	47	{	46	o	45	m	44	U	43	x	42	f	41	T	40	{
  39	S	38	T	37	_	36	m	35	O	34	6	33	d	32	O	31	o	30	I
  9	x	28	I	27	m	26	z	25	n	24	^	23	d	22	b	21	b	20	^
  19	z	18	m	17	I	16	m	15	S	14	h	13	n	12	m	11	n	10	z
  9	m	8	S	7	b	6	m	5	U	4	h	3	x	2	b	1	S	0	m''')


  guess=input("press enter and see your symbol/alphabet :")
  print("\tyour symbol is 'm'\n")

  print("\n\twant to to repeat! ?")
  enter_2=input("press enter to run again")

  print('''99	m	98	o	97	b	96	^	95	S	94	N	93	x	92	M	91	v	90	m
  89	I	88	l	87	o	86	i	85	N	84	M	83	d	82	S	81	b	80	u
  79	6	78	T	77	R	76	n	75	x	74	d	73	R	72	b	71	N	70	m
  69	R	68	U	67	o	66	J	65	U	64	_	63	b	62	{	61	b	60	b
  59	d	58	R	57	I	56	R	55	T	54	b	53	N	52	6	51	n	50	m
  49	b	48	^	47	_	46	i	45	b	44	M	43	_	42	n	41	x	40	{
  39	h	38	x	37	i	36	b	35	S	34	f	33	S	32	h	31	d	30	f
  29	v	28	U	27	b	26	T	25	I	24	f	23	N	22	J	21	i	20	v
  19	d	18	b	17	6	16	a	15	z	14	l	13	f	12	U	11	O	10	u
  9	b	8	M	7	{	6	x	5	R	4	O	3	{	2	J	1	6	0	b
  ''')

  enter_2=input("press enter to get your symbol/alphabet:\n")
  print("\n\tyour symbol/alphabet was 'b' \n")


  print("\tTHANKS FOR PLAYING!,HAVE FUN!")

else:
    print('''you have entered invalid program!.....be sure to select only from this
    1.open calculator
    2.calculate discount
    3.fun_status
    4.calculate the power of i [iota]
    5.calculate age and see how many months/weeks/days...you lived!
    6.guess the symbol/alphabet
    Run THE PROGRAM FROM STARING...!''')

exit=input()
