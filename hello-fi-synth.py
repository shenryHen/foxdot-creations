print(SynthDefs)

### Testing grounds ###
p1 >> gong([1,3,5,7], dur=[1/3, 1/3, 1/3, 1], amp=0.5) + [0,0,0,1]
p2 >> marimba(dur=1, amp=0.8)

p2 >> pluck(pan=[-1,1])
d1 >> play("x-o-").every(4, "stutter", 8, rate=[1,2,3,4,5,6,7,8])

dur1 = [1/4, 1/4, 3.5]
m1 >> marimba([-2,-1, 4,  -3, -2, 3,  -4, -3, 2], dur=dur1)

b1 >> bass(dur=[rest(12), 1/2])
#######################

### Composition area ###
dur1 = [1/4, 1/4, 3.5]


m1 >> marimba([-2,-1, 4,  -3,-2,3,  -4, -3, 2, -2,-3,-4], dur=dur1)
m2 >> sinepad([4, 3, 2, 0], dur=4, sus=4, tremolo=2) + (0, 2, 4)
p4 >> play("ss  o   ", sample=2, amp=[0.5, 0.5, 0.2])
g1 >> gong(m1.pitch, dur=2, amp=0.6)
sp >> space(dur=[rest(15),1], sus=4)




