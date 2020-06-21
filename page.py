import asyncio
import faker.providers 
from faker import Faker
from faker_wifi_essid import WifiESSID
import json
import time
import random
from datetime import datetime

fake = Faker(['en_US'])
fake.add_provider(WifiESSID)


class PageAccess(KafkaProducer):

    def __init__(self):

        self.__website = ["http://www.samuelBloger.com","http://www.RayanneMaker.com","http://www.AlexTaynaPhotos.com",
    "http://www.VrlGamer","http://www.Vegetarian.com"]

        self.__plataform = [fake.android_platform_token(),fake.ios_platform_token()]
        
        self.ip = fake.ipv4()
        self.sessionId = f"{fake.pyint()}{fake.pystr(min_chars=2, max_chars=5)}"
        self.url = f"{random.choice(self.__website)}/{fake.uri_page()}"
        self.browser = fake.user_agent().split(" ")[0].split(".")[0]
        self.plataform = random.choice(self.__plataform)
        
        self.__timeS,self.__timeE = self.__genTime()
        self.timeStart = datetime.strptime(self.__timeS, '%Y-%m-%dT%H:%M:%S')
        self.timeEnd = datetime.strptime(self.__timeE, '%Y-%m-%dT%H:%M:%S')

    
    def __repr__(self):
        return f"[Ip: {self.ip}; sessionId: {self.sessionId}; url: {self.url}; browse: {self.browser}; plataform: {self.plataform}; TimeSpend: {self.timeEnd-self.timeStart} ]"


    def __genTime(self):
        day = random.randint(1,30)
        month = random.randint(1,12)
        # Beginning time
        hour_begin = random.randint(1,12)
        minutes_begin = random.randint(0,60)
        seconds_begin = random.randint(0,60)
        # End time
        delta_hour = hour_begin
        delta_minutes = minutes_begin + random.randint(0,60)
        delta_seconds = seconds_begin + random.randint(0,60)

        hour_end = hour_begin
        minutes_end = (delta_minutes - 60) if (delta_minutes >= 60) else delta_minutes
        seconds_end = (delta_seconds - 60) if (delta_seconds >= 60) else delta_seconds

        start_date = f"2020-{month}-{day}T{hour_begin}:{minutes_begin}:{seconds_begin}"
        end_date = f"2020-{month}-{day}T{hour_end}:{minutes_end}:{seconds_end}"
        return(start_date,end_date)