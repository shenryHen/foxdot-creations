Clock.bpm = 135
Root.default.set('F')

z1 >> zap(var([0,2,-1,3]),dur=PDur(3,8), bits=4, fmod=(0,1))
k1 >> karp(1/4, oct=var([6,7]), sus=1) + var([0,-1,1,0])

z2 >> pluck(var([0,2, -1,3]).every(8, "stutter", cycle=8)
z1 >> zap(var([(0,2,4), (4,6,8), (5,7,9)], 4) , dur=[1, 1/2, 1/2, rest(1), 1], amp=0.5)

p1 >> pads([0,1,2,3,], dur=PDur(3,8,0,1))

p1 >> pluck(oct=[4,5,6,7]).every(4, "oct.trim", 3)
p1 >> play("x-o-").every(4, "stutter", 4, dur=Cycle([3, 2]))
p1 >> play('x-o-').every(6, "stutter", 4, dur=Cycle([3, 2]))
d1 >> play("x-o-", amp=linvar([0, 1], 8, start=now))
p1.stop()

Clock.reset()
print(Samples)
print(PatternMethods)
print(pads.get_methods())
print(Attributes)
print(Clock.bpm)

print(PEuclid(3,8)) # xxx_ xxx_ x_x_
print(PDur(3,8,0,1))
