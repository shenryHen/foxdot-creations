Scale.default.set("major")
Root.default.set("C")
Clock.bpm=96
Clock.reset()

##############################

# lofi 1 - Gmaj7, F#min7, Amin7b5
## these are all the same chord progression, just with extended chords or using different synths
k1 >> keys([(-3, -1, 1), (-3.5, -2, 0.5), (-2, 0, 1.5)], dur=[4,2,2])

ch1 = [(-3, -1, 1, 3.5, 6, 8)]
ch2 = [(-3.5, -2, 0.5,  2, 5, 7.5)]
ch3 = [(-2, 0, 1.5, 4, 5, 7, 8.5)]
p1 >> keys([ch1, ch2, ch3], dur=[4,2,2], rate=4)


lofi = [(-3, -1, 1, 3.5, 6, 8), (-3.5, -2, 0.5,  2, 5, 7.5), (-2, 0, 1.5, 4,5, 7, 8.5)]
k1 >> sinepad(lofi, dur=[4, 2,2], rate=[-10,10])

d1 >> play('----', sample=2, amp=0.6)
d2 >> play(P['V( V)  o   '], sample=5, amp=0.5)

##############################

# lofi 2 - Dmin11 – Gmin7 – Dmin11 – Ebmin11 – C#dim7
ch1 = (0, 1.5, 4,  6, 8, 10)
ch2 = (3, 4.5, 7,  8.5)
ch3 = ch1
ch4 = (0.5, 2, 4.5,  6.5, 8.5, 10.5)
ch5 = (-0.5, 1, 3, 4.5)
lofi2 = P[ch1, ch2, ch3, ch4, ch5]
p3 >> keys([ch1, ch2, ch3, ch4, ch5], dur=[4,4,4,2,2], amp=[1, 1, 0.8, 0.8, 0.7])
d1 >> play(P['x---o---xx--o---'], amp=0.4)
d2 >> play('S', amp=0.15)

##############################

lofi3 = P[
	(-2, 0, 2, 5), # A C E A
	(1, 4.5, 6, 8),
	(3, 5, 8, 10),
	(0, 2, 4, 6)
]
lofi4 = [tuple(x+2 for x in t) for t in lofi3]
lofi5 = P[
	(0, 1.5, 4, 5.5, 8, 10), 		# Cmin11 > (C, E#, G, A#, D, F)
	(0,  3, 4.5, 7, 8.5, 11, 12.5), # Fmin9 > C + ( F, G#, C, D#, G, A#)
	(0, 1.5, 4, 5.5, 8, 10), 		# Cmin11 
	(-1, 1.5, 3, 4, 6, 8.5), 		# G7#5 > (B D# F G B D# )
]
lofi6 = P[
	(1.5, 3, 4, 5.5, 8, 10, 11), # Ebmaj9 > (Eb, F, G, A#, D, F, G)
	(1.5, 4.5, 5.5, 7, 8.5, 10, 11, 12.5), # Abmaj13 > Eb + (Ab, Bb, C, Eb, F, G, Bb)
]

p1 >> keys(lofi3, rate=var([1,4], [12, 4]), dur=PDur(3,20)*2)
k1 >> karp(P[-2, 1, 3, 0], dur=PDur(5,8), sus=1, amp=0.5, rate=P[:32])


p1 >> keys(lofi3, dur=4)
#k1 >> karp(P[-2, 1, 3, 0], dur=PDur(5,8)*2, sus=2, amp=0.5, rate=P[:32])

b1 >> blip(pan=var([1,-1], 4))

print(PDur(3,20)*2)

