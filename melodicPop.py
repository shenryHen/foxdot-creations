Scale.default = 'minor'
Scale.default = 'majorPentatonic'
Scale.default = 'dorian'
Clock.bpm=120

var.chords = var([0,2,3], 8)

l2 >> loop('bernie-women', P[80:86], amp=2, rate=1.5)
p1 >> gong(P[var.chords, 4, 6, 7][:6], dur=PDur(3,8)*2, amp=3)
p2 >> bell(var.chords + var([(0,2), (2,4)]), dur=[1, 1/2], amp=0.5)
p3 >> sawbass(var.chords + var([0,5],16), dur=PDur(5,8), cutoff=linvar([100, 10000], 30), amp=linvar([0.5, 0.8], 20), fmod=PWhite(-1, 1))

p4 >> prophet(P[3,2, var.chords].loop(4) | P[var([4,6])].stutter(4), dur=1/4, hpf=linvar([0,2000], [16,0]),
    hpr=linvar([0.1, 1], 25),   
    formant=var([0,4], [6,2]))

# p4 alt
p4 >> prophet(P[3,2, var.chords].loop(3) | P[var([4,8,0,-2],4)].stutter(4), dur=1/4,
    hpf=000)
    
d1 >> play('x[ [xn]]< h>', sample=2, dur=2)
d2 >> play('- -- - -- ', dur=1/4)

b1 >> pluck(P[0,P[6,4,7]], dur=PDur(3,8), sus=2, coarse=4)
b2 >> bass(var([0,-2,0,3],8), dur=PRand([1, 1/2]), shape=0.2)

# todo
# 1. use viola() for soft melodic long tones, with blur=1.5 param
# 2. try using PDur(3,8)*2 for dur
# 3. use p1.pitch in synths to share pitch with melodies
# 4. use '<>' in drum synths
# 5. use var.chords and concat with new notes
# 6. + PStep(4, (0,9),0)

a4 >> bell(P[var.chords] | P[var([5,5,6],[2,1,2])], dur=P[0.25].loop(3) | PDur(3,8) | P[1], formant=var([2,0], [16,16]), hpf=var([100, 1000],8))
a3 >> karp([0,2,4,6], dur=1/4, echo=4, sus=4, hpf=80, amp=0.8) + PStep(1, (var.chords,var.chords+2),0)
a2 >> play('<- - ><x xxo     xxo ( o(x)) >', dur=1/4, sample=(2,4), amp=0.8, hpf=100, room=0.5)
a5 >> play('<  % >< * **>', room=0.5)



#########################################
### more like melodic background music

Clock.bpm=100

p1 >> bell(P[var([var([7,5], 16,4)  ,2,6,1],[6,2])], dur=[1/2,3/2], root=5, chop=0.5, formant=2, amp=0.68)
p2 >> sawbass(p1.pitch, dur=2, root=2, fmod=PWhite(-1,1), rate=1.2, amp=var([1,0.8],[2,2]))
p3 >> viola(P[0,6,1,7].loop(2) | P[-1,4,0,1][:2], blur=1.5, dur=PDur(3,8) | PDur(5,8), amp=1.2, rate=1.2, shape=1.2, hpf=5000)
p4 >> sinepad(p1.pitch, dur=8, sus=8, amp=0.8, root=var([4,5],8))
d1 >> play('<----><xx  o   xoxxo   >', sample=0, hpf=00, dur=1/4)


nextBar(a_all.stop())

a1 >> bell(P[var([var([7,5], 16,4)  ,2,6,1],[6,2])], dur=[1/2,3/2], root=5, chop=0.5, formant=2, amp=0.68)
a2 >> keys([99, (a1.pitch, a1.pitch+2, a1.pitch+4), ], dur=[rest(1/2),1,])
a3 >> play('<--><m o[mm][%%] o >< **>')
a4 >> karp(P[P[0,1,2].arp([5,6])].loop(4) | P[7,9,8,9], dur=P[1/4][:8] | PDur(3,8), hpf=200, shape=0.4)
##########################################


b1 >> bass(var([p2.pitch + 5, p2.pitch], 4)
p2 >> bell(formant=var([0.9, 0.1],1), cut=0.5)
p4 >> star(b1.pitch, dur=PDur(3,8)*2 | PDur(5,8)*2,rate=2,shape=2,amp=0.5)
p2 >> sawbass([0], root=var([4,0],4), delay=(0, 0.25), room=0.5, formant=2)

#########################################
nextBar(Clock.clear)
nextBar(a_all.stop())
nextBar(a1.only())

d_all.stop()