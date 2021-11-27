#melodies 
p2 >> pluck([3,0,4,5], dur = [1/4, 1/4, 1/2])
p2 >> pluck(var([3,0,1,5,2], [4,2]))

p2 >> pluck([3,0,4,5], dur = [1/4, 1/4, 1/4, 1/4])
p2 >> pluck(var([7,4,3,1],4))

p3 >> pluck(var([3,0,5,4],4), dur=[1,1,1,1/4,3/4])

# harmonies
p1 >> keys(var([(-4,-2, 0), (1, 3, 5)], 4), dur=[3/4, 3/4, 1, 1/2, 1]) 
k1 >> keys(P[(-4,-2, 0)].loop(3) | P[(1,3,5)].duplicate(3) | P[3,2,3,2],
     dur=P[3/4, 3/4, 1, 1/2, 1] | P[3/4, 3/4, 1/2, 1/4, 1/4, 2/4, 1])
d1 >> play('X  Xo ++', amp=[2, 1], sample=6) 
f1 >> swell([0,1], sus=4,
dur=4, amp=0.5, root=2)
#>  >   >   >   > >
#rlrl rlrl rlrl rlrl
print(Clock.bpm)
Clock.bpm = 100

'''
o--o --o- --o- o---
o--o --o- --oo oo--
'''

