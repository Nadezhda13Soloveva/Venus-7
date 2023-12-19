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

pressure_remains = {}
new_pressure = {}

with open("KSP_data.json", encoding="UTF-8") as file_in:
    KSP_data = json.load(file_in)

KSP_data = [value for value in KSP_data.values()]
KSP_pressure = {}
for value in KSP_data:
    KSP_pressure[value["Current altitude"] / 1000] = value["atm_press"] / 101325
    

for high in KSP_pressure.keys():
    pressure = (P_0 * exp(-int(high) * 1000 / H)) / 101325
    new_pressure[high] = pressure
    pressure_remains[high] = KSP_pressure[high] - pressure
    
with open("pressure_for_remains.json", "w", encoding="UTF-8") as file_out:
    json.dump([new_pressure], file_out, ensure_ascii=False, indent=2)
with open("KSP_pressure.json", "w", encoding="UTF-8") as file_out:
    json.dump([KSP_pressure], file_out, ensure_ascii=False, indent=2)
    

x = [key for key in pressure_remains.keys()]
y = [value for value in pressure_remains.values()]
plt.plot(x, y, color='blue')
plt.axhline(0, color='r', linestyle='--')
plt.xlabel('Высота, км') 
plt.ylabel('Остатки, Па')
plt.title('Погрешность при вычислении атмосферного давления') 
plt.show