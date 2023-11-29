#!/usr/bin/env python3
#
# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres


def liters_100km_to_miles_gallon(liters):
    miles = 100_000 / 1609.344
    gallons = liters / 3.785411784
    miles_gallon = miles / gallons
    return miles_gallon


def miles_gallon_to_liters_100km(miles):
    literes_100km = 3.785411784 / (miles * 1609.344 / 1000 / 100) 
    return float(literes_100km)



print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


