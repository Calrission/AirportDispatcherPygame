from Scenario import Scenario
from const import fps

sct = Scenario()

"""DEBUG START"""
sct.add_land('001', 'A', 5 * fps, 10)
sct.add_take_off("000", 'A', 4 * fps, 20)
sct.add_land('002', 'B', 6 * fps, 12)
sct.add_land('003', 'A', 7 * fps, 14)
sct.add_take_off('004', 'A', 10 * fps, 16)
sct.save('debagScenario.scen')

"""LEVEL-1"""
sc1 = Scenario()
sc1.add_land('01', 'A', 3 * fps, 10)
sc1.add_land('02', 'B', 4 * fps, 10)
sc1.add_take_off('03', 'A', 11 * fps, 16)
sc1.add_land('04', 'B', 14 * fps, 16)
sc1.add_land('05', 'A', 20 * fps, 12)
sc1.add_take_off('06', 'B', 22 * fps, 12)
sc1.add_take_off('07', 'A', 31 * fps, 12)
sc1.save('Level-1.scen')

"""LEVEL-2"""
sc2 = Scenario()
sc2.add_land('01', 'B', 2 * fps, 10)
sc2.add_take_off('02', 'B', 3 * fps, 20)
sc2.add_take_off('03', 'A', 5 * fps, 16)
sc2.add_land('04', 'B', 10 * fps, 16)
sc2.add_land('05', 'A', 11 * fps, 12)
sc2.add_take_off('06', 'B', 15 * fps, 12)
sc2.add_land('07', 'A', 20 * fps, 18)
sc2.save('Level-2.scen')

"""LEVEL-3"""
sc3 = Scenario()
sc3.add_land('01', 'A', 5 * fps, 4)
sc3.add_take_off('02', 'A', 6 * fps, 20)
sc3.add_land('03', 'B', 5 * fps, 16)
sc3.add_land('04', 'B', 6 * fps, 4)
sc3.add_take_off('05', 'A', 9 * fps, 12)
sc3.add_take_off('06', 'B', 14 * fps, 12)
sc3.add_land('07', 'B', 19 * fps, 15)
sc3.save('Level-3.scen')

