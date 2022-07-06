from math import sqrt, degrees
import matplotlib.pyplot as plt

print("Rysowanie liczby zespolonej w postaci prostej na wykresie")
x = float(input("Podaj wartość x: "))
y = float(input("Podaj wartość y: "))

module = round(sqrt(x**2 + y**2), 2)
degrees = round(degrees(x / module), 2)

plt.plot([0, x], [0, y], ls="--")
plt.legend(
    [f"|z| = {module}\nkąt: {degrees}°"])

plt.xlabel('Część Rzeczywista (Re)')
plt.ylabel('Część Urojona (Im)')

xLimit = 2 * sqrt(x**2)
yLimit = 2 * sqrt(y**2)

plt.xlim(-xLimit, xLimit)
plt.ylim(-yLimit, yLimit)

plt.scatter(x, y)

plt.axvline(0, color='black')
plt.axhline(0, color='black')

plt.annotate(f"({x}, {y}i)", xy=(x, y))

plt.grid()
plt.show()
