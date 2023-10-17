import random
import time

# Simulated sensor readings
def get_pH_reading():
    return random.uniform(6.9, 8.0)

def get_conductivity_reading():
    return random.uniform(0.0, 1.5)  # Simulated conductivity within +/- 0.5

def get_chlorine_reading():
    return random.uniform(0.0, 0.2)  # Simulated chlorine content

def get_hardness_reading():
    return random.uniform(0.0, 500.0)  # Simulated hardness

# Alarm function
def trigger_alarm(parameter, threshold, parameter_name):
    print(f"ALARM: {parameter_name} is out of bounds! Current \ value: {parameter:.2f}, Threshold: {threshold}")

# Main monitoring loop
while True:
    pH = get_pH_reading()
    conductivity = get_conductivity_reading()
    chlorine = get_chlorine_reading()
    hardness = get_hardness_reading()

    # Check pH threshold
    if pH < 6.9 or pH > 7.6:
        trigger_alarm(pH, "6.9-7.6", "pH")

    # Check conductivity threshold
    if abs(conductivity - 0.5) > 0.5:
        trigger_alarm(conductivity, "+/- 0.5", "Conductivity")

    # Check chlorine content threshold
    if chlorine > 0.1:
        trigger_alarm(chlorine, "< 0.1 mg/L", "Chlorine Content")

    # Check hardness threshold
    if hardness > 450:
        trigger_alarm(hardness, "< 450 mg/L", "Hardness")

    # Sleep for a specified interval (e.g., 1 minute)
    time.sleep(5)
