# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton
# ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden
# ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi
# sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton
# (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja
# tulosta autojen matkamittarilukemat.

from random import randint


class Kilpailu:

    def __init__(self, race_name, distance, participants):
        self.race_name = race_name
        self.distance = distance
        self.participants = participants

    def hour_pass(self):
        for car in self.participants:
            car.accelerate(randint(-10, 15))
            car.travel(1)

    def print_status(self):
        for car in self.participants:
            car.print_info()

    def race_over(self):
        for car in self.participants:
            if car.tripmeter >= self.distance:
                return True
            else:
                continue


class Car:

    def __init__(self, reg, top_speed):
        self.reg = reg
        self.top_speed = top_speed
        self.speed = 0
        self.tripmeter = 0

    def print_info(self):
        print(f"Auton {self.reg:6}; "
              f"huippunopeus on:{self.top_speed:0}Km/h, "
              f"matkamittari: {self.tripmeter:5}Km, "
              f"Tämän hetkinen nopeus: {self.speed}Km/h")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change <= self.top_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        elif self.speed + speed_change > self.top_speed:
            self.speed = self.top_speed

    def travel(self, hours):
        if hours < 0:
            self.tripmeter = self.tripmeter
        elif hours > 0:
            self.tripmeter = self.tripmeter + (self.speed * hours)


class Electric(Car):

    def __init__(self, reg, top_speed, kwh):
        super().__init__(reg, top_speed)
        self.battery_capacity = kwh

    def print_info(self):
        super().print_info()
        print(f"Akun kapasiteetti: {self.battery_capacity} kW/h")


class Gas(Car):

    def __init__(self, reg, top_speed, gaso):
        super().__init__(reg, top_speed)
        self.gaso = gaso

    def print_info(self):
        super().print_info()
        print(f"Bensatankki tilavuus: {self.gaso} l.")


ev = Electric("ABC-15", 180, 52.5)
gas = Gas("ACD-123", 165, 32.3)

ev.accelerate(50)
ev.travel(3)
ev.print_info()

gas.accelerate(50)
gas.travel(3)
gas.print_info()