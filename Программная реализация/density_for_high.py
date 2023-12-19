import json
import matplotlib.pyplot as plt
from math import exp, log

#КОНСТАНТЫ
H_0  = 55 * 10 ** 3 #высота начала падения в метрах
R = 8.31 #универсальная газовая постоянная в Дж/(градус*моль)
M = 0.044 #молярная масса СО2 в кг/моль
g = 16.7 #ускорение свободного падения в м/с^2
p_0 = 6.517 #плотность воздуха на уровне моря кг/м^3

h_1 = 5000 #м
p_1 = 4.633  #кг/м^3
h_2 = 10000 #м
p_2 = 3.036 #кг/м^3   
    
density_for_high = {}
H = (h_2 - h_1) / log(p_1 / p_2)

for high in range(56):
    density = p_0 * exp(-high * 1000/ H)
    density_for_high[high] = density
    
with open("density_for_high.json", "w", encoding="UTF-8") as file_out:
    json.dump([density_for_high], file_out, ensure_ascii=False, indent=2)
    
    
with open("KSP_data.json", encoding="UTF-8") as file_in:
    KSP_data = json.load(file_in)

KSP_data = [value for value in KSP_data.values()]
KSP_density = {}
for value in KSP_data:
    KSP_density[value["Current altitude"] / 1000] = value["Atmosphere density"]
    
  
x_KSP = [key for key in KSP_density.keys()]
y_KSP = [value for value in KSP_density.values()]
    
x = [key for key in density_for_high.keys()]
y = [value for value in density_for_high.values()]
plt.plot(x, y, color='green')
plt.plot(x_KSP, y_KSP, color='orange')
plt.xlabel('Высота, км') 
plt.ylabel('Плотность воздуха, кг/м^3')
plt.title('График зависимости плотности воздуха от высоты') 
plt.legend(["Реализация мат. модели", "Даные KSP"])
plt.show

