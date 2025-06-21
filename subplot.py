import matplotlib.pyplot as plt

# Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperatures = [30, 32, 31, 29, 28]

# Create a figure
plt.figure(figsize=(10, 8))  # Wider and taller figure

# ----------- 1. Line Plot (Top Left) -----------
plt.subplot(2, 2, 1)
plt.plot(days, temperatures, marker='o', linestyle='-', color='blue')
plt.title("Line Plot")
plt.xlabel("Day")
plt.ylabel("Temp (°C)")

# ----------- 2. Verical Bar Plot (Top Right) -----------
plt.subplot(2, 2, 2)
plt.bar(days, temperatures, color='green')
plt.title("Bar Plot")
plt.xlabel("Day")
plt.ylabel("Temp (°C)")

# ----------- 3. Pie Chart (Bottom Left ) -----------
plt.subplot(2, 2, 3)
plt.pie(temperatures, labels=days, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")

# ----------- 4. Horizontal Bar Plot (Bottom Right) -----------
plt.subplot(2, 2, 4)
plt.barh(days, temperatures, color='green')
plt.title("Bar Plot")
plt.xlabel("Temp (°C)")
plt.ylabel("Day")


# Adjust layout
plt.tight_layout()

# Show all plots
plt.show()
