print(Scale.default)

Scale.default.set("major")
Root.default.set("C")
Clock.bpm=100

a = P[:8]
p1 >> pluck(a)

ch1 = (-3, -1, 1)
ch2 = (-3.5, -2)
ch3 = (-2, 0, 1.5)
p1 >> keys([ch1, ch2, ch3], dur=[4,2,2], root=4, rate=2, vib=4)

lofi = [ch1, ch2, ch3]
p2 >> bass([tuple(x -2 for x in t) for t in lofi])

d1 >> play("V---o---", bpm=120, sample=-5)
t1 >> play("S")
d2 >> play("X   ><-   ><#   ><V   >")

ch1 = (0,2,4, 6,8)
ch2 = (0,1.5,4)
ch3 = (2,4,6)
ch4 = (-1, -2,5, -5)
lofi = [ch1, ch2, ch3, ch4]
p1 >> keys(lofi, dur=[4,4, 0.5, 2.5], sus=2, rate=[0], bits=24)

d1 >> play("x - o - ", sample=0)

p2.stop()


print(Clock.bpm)
print(Player.get_attributes())

p1 >> pluck()
