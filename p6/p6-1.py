#!/usr/bin/env python3

OrbitObjs = {}

class OrbitObj:
    def __init__(self, name):
        OrbitObjs[name] = self
        self.__name = name
        self.__orbiting = []

    def AddOrbit(self, name):
        if name not in OrbitObjs:
            OrbitObjs[name] = OrbitObj(name)
        self.__orbiting.append(OrbitObjs[name])

    def GetOrbitAmt(self):
        if len(self.__orbiting) == 0:
            return 0
        else:
            amt = 0
            for orbit in self.__orbiting:
                amt += 1 + orbit.GetOrbitAmt()
            return amt

with open("p6-input") as f:
    data = f.read().splitlines()

for orbit_data in data:
    objs = orbit_data.split(')')
    if objs[1] not in OrbitObjs:
        orbiter = OrbitObj(objs[1])
    else:
        orbiter = OrbitObjs[objs[1]]
    orbiter.AddOrbit(objs[0])

total = 0
for orbit in OrbitObjs:
    total += OrbitObjs[orbit].GetOrbitAmt()

print(total)
