import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temps = [30, 32, 31, 29, 28]

plt.plot(days, temps, marker='^', linestyle='--', color='blue')

plt.title("Daily Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.show()
