Clock.bpm = 135
Root.default.set('F')

z1 >> zap(var([0,2,-1,3]),dur=PDur(3,8), bits=4, fmod=(0,1))
k1 >> karp(1/4, oct=var([6,7]), sus=1) + var([0,-1,1,0])

z2 >> pluck(var([0,2, -1,3]).every(8, "stutter", cycle=8)
z1 >> zap(var([(0,2,4), (4,6,8), (5,7,9)], 4) , dur=[1, 1/2, 1/2, rest(1), 1], amp=0.5)



p1 >> play("x-o-").every(4, "stutter", 4, dur=Cycle([3, 2]))
p1 >> play('x-o-').every(6, "stutter", 4, dur=Cycle([3, 2]))
d1 >> play("x-o-", amp=linvar([0, 1], 8, start=now))
p1.stop()

#################################################E Experimental ##########################################################################
d1 >> play('x-o[---]', dur=1)
d1 >> play('x--(o)-(-(xo))o-')

p1 >> pluck(oct=[0,5,6,7]).every(4, "oct.trim", 3)

p2 >> pads(dur=1/4, oct=var([6,7]), sus=1) + var([0,-1,1,2])

b1 >> dirt(var([0,-1,3,2], dur=PDur(3,8)), bits=4, lpf=100, fmod=(0,1))

d1 >> play(P['x[-x]o--xo(-(D)-[DD]))'],
        sample=2,
        amp=0.5
    )
    
d2 >> play(PZip("Vs", "  n "), sample=2, amp=0.3, hpf=var([10,200],[28,4])).every(3, 'stutter', dur=1)

print(PZip("Vs"," on "))

########################################################################################################################################
# PDur, var([],[]), + var([]), play(()())

p2 >> pads(dur=PDur(5,7), oct=var([5,7]), sus=1)

p1 >> karp(var([ 8, 4, 3, 6, 5], dur=PDur(5,16))).every(8, 'stutter', 4, dur=1) 

b1 >> dirt(var([-1,4,3,2]), lpf=100, fmod=(0,1))

d1 >> play('x[--]o[--](x(o))xo([--]x)')

d2 >> play('x--(-o(oD)--xoxo') # not that great

d2 >> play(PZip("Vs", "  qq"), amp=0.3, hpf=var([10, 2000], [12, 4]))

p2.stop()

d1.stop()
p1.solo(0)

#######################################################################################################################################
Clock.reset()
print(Samples)
print(PatternMethods)
print(pads.get_methods())
print(Attributes)
print(Clock.bpm)

print(PDur(5,16))
