import json
import matplotlib.pyplot as plt
from math import exp, log

#КОНСТАНТЫ
H_0  = 55 * 1000 #высота начала падения в метрах
R = 8.31 #универсальная газовая постоянная в Дж/(градус*моль)
P_0 = 506625 # средняя атм давления на уровне поверхности в Па

h_1 = 5000 #м
p_1 = 316277	 #Па
h_2 = 10000 #м
p_2 = 182072	 #Па

H = (h_2 - h_1) / log(p_1 / p_2)

pressure_for_high = {}

for high in range(56):
    pressure = P_0 * exp(-high * 1000 / H)
    pressure_for_high[high] = pressure / 101325

    
with open("pressure_for_high.json", "w", encoding="UTF-8") as file_out:
    json.dump([pressure_for_high], file_out, ensure_ascii=False, indent=2)
    

with open("KSP_data.json", encoding="UTF-8") as file_in:
    KSP_data = json.load(file_in)

KSP_data = [value for value in KSP_data.values()]
KSP_pressure = {}
for value in KSP_data:
    KSP_pressure[value["Current altitude"] / 1000] = value["atm_press"] / 101325 
    

x_KSP = [key for key in KSP_pressure.keys()]
y_KSP = [value for value in KSP_pressure.values()]
x = [key for key in pressure_for_high.keys()]
y = [value for value in pressure_for_high.values()]
plt.plot(x, y, color='green')
plt.plot(x_KSP, y_KSP, color='orange')
plt.xlabel('Высота, км') 
plt.ylabel('Давление, атм')
plt.title('График зависимости давления от высоты') 
plt.legend(["Реализация мат. модели", "Даные KSP"])
plt.show