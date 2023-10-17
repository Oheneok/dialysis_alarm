import time

1 usage
class DialysisWaterMonitor:
    def __init__(self):
        # Initialize a dictionary to store acceptable thresholds for water parameters
        self. thresholds = {
            "pH" : (0, 14),         #pH range (0-14)
            "hardness" : (0, 100)   #Hardness range (0-100)
            "chlorine" : (0, 5)     #Chlorine range (0-5)
            "conductivity" : ()
        }