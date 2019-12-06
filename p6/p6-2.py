#!/usr/bin/env python3

OrbitObjs = {}

class OrbitObj:
    def __init__(self, name):
        OrbitObjs[name] = self
        self.__name = name
        self.__orbiting = []

    def GetName(self):
        return self.__name

    def AddOrbit(self, name):
        if name not in OrbitObjs:
            OrbitObjs[name] = OrbitObj(name)
        self.__orbiting.append(OrbitObjs[name])

    def GetOrbits(self):
        if len(self.__orbiting) == 0:
            return []
        else:
            res = []
            for orbit in self.__orbiting:
                res.append(orbit.GetName())
                res += orbit.GetOrbits()
            return res

    def GetStepsTo(self, name):
        if self.__name == name:
            return 0
        elif len(self.__orbiting) == 0:
            return float("inf")
        else:
            minsteps = float("inf")
            for orbit in self.__orbiting:
                nsteps = 1 + orbit.GetStepsTo(name)
                if nsteps < minsteps:
                    minsteps = nsteps
            return minsteps
            

with open("p6-input") as f:
    data = f.read().splitlines()

for orbit_data in data:
    objs = orbit_data.split(')')
    if objs[1] not in OrbitObjs:
        orbiter = OrbitObj(objs[1])
    else:
        orbiter = OrbitObjs[objs[1]]
    orbiter.AddOrbit(objs[0])

YOU_ORBITS = OrbitObjs['YOU'].GetOrbits()
SAN_ORBITS = OrbitObjs['SAN'].GetOrbits()
BOTH_ORBITS = list(set(YOU_ORBITS) & set(SAN_ORBITS))
minys = float("inf")
for close in BOTH_ORBITS:
    yssteps = OrbitObjs['YOU'].GetStepsTo(close) - 1 + OrbitObjs['SAN'].GetStepsTo(close) - 1
    if yssteps < minys:
        minys = yssteps

print(minys)
