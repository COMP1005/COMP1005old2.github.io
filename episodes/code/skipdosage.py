#
# skipdosage.py
#
import matplotlib.pyplot as plt
import math
import numpy as np

half_life = 22            # Dilantin half-life
interval = 8              # 8 hours between doses
MEC = 10/100000           # Effective concentration
MTC = 20/100000           # Toxic concentration
volume = 3000             # blood plasma volume
dosage = 100*1000         # dosage 100mg 
absorption_fraction = 0.12
drug_in_system = 0        # initial amount of drug in system
ln05 = math.log(0.5)
elimination_constant = -ln05/half_life
pulse = 0
entering = absorption_fraction * pulse * dosage
elimination = elimination_constant * drug_in_system
concentration = drug_in_system/volume

simulation_time = 168     # simulation time 168
time_step_size = 1        # time step = 1 hour
num_steps = int(simulation_time/time_step_size)
cumulative_time = 0.0     # initial time = 0

values = np.empty(num_steps) 

for time_step in range (num_steps):
    values[time_step] = concentration
    if (time_step % interval == 0):
       pulse = 1
    else:
       pulse = 0
#    if time_step == 80 or time_step == 88 or time_step == 96:
#        pulse = 0
    entering = absorption_fraction * pulse
    elimination = elimination_constant * drug_in_system
    drug_in_system = drug_in_system - elimination + entering
    concentration = drug_in_system / volume

times = np.linspace(0, simulation_time - time_step_size, num_steps)
# print(values)

MECline = np.full(num_steps, MEC)
MTCline = np.full(num_steps, MTC)

plt.figure()
plt.title('Dilantin Concentration')
plt.xlabel('Time (hours)')
plt.ylabel('Concentration')
plt.plot(times, values, '-', times, MECline, 'g-', times, MTCline, 'r-')
plt.show()
