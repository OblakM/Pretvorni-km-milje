#!/usr/bin/env python
# -*- coding: utf-8 -*-

PRETVORNIK = "Pozdravljeni, sem PRETVORNIK merskih enot - km/milje"
print PRETVORNIK

milje = 0.6214

while True:
    xkm = int(raw_input("Vnesi število km: "))
    Rezultat = float(xkm * milje)
    print Rezultat


    ponovi_vajo = raw_input("Ali želite ponovno uporabiti pretvornik? (da/ne) ")

    if ponovi_vajo.lower() != "da":
        break