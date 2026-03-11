import RPi.GPIO as GPIO

# Global settings
GPIO_MODE = GPIO.BCM

# -----------------
# Motor Configuration (L298N)
# -----------------
# Left Motor 
ENA = 12  # PWM pin
IN1 = 5
IN2 = 6

# Right Motor
ENB = 13  # PWM pin
IN3 = 19
IN4 = 26

# Default Motor Speed (0-100)
# Maximum speed configuration to prevent brownout stalling 
DEFAULT_SPEED = 100
TURN_SPEED = 100

# -----------------
# IR Sensor Array Configuration
# -----------------
# Array of 8 Digital IR Sensors from Left to Right
# Depending on the sensor, HIGH could mean Black or White. Default: HIGH = Black line
IR_PINS = [4, 17, 27, 22, 10, 9, 11, 0] # Example GPIO pins

# -----------------
# Ultrasonic Sensor Configuration (HC-SR04)
# -----------------
ENABLE_OBSTACLE_AVOIDANCE = True # Set to True once line following works cleanly!
ULTRASONIC_TRIG = 23
ULTRASONIC_ECHO = 24
OBSTACLE_DISTANCE_THRESHOLD_CM = 15.0

# -----------------
# Camera Servo Configuration
# -----------------
SERVO_PIN = 18  # PWM pin for Servo
SERVO_FREQ = 50 # 50Hz for SG90 or similar servos

# -----------------
# Web Dashboard & Camera Configuration
# -----------------
FLASK_PORT = 5000
CAMERA_INDEX = 0  # 0 or 1 depending on Lapcare USB mounting
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
