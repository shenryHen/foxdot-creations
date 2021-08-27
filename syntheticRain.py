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
p1 >> marimba([0, 2, 6, 3, 2, 4, 1, -2], dur=1/2, pan=[-1, 0.5, 0.25, -0.5, 0])
m1 >> marimba([-2,-1, 4,  -3, -2, 3,  -4, -3, 2], dur=[1/4, 1/4, 3.5])

p2 >> gong(p1.pitch + 3, dur=2)

p3 >> gong([0, 2, 4], dur=[1/2,1/2,3])

p4 >> play("x o  -o ", sample=2, amp=0.3)

p5 >> blip(p1.pitch + 2, dur=1/2, pan=p1.pan * -1)

d1.stop()

p1 >> pluck(dur=1, sus=5)
p2 >> pluck(dur=4, slide=1, slidedelay=0.5)
p3 >> pluck([0,1,2,3], dur=2, chop=3)
p2 >> pluck(-1, dur=1, tremolo=2)
#d1 >> pads(hpf=2000)
