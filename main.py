import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import *

time = [0]
lapin = [1]
renard = [2]

alpha, beta, delta, gama = 2/3, 4/3, 1, 1
step = 0.001

fichier = "populations_lapins_renards.csv"
df = pd.read_csv(fichier)

for _ in range(100_000):
    nex_value_time = time[-1] + step
    new_value_lapin = (lapin[-1] * (alpha - beta * renard[-1])) * step  + lapin[-1]
    new_value_renard = (renard[-1] * (delta * lapin[-1] - gama)) * step  + renard[-1]
    
    time.append(nex_value_time)
    lapin.append(new_value_lapin)
    renard.append(new_value_renard)
    
lapin = np.array(lapin)
lapin *= 1_000

renard = np.array(renard)
renard *= 1_000


#Calcul de la MSE 

real_lapin_value = np.array(df["lapin"])
real_renard_value = np.array(df["renard"])

mse_lapin = mean_squared_error(real_lapin_value, lapin[:1_000])
mse_renard = mean_squared_error(real_renard_value, renard[:1_000])

rmse_lapin = np.sqrt(mse_lapin)
rmse_renard = np.sqrt(mse_renard)

"""print(f"MSE lapin = {mse_lapin}")
print(f"MSE renard = {mse_renard}")"""

print(f"RMSE lapin = {rmse_lapin}")
print(f"RMSE renard = {rmse_renard}")


# Graphique
plt.figure(figsize=(15, 6))
plt.plot(time, lapin, "b-", label="Lapins")
plt.plot(time, renard, "r-", label="Renards")
plt.xlabel("Temps (en Mois)")
plt.ylabel("Population")
plt.legend()
plt.show()