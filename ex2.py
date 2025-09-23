import numpy as np
import matplotlib.pyplot as plt

#First Design with unequal power output
t=np.linspace(0,60,500)
m1=t
m2=4*(t-30)

fig, ax = plt.subplots()

plt.title('Unequal power output')
plt.xlabel('time (in days)')
plt.ylabel('energy (in KJ)')

ax.set_xlim(0,60)
ax.set_ylim(0,60)
ax.plot(t,m1,c='green')
ax.plot(t,m2,c='brown')
plt.axvline(x=40, color='purple', linestyle='--')
plt.axhline(y=40, color='purple', linestyle='--')

#Second Design with equal power output

t=np.linspace(0,1600,1500)
m1=t
m2=1*(t-30)

fig, bx = plt.subplots()

plt.title('Equal power output')
plt.xlabel('time (in days)')
plt.ylabel('energy (in KJ)')

bx.set_xlim(0,300)
bx.set_ylim(0,300)
bx.plot(t,m1,c='blue')
bx.plot(t,m2,c='red')
plt.axvline(x=40, color='green', linestyle='-.')
plt.axhline(y=40, color='green', linestyle='-.')