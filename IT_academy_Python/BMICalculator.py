# ввод данных

input_data = False
while input_data==False: 
 try:
  a = int(input("Enter your height in cm: "))
  b = int(input("Enter your weight in kg: "))
  input_data=True
 except ValueError:
    print ("Only whole numbers, without literal or decimals.")
    input_data=False

## пользователь вводит некорректные данные, вводим ограничения по весу и росту для взрослого человека, нижнюю границу не обозначаем
# для инклюзивности
i=0
if a>251 or b>635: 
    i+=1
    while i<3: 
          a = int(input("Let's try again.Your height in cm: "))
          b = int(input("Let's try again. Your weight in kg: "))
          i=i+1
          if i>=3:
              print ("Are youe kidding me?")
              index_bmi=0
              break
else: 
     a=a
     b=b
     index_bmi=int(round(b/(a/100)**2,0))

# рисуем шкалу

scale_size=37
left_limit=13
right_limit=50

if index_bmi in range(left_limit,right_limit): 
    left_interval=(index_bmi-left_limit-1)
    right_interval=(scale_size-left_interval-2)
    print (str(left_limit)+'='*left_interval+'|'+'='*right_interval+str(right_limit))
    if index_bmi in range(left_limit, 18):
       print("Your BMI index is "+str(index_bmi)+" and you are in the underweight range")
    elif index_bmi in range(18, 25):
          print("Your BMI index is "+str(index_bmi)+" and you are in the healthy weight range")
    elif index_bmi in range(25, 30):
          print("Your BMI index is "+str(index_bmi)+" and you are in the overweight range")
    elif index_bmi in range(30, 40):
          print("Your BMI index is "+str(index_bmi)+" and you are in the obese range")
   
elif index_bmi ==0: 
     print("I'm tired of you")
else: 
     print("You are propably dead")
     
   




