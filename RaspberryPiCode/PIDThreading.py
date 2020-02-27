import threading
import time
from simple_pid import PID

import smbus
import math

# Power management registers
power_mgmt_1 = 0x6b

bus = smbus.SMBus(0) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command


def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def get_imu():
    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    return get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled), get_y_rotation(
        accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)




# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)
motor_values = [2048, 2074, 2100, 2127, 2153, 2180, 2206, 2233, 2259, 2285, 2312, 2338, 2364, 2390, 2416, 2442, 2468, 2494, 2520, 2546, 2571, 2597, 2622, 2648, 2673, 2698, 2723, 2748, 2773, 2797, 2822, 2846, 2871, 2895, 2919, 2943, 2967, 2990, 3014, 3037, 3060, 3083, 3106, 3128, 3151, 3173, 3195, 3217, 3238, 3260, 3281, 3302, 3323, 3344, 3364, 3384, 3404, 3424, 3443, 3463, 3482, 3500, 3519, 3537, 3555, 3573, 3591, 3608, 3625, 3642, 3658, 3674, 3690, 3706, 3721, 3736, 3751, 3766, 3780, 3794, 3808, 3821, 3834, 3847, 3859, 3872, 3884, 3895, 3906, 3917, 3928, 3938, 3948, 3958, 3967, 3976, 3985, 3994, 4002, 4009, 4017, 4024, 4031, 4037, 4043, 4049, 4055, 4060, 4064, 4069, 4073, 4077, 4080, 4083, 4086, 4088, 4090, 4092, 4093, 4094, 4095, 4095, 4095, 4095, 4094, 4093, 4092, 4090, 4088, 4086, 4083, 4080, 4077, 4073, 4069, 4064, 4060, 4055, 4049, 4043, 4037, 4031, 4024, 4017, 4009, 4002, 3994, 3985, 3976, 3967, 3958, 3948, 3938, 3928, 3917, 3906, 3895, 3884, 3872, 3859, 3847, 3834, 3821, 3808, 3794, 3780, 3766, 3751, 3736, 3721, 3706, 3690, 3674, 3658, 3642, 3625, 3608, 3591, 3573, 3555, 3537, 3519, 3500, 3482, 3463, 3443, 3424, 3404, 3384, 3364, 3344, 3323, 3302, 3281, 3260, 3238, 3217, 3195, 3173, 3151, 3128, 3106, 3083, 3060, 3037, 3014, 2990, 2967, 2943, 2919, 2895, 2871, 2846, 2822, 2797, 2773, 2748, 2723, 2698, 2673, 2648, 2622, 2597, 2571, 2546, 2520, 2494, 2468, 2442, 2416, 2390, 2364, 2338, 2312, 2285, 2259, 2233, 2206, 2180, 2153, 2127, 2100, 2074, 2048, 2021, 1995, 1968, 1942, 1915, 1889, 1862, 1836, 1810, 1783, 1757, 1731, 1705, 1679, 1653, 1627, 1601, 1575, 1549, 1524, 1498, 1473, 1447, 1422, 1397, 1372, 1347, 1322, 1298, 1273, 1249, 1224, 1200, 1176, 1152, 1128, 1105, 1081, 1058, 1035, 1012, 989, 967, 944, 922, 900, 878, 857, 835, 814, 793, 772, 751, 731, 711, 691, 671, 652, 632, 613, 595, 576, 558, 540, 522, 504, 487, 470, 453, 437, 421, 405, 389, 374, 359, 344, 329, 315, 301, 287, 274, 261, 248, 236, 223, 211, 200, 189, 178, 167, 157, 147, 137, 128, 119, 110, 101, 93, 86, 78, 71, 64, 58, 52, 46, 40, 35, 31, 26, 22, 18, 15, 12, 9, 7, 5, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 5, 7, 9, 12, 15, 18, 22, 26, 31, 35, 40, 46, 52, 58, 64, 71, 78, 86, 93, 101, 110, 119, 128, 137, 147, 157, 167, 178, 189, 200, 211, 223, 236, 248, 261, 274, 287, 301, 315, 329, 344, 359, 374, 389, 405, 421, 437, 453, 470, 487, 504, 522, 540, 558, 576, 595, 613, 632, 652, 671, 691, 711, 731, 751, 772, 793, 814, 835, 857, 878, 900, 922, 944, 967, 989, 1012, 1035, 1058, 1081, 1105, 1128, 1152, 1176, 1200, 1224, 1249, 1273, 1298, 1322, 1347, 1372, 1397, 1422, 1447, 1473, 1498, 1524, 1549, 1575, 1601, 1627, 1653, 1679, 1705, 1731, 1757, 1783, 1810, 1836, 1862, 1889, 1915, 1942, 1968, 1995, 2021]

import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(1600)
sample_time = .01
time_delay = .01

m1_min = -10
m1_max = 10
m1_pid = PID(0, 0, 0, 0, sample_time, (-10, 10))

m1_p1 = 0
m1_p2 = 162
m1_p3 = 324

m1_p1_1 = 0
m1_p1_2 = 1
m1_p1_3 = 2

m1_speed = 0

m1_error = 0

class BrushlessMotorThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        global m1_p1
        global m1_p2
        global m1_p3
        global m1_speed
        while True:
            m1_p1 += m1_speed
            m1_p2 += m1_speed
            m1_p3 += m1_speed

            if m1_p1 > 485:
                m1_p1 = 0
            if m1_p2 > 485:
                m1_p2 = 0
            if m1_p3 > 485:
                m1_p3 = 0

            if m1_p1 < 0:
                m1_p1 = 485
            if m1_p2 < 0:
                m1_p2 = 485
            if m1_p3 < 0:
                m1_p3 = 485

            time.sleep(time_delay)

class InterfaceThread(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      while True:
          pwm.set_pwm(m1_p1_1, 0, motor_values[m1_p1])
          pwm.set_pwm(m1_p1_2, 0, motor_values[m1_p2])
          pwm.set_pwm(m1_p1_3, 0, motor_values[m1_p3])


class PIDCalculationThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        global m1_speed
        global m1_error
        while True:
            m1_error, m2_error = get_imu()
            m1_speed = m1_pid(m1_error)


# Create new threads
interface = InterfaceThread(2, "interface")
pidCalc = PIDCalculationThread(1, "pidCalc")
motorCalc= BrushlessMotorThread(3, "motorCalc")

# Start new Threads
interface.start()
pidCalc.start()
motorCalc.start()