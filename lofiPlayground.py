Clock.bpm=100
Scale.default = "major"
Root.default.set("D")

Clock.reset()

ch1 = (0, 1.5, 4,  6, 8, 10)
ch2 = tuple(x + 0.5 for x in ch1)
print(ch2)
p1 >> nylon(P[ch1, ch2], dur=4, sus=3, amp=0.8, rate=0)

p2 >> blip([(0, 1.5, 4, 6, 8, 10), (0.5, 2, 4.5)], dur=4, sus=3, amp=0.8)

print(Player.get_attributes())

# not strictly according to chord, small variations
ch1 = (0, 1.5, 4,  6, 8, 10)
ch2 = (0,  3, 4.5, 7,  8.5, 11.5)
ch3 = ch1
ch4 = (0.5, 2, 4.5,  6.5, 8.5, 10.5)
ch5 = (-0.5, 1, 3,  4.5, 6.5, 8,  10)
lofi1 = P[ch1, ch2, ch3, ch4, ch5]
p3 >> keys(lofi1, dur=[4,4,4,2,2], amp=1)

d1 >> play(P['x---o---xx--o---'], amp=0.4)
d2 >> play('S', amp=0.15)

p9 >> nylon()
p9 >> keys()

p1.stop()

# same as above, but following strict chord def (or it did.)
# Dmin11 – Gmin7 – Dmin11 – Ebmin11 – C#dim7
ch1 = (0, 1.5, 4,  6, 8, 10)
ch2 = (3, 4.5, 7,  8.5)
ch3 = ch1
ch4 = (0.5, 2, 4.5,  6.5, 8.5, 10.5)
ch5 = (-0.5, 1, 3, 4.5)
lofi2 = P[ch1, ch2, ch3, ch4, ch5]
p3 >> keys([ch1, ch2, ch3, ch4, ch5], dur=[4,4,4,2,2], amp=[1, 1, 0.8, 0.8, 0.7])
d1 >> play(P['x---o---xx--o---'], amp=0.4)
d2 >> play('S', amp=0.15)

d1 >> play(P["x-o-"] & P[" **"])

d1 >> play("x[--]xu[--]x", sample=(d1.degree=="x"))

d1 >> play("[--][--]")

d1 >> play("<X   ><-   ><#   ><V   >")

#### something chill #####
# ace, Key in C, D F# A
lofi3 = [(-2, 0, 2, 5), (1, 4.5, 6, 8), (3, 5, 8, 10), (0, 2, 4, 6)]
p1 >> keys([(-2, 0, 2, 5), (1, 4.5, 6, 8), (3, 5, 8, 10), (0, 2, 4, 6)], dur=[5/2, 3/2, 2, 2], rate=var([1,4], [12, 4]))#
k1 >> karp(P[-2, 1, 3, 0], dur=PDur(5,8), sus=1, amp=0.5, rate=P[:32])
lofi4 = [tuple(x+2 for x in t) for t in lofi3]
print(lofi4)

p1 >> keys(lofi4, dur=4)
#k1 >> karp(P[-2, 1, 3, 0], dur=PDur(5,8)*2, sus=2, amp=0.5, rate=P[:32])

b1 >> blip(pan=var([1,-1], 4))

## 1, 2+ 3 
d1 >> play("V VV   ([ V]**)", amp=0.5)
d2 >> play("--o---o-")

Root.default.set("C")
ch1 = (3, 5.5, 6)
ch2 = (1.5, 4, 5.5)
k1 >> keys([ch1, ch2], dur=[4,4], scale=Scale.major)
k2 >> keys( [0,2,4,5,7,9,11])

Clock.reset()

print(P[:32]*(1,2))
print(PDur(5,8))



print(Clock.bpm)

