#
# dosage.py - simulates the amount of aspirin in the system
#
import matplotlib.pyplot as plt
import numpy as np
import math

half_life = 3.2          # elimination of aspirin
plasma_volume = 3000     # volume of plasma (adult)
aspirin_in_plasma = 2 * 325 * 1000  # two tablets @ 325mg @ unit conversion
MEC = 150   # approximate concentration for effectiveness
MTC = 350   # approximate concentration for toxicity

elimination_constant = -math.log(0.5)/half_life
elimination = elimination_constant * aspirin_in_plasma
plasma_concentration = aspirin_in_plasma/plasma_volume

simulation_time = 8
time_step_size = 0.1
num_steps = int(simulation_time/time_step_size)
cumulative_time = 0.0

values = np.empty(num_steps)

for time_step in range (int(num_steps)):
    values[time_step] = plasma_concentration
    elimination = elimination_constant * time_step_size * aspirin_in_plasma
    aspirin_in_plasma -= elimination
    plasma_concentration = aspirin_in_plasma/plasma_volume


# print(values)

times = np.linspace(0, simulation_time - time_step_size, num_steps)

# MECline = np.full(num_steps, MEC)
# MTCline = np.full(num_steps, MTC)

plt.figure()
plt.title('Aspirin in Plasma')
plt.xlabel('Time (hours)')
plt.ylabel('Concentration')

plt.plot(times, values)

# plt.plot(times, values, '-', times, MECline, 'g-', times, MTCline, 'r-')

plt.show()


