# Что должен делать
#Запрашиваем рост/вес
#Считать BMI по введенным параметрам
#Выводить результат в виде текста - Ваш индекс массы тела: <результат расчета>
#Выводить результат в виде шкалы: Пример: Если результат 30
#20======|============50
#Если 40
#20=====
#from decimal import Decimal

input_data = False
while input_data==False: 
 try:
  a = int(input("Введите ваш рост в сантиметрах: "))
  b = int(input("Введите ваш вес в килограммах: "))
  input_data=True
 except ValueError:
    print ("Only whole numbers, without literal or decimals.")
    input_data=False

# пользователь вводит абышто
if a<1 or a>210 or b<35 or b>400: 
    a = int(input("Попробуйте еще раз. Ваш рост в сантиметрах:  "))
    b = int(input("Попробуйте еще раз. Ваш вес в килограммах:  "))
else: 
     a=a
     b=b

index_bmi=int(b/(a/100)**2)
#index_bmi= round(Decimal(b/(a/100)**2),0) 

scale_size=37
left_limit=13
right_limit=50

if index_bmi in range(left_limit,right_limit): 
    left_interval=(index_bmi-left_limit-1)
    right_interval=(scale_size-left_interval-2)
    print (str(left_limit)+'='*left_interval+'|'+'='*right_interval+str(right_limit))
else: 
     print("You are propably dead")

if index_bmi in range(left_limit, 18):
       print("Your BMI index is "+str(index_bmi)+" and you are in the underweight range")
elif index_bmi in range(18, 25):
          print("Your BMI index is "+str(index_bmi)+" and you are in the healthy weight range")
elif index_bmi in range(25, 30):
          print("Your BMI index is "+str(index_bmi)+" and you are in the overweight range")
elif index_bmi in range(30, 40):
          print("Your BMI index is "+str(index_bmi)+" and you are in the obese range")
else: 
         print("You are propably dead")


