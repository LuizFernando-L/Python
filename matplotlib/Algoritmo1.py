from matplotlib import pyplot as plt
import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)
plt.plot(dados1, dados2) #Python gerencia a figura e o eixo
