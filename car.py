#! /usr/bin/python
# -*- coding:UTF-8 -*-
import sys
import RPi.GPIO as GPIO
import time
import motor as motor
import Getch

'''
L298N驱动马达状态表：
--------------------------------------------
	EN    |   IN1   |   IN2   |   电机状态
--------------------------------------------
	低    |  任意   |   任意  |    停止
	高    |   低    |    低   |    制动
	高    |   高    |    高   |    制动
	高    |   高    |    低   |    正传
	高    |   低    |    高   |    反转
--------------------------------------------
'''

'''
四轮定义: 马达 = [IN1, IN2, EN]
'''

Motor_Right = [26, 19, 13]	#右

Motor_Left = [21, 20, 16]  #左


#小车点火
def Car_power_on():
	GPIO.setmode(GPIO.BCM)	#设置GPIO模式
	GPIO.setwarnings(False) 
	motor.Motor_power_on(Motor_Right)
	motor.Motor_power_on(Motor_Left)

#小车运行：倒车
def Car_run_back():
	motor.Motor_positive(Motor_Right)
	motor.Motor_positive(Motor_Left)

#小车运行：前进
def Car_run_forward():
	motor.Motor_negative(Motor_Right)
	motor.Motor_negative(Motor_Left)

#小车运行：左转
def Car_run_left():
	motor.Motor_positive(Motor_Right)
	motor.Motor_negative(Motor_Left)

#小车运行：右转
def Car_run_right():
	motor.Motor_negative(Motor_Right)
	motor.Motor_positive(Motor_Left)

#小车运行：停止
def Car_run_pause():
	motor.Motor_pause(Motor_Right)
	motor.Motor_pause(Motor_Left)

#小车运行：制动
def Car_run_brake():
	motor.Motor_brake(Motor_Right)
	motor.Motor_brake(Motor_Left)

#小车熄火
def Car_Power_Off():
	GPIO.cleanup()

print("The Car is start...")
Car_power_on()
time.sleep(0.5)

#操作手册
print('----------------------------------')
print('w: Car forward.')
print('a: Car left.')
print('d: Car right.')
print('s: Car pause.')
print('x: Car back.')
print('f: Car brake.')
print('q: quit the program.')
print('----------------------------------')

while True:
	opt = Getch.Getch()
	if opt == 'w':
		Car_run_forward()
	elif opt == 'a':
		Car_run_left()
	elif opt == 'd':
		Car_run_right()
	elif opt == 's':
		Car_run_pause()
	elif opt == 'x':
		Car_run_back()
	elif opt == 'f':
		Car_run_brake()
	elif opt == 'q':
		break
	else:
		print('Invaild input.')

Car_run_pause()
Car_Power_Off()
