"""
file:teach04:teamactivity.py
author
"""
print("Welcome to the velocity calculator. Please enter the following:")
import math
#User Input
mass_bowling=float(input("What is the mass of the bowling ball (kg)? "))
mass_bread=float(input("What is the mass of the bread (kg)? "))
mass_skydiver=float(input("What is the mass of the skydiver (kg)? "))
gravity=float(input("What is the constant of gravity (m/s^2, 9.8 for Earth, 24 for Jupiter)? "))
time=float(input("Time (in seconds):"))
fluid_density=float(input("What is the density of the fluid (kg/m^3, 1.3 for air, 1000 for water)? "))
cross_sectional_bowling=float(input("What is the radius of the bowling ball (m)?"))
cross_sectional_bread=float(input("What is the length of the bread (m)?"))
cross_sectional_skydiver=float(input("What is the length of the skydiver(m)?"))
drag_constant_bowling=float(input("What is the drag constant of the bowling ball? (0.5 for sphere, 1.1 for cylinder)"))
drag_constant_bread=float(input("What is the drag constant of the bread? (0.5 for sphere, 1.1 for cylinder)"))
drag_constant_skydiver=float(input("What is the drag constant of the skydiver? (0.5 for sphere, 1.1 for cylinder)"))
print()
#Calculations
bowling_ball=math.pi*cross_sectional_bowling**2
bread=math.pi*cross_sectional_bread**2
skydiver=math.pi*cross_sectional_skydiver**2
c_bowling=(1/2)*fluid_density*bowling_ball*drag_constant_bowling
c_bread=(1/2)*fluid_density*bread*drag_constant_bread
c_skydiver=(1/2)*fluid_density*skydiver*drag_constant_skydiver

velocity_bowling=math.sqrt(mass_bowling*gravity/c_bowling)*(1-math.exp((-math.sqrt(mass_bowling*gravity*c_bowling)/mass_bowling)*time))
velocity_bread=math.sqrt(mass_bread*gravity/c_bread)*(1-math.exp((-math.sqrt(mass_bread*gravity*c_bread)/mass_bread)*time))
velocity_skydiver=math.sqrt(mass_skydiver*gravity/c_skydiver)*(1-math.exp((-math.sqrt(mass_skydiver*gravity*c_skydiver)/mass_skydiver)*time))

#Output
print()
print(f"The inner value of c is: {c_bowling:.3f}")
print(f"The velocity after {time} seconds is: {velocity_bowling:.3f} m/s")
print(f"The inner value of c is: {c_bread:.3f}")
print(f"The velocity after {time} seconds is: {velocity_bread:.3f} m/s")
print(f"The inner value of c is: {c_skydiver:.3f}")
print(f"The velocity after {time} seconds is: {velocity_skydiver:.3f} m/s")
print()
#Terminal Velocity of a Skydiver
v_terminal= math.sqrt(mass_skydiver*gravity/c_skydiver)
print(f"The terminal velocity of a skydiver is: {v_terminal:.3f} m/s.")
