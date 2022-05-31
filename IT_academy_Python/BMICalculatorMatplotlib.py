import numpy as np
import matplotlib.pyplot as plt


category_names = ['Underweight range', 'Healthy weight',
                  'Overweight', 'Obese range']
refferal_ranges = {
    'BMI range': [13, 18, 25, 30],
    
}


def survey(refferal_ranges, category_names):
    
    labels = list(refferal_ranges.keys())
    data = np.array(list(refferal_ranges.values()))
    data_cum = data.cumsum(axis=1)
    #что-то непонятное пока
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())
    
    #форматирование
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            ax.text(x, y, str(int(c)), ha='right', va='center',
                    color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax

# рисуем горизонтальную линию c BMI
def bmi_line(a, b):
    index_bmi=int(round(b/(a/100)**2,0))
    ln=plt.axvline(x=index_bmi)
    plt.text((index_bmi+0.4),0,'Your BMI Index',rotation=270, color = 'white')
    return ln


input_data = False
while input_data==False: 
 try:
  a = int(input("Enter your height in cm: "))
  b = int(input("Enter your weight in kg: "))
  input_data=True
 except ValueError:
    print ("Only whole numbers, without literal or decimals.")
    input_data=False


# запускаем 

survey(refferal_ranges, category_names)
bmi_line(a, b)
plt.show()
