#! /usr/bin/python
# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO  #GPIO package  
import time

IN1 = 0
IN2 = 1 
EN = 2

#马达上电
def Motor_power_on(motor): 
	GPIO.setup(motor[IN1],GPIO.OUT,initial=GPIO.LOW)
	GPIO.setup(motor[IN2],GPIO.OUT,initial=GPIO.LOW)
	GPIO.setup(motor[EN], GPIO.OUT,initial=GPIO.LOW)

'''
马达停转
--------------------------------------------
	EN    |   IN1   |   IN2   |   电机状态
--------------------------------------------
	低    |  任意   |   任意  |    停止
--------------------------------------------
'''
def Motor_pause(motor):
	GPIO.output(motor[IN1], GPIO.LOW) #输出低电平  
	GPIO.output(motor[IN2], GPIO.LOW) #输出低电平  
	GPIO.output(motor[EN], GPIO.LOW) #输出低电平 
	
'''
马达正转
--------------------------------------------
	EN    |   IN1   |   IN2   |   电机状态
--------------------------------------------
	高    |   高    |    低   |    正传
--------------------------------------------
'''
def Motor_positive(motor):
	GPIO.output(motor[IN1], GPIO.HIGH) #输出高电平  
	GPIO.output(motor[IN2], GPIO.LOW) #输出低电平  
	GPIO.output(motor[EN], GPIO.HIGH) #输出高电平 

'''
马达反转
--------------------------------------------
	EN    |   IN1   |   IN2   |   电机状态
--------------------------------------------
	高    |   低    |    高   |    反转
--------------------------------------------
'''
def Motor_negative(motor):
	GPIO.output(motor[IN1], GPIO.LOW) #输出低电平  
	GPIO.output(motor[IN2], GPIO.HIGH) #输出高电平  
	GPIO.output(motor[EN], GPIO.HIGH) #输出高电平 

'''
马达制动
--------------------------------------------
	EN    |   IN1   |   IN2   |   电机状态
--------------------------------------------
	高    |   低    |    低   |    制动
	高    |   高    |    高   |    制动
--------------------------------------------
'''
def Motor_brake(motor):
	GPIO.output(motor[IN1], GPIO.LOW) #输出高电平  
	GPIO.output(motor[IN2], GPIO.LOW) #输出低电平  
	GPIO.output(motor[EN], GPIO.HIGH) #输出低电平 