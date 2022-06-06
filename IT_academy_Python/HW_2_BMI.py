import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#ввод данных
input_data = False
while input_data==False: 
    try:
        a = int(input("Enter your height in cm: "))
        b = int(input("Enter your weight in kg: "))
        c = int(input("Enter your age in years: "))
        d = str(input("Chose your name from the list: male, female, other: "))
        input_data=True
    except ValueError:
         print ("For height, weight and age you should enter only whole numbers, without literal or decimals.n\ For gender just enter 'male', 'female' or 'other'")
         input_data=False

##в зависимости от пола подгружаем разные дата сеты  (один для женщин и прочих полов и один для мужчин.) 
#Дата сеты примерные, соблюдая общие очертания, найти точные не удалось. 

def draw_plot (df):
    
    #строим stacked areas plot

    headers =df.columns.tolist()
    col=tuple(headers)
    plt.rcParams["figure.figsize"] = [14.00, 7]
    plt.rcParams["figure.autolayout"] = True
    age = df['YEAR'].tolist()
        
    bmi_index = {
         col[7]: df['severe underweight'].tolist(),
         col[6]: df['strong underweight'].tolist(),
         col[5]: df['underweight'].tolist(),
         col[4]: df['normal'].tolist(),
         col[3]: df['overweight'].tolist(),
         col[2]: df['strong overweight'].tolist(),
         col[1]: df['severe overweight'].tolist()
        }

    fig, ax = plt.subplots()
    ax.stackplot(age, bmi_index.values(),
             labels=bmi_index.keys(), alpha=0.8)
    ax.legend(loc='upper left')
    
    if d =='female' or d == 'other':
        ax.set_title('BMI Index for females and other genders')
    else:
         ax.set_title('BMI Index for males')
    
    ax.set_xlabel('Age')
    ax.set_ylabel('BMI Index')
    return fig, ax, df
    
def bmi_point(a, b,c):
    index_bmi=int(round(b/(a/100)**2,0))
    pnt=plt.plot(c,index_bmi, marker=(5, 1), color = 'white')
    plt.text(c,(index_bmi+2),'Your BMI Index',rotation=0, color = 'white' )
    return pnt, index_bmi

# определяем величину индекса, соотносим ее с реферальными значениями и даем рекомендации

def diagnose (a, b,c,d, df): 
    index_bmi=int(round(b/(a/100)**2,0))
    left_limit=0
    right_limit=50
    severe_underweight=int(df['severe underweight'].values[c])
    strong_underweight=severe_underweight+int(df['strong underweight'].values[c])
    underweight=strong_underweight+int(df['underweight'].values[c])
    normal=underweight+int(df['normal'].values[c])
    overweight=normal+int(df['overweight'].values[c])
    strong_overweight=overweight +int(df['strong overweight'].values[c])
    severe_overweight=strong_overweight+int(df['severe overweight'].values[c])
     
    # рекомендации по полу в реальном мире вроде бы не различаются

    if index_bmi in range(left_limit,right_limit): 
        if index_bmi in range(left_limit, severe_underweight):
            print("Your BMI index is "+str(index_bmi)+" and you are in the extreme underweight and should call a doctor")
        elif index_bmi in range(severe_underweight, strong_underweight):
            print("Your BMI index is "+str(index_bmi)+
                  " and you are in the strong underweight range and should visit\n a doctor and a psychotherapist. "+
                  "And by the way do some "+str('male stuff' if d == 'male' else 'female or other stuff.'))
        elif index_bmi in range(strong_underweight, underweight):
            print("Your BMI index is "+str(index_bmi)+" and you are in the underweight range. It'kind a normal,\n but take some meds tests. "+
                  "And by the way do some "+str('male stuff' if d == 'male' else 'female or other stuff.'))
        elif index_bmi in range(underweight, normal):
            print("Your BMI index is "+str(index_bmi)+" and you are in the normal range." +
                  " Keep in pace your "+str('male stuff' if d == 'male' else 'female or other stuff.') )
        elif index_bmi in range(normal, overweight):
            print("Your BMI index is "+str(index_bmi)+" and you are in the overweight range. It'kind a normal,\n but take some meds tests. "+
                  "And by the way do some "+('male stuff' if d == 'male' else 'female or other stuff.'))
        elif index_bmi in range(overweight,strong_overweight):
            print("Your BMI index is "+str(index_bmi)+" and you are in the strong overweight range and should visit a doctor\n and a pshyhotherapist. "+
                  "And by the way do some "+('male stuff' if d == 'male' else 'female or other stuff.'))
        elif index_bmi in range(strong_overweight,severe_overweight):
            print("Your BMI index is "+str(index_bmi)+" and you are in the obese range and should call a doctor.")
        else: print ("You are probably dead")
        

#создаем дата фрэйм    
if d =='female' or d == 'other':
        df=pd.read_excel("referencesFemales.xlsx")
else:
         df=pd.read_excel("referencesMales.xlsx")
        

#рисуем график
draw_plot(df)

# Определяем BMI и его относительное расположение
bmi_point(a, b,c)

# определяем рекомеендации
diagnose(a, b,c,d, df)
plt.show()

#print( "Your referal values are: ")
#print(df.iloc[c:c+1, 0:9])




