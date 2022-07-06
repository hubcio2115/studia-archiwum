import cmath
import matplotlib.pyplot as plt

(rad, py) = cmath.polar(complex(1, 0))

n = int(input("Podaj stopień pierwiastka (n >= 2): "))

nums = []
coordsX = []
coordsY = []
for k in range(1, n + 1):
    number = cmath.cos((py + 2 * k * cmath.pi) / n) + \
        cmath.sin((py + 2 * k * cmath.pi) / n) * 1j
    nums.append(number)
    coordsX.append(number.real)
    coordsY.append(number.imag)

for i in range(len(nums)):
    plt.plot(nums[i].real, nums[i].imag, marker="o", markersize="3")
    if (i != len(nums) - 1):
        plt.plot([nums[i].real, nums[i + 1].real],
                 [nums[i].imag, nums[i + 1].imag])
    else:
        plt.plot([nums[i].real, nums[0].real],
                 [nums[i].imag, nums[0].imag])


plt.fill(coordsX, coordsY, "lightgray")

plt.axis('scaled')

plt.xlim([-2, 2])
plt.ylim([-2, 2])

plt.xlabel('Część Rzeczywista (Re)')
plt.ylabel('Część Urojona (Im)')

if n != 2:
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')

plt.grid()
plt.show()
