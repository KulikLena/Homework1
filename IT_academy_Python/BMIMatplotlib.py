import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


input_data = False
while input_data==False: 
    try:
        a = int(input("Enter your height in cm: "))
        b = int(input("Enter your weight in kg: "))
        c= int(input("Enter your age in years: "))
        input_data=True
    except ValueError:
         print ("Only whole numbers, without literal or decimals.")
         input_data=False


def draw_plot (filename):
    df=pd.read_excel(filename)
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
    ax.set_title('BMI Index')
    ax.set_xlabel('Age')
    ax.set_ylabel('BMI Index')
    return fig, ax
    
def bmi_point(a, b,c):
    index_bmi=int(round(b/(a/100)**2,0))
    pnt=plt.plot(c,index_bmi, marker=(5, 1), color = 'white')
    plt.text(c,(index_bmi+2),'Your BMI Index',rotation=0, color = 'white' )
    return pnt, index_bmi

def diagnose (a, b,c): 
    index_bmi=int(round(b/(a/100)**2,0))
    left_limit=0
    right_limit=50
    
    if index_bmi in range(left_limit,right_limit): 
        if index_bmi in range(left_limit, int(df['severe underweight'].values[c])):
            print("Your BMI index is "+str(index_bmi)+" and you are in the extreme underweight")
        elif index_bmi in range(int(df['severe underweight'].values[c]), int(df['strong underweight'].values[c])):
            print("Your BMI index is "+str(index_bmi)+" and you are in the strong underweight range")
        elif index_bmi in range(int(df['strong underweight'].values[c]), int(df['underweight'].values[c])):
            print("Your BMI index is "+str(index_bmi)+" and you are in the underweight range")
        elif index_bmi in range(int(df['underweight'].values[c]), int(df['normal'].values[c])):
            print("Your BMI index is "+str(index_bmi)+" and you are in the normal range")
        elif index_bmi in range(int(df['normal'].values[c]), int(df['overweight'].values[c])):
            print("Your BMI index is "+str(index_bmi)+" and you are in the overweight range")
        elif index_bmi in range(int(df['overweight'].values[c]),int(df['strong overweight'].values[c])):
            print("Your BMI index is "+str(index_bmi)+" and you are in the strong overweight range")
        elif index_bmi in range(int(df['strong overweight'].values[c]),int(df['severe overweight'].values[c])):
            print("Your BMI index is "+str(index_bmi)+" and you are in the obese range")
        return




draw_plot("references.xlsx")
bmi_point(a, b,c)

diagnose(a, b,c)
plt.show()

print( "Your referal values are: ")
print(df.iloc[c:c+1, 0:9])

