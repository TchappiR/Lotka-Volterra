import matplotlib.pyplot as plt
import numpy as np

time = [0]
lapin = [1]
renard = [2]

alpha, beta, delta, gama = 2/3, 4/3, 1, 1
step = 0.001

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

    
plt.figure(figsize=(15, 6))
plt.plot(time, lapin, "b-", label="Lapins")
plt.plot(time, renard, "r-", label="Renards")
plt.xlabel("Temps (en Mois)")
plt.ylabel("Population")
plt.legend()
plt.show()