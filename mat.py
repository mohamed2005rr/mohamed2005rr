import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz


x = np.arange(0, 101, 1)

fast = fuzz.trapmf(x, [40, 70, 100, 100])


plt.figure(figsize=(10, 5))

plt.plot(x, fast, 'b', linewidth=2, label='Fast Internet Speed')


plt.fill_between(x, fast, alpha=0.3, color='blue')


plt.title('Fuzzy Set - Fast Internet Speed')
plt.xlabel('Internet Speed (Mbps)')
plt.ylabel('Membership Degree')
plt.ylim(-0.05, 1.05)
plt.xlim(0, 100)



plt.grid(True, alpha=0.3)
plt.legend()


plt.show()