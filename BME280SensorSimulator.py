# coding: utf-8
import random

class BME280SensorSimulator:

    def __init__(self):
        pass

    def get_temperature(self):
        return random.uniform(20, 30)

    def get_light(self):
        return random.uniform(60, 80)
