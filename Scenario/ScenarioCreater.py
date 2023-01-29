from Scenario import Scenario
from const import fps

sct = Scenario()

sct.add_land('001', 'A', 5 * fps, 10)
sct.add_take_off("000", 'A', 4 * fps, 20)
sct.add_land('002', 'B', 6 * fps, 12)
sct.add_land('003', 'A', 7 * fps, 14)
sct.add_take_off('004', 'A', 10 * fps, 16)

sct.save('debagScenario.scen')


sc1 = Scenario()

# sc1.add_land('Level-1', 'A', 1 * fps, 999)

sc1.add_land('01', 'A', 3 * fps, 10)
sc1.add_land('02', 'B', 4 * fps, 10)
sc1.add_take_off('03', 'A', 11 * fps, 16)
sc1.add_land('04', 'B', 14 * fps, 16)
sc1.add_land('05', 'A', 20 * fps, 12)
sc1.add_take_off('06', 'B', 22 * fps, 12)
sc1.add_take_off('07', 'A', 31 * fps, 12)

sc1.save('Level-1.scen')

sc2 = Scenario()

sc2.add_land('Level-2', 'B', 1 * fps, 999)

sc2.save('Level-2.scen')

sc3 = Scenario()

sc3.add_land('Level-3', 'A', 1 * fps, 999)

sc3.save('Level-3.scen')

