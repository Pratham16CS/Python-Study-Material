import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import os 
data = pd.DataFrame({
    'x': range(10),
    'y': [1,3,2,5,7,8,4,9,6,10]
})
plt.figure()
plt.plot(data['x'],data['y'],marker='o')
plt.title('Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig('line_plot.png')
plt.close()
wb = Workbook()
ws = wb.active
img = Image('line_plot.png')
ws.add_image(img,'A1')
wb.save('chart.xlsx')
os.remove('line_plot.png')
print('Successfull!!')