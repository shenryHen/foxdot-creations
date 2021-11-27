print(Scale.default)

Scale.default.set("major")
Root.default.set("C")
Clock.bpm=100

# this contains more melodies

## Aruarian Dance - Samurai Champloo

p1 >> sinepad(
	P[4,2,0,4, 3, 2] | P[-4, 4, 8, 6] | P[:4] + var([3,1,-1,-3], 1),
    dur=P[1/2, 1/2, 1/2] | P[1] | 1/2 | 1  | P[1].loop(3) | P[1/4].loop(3),
    sus=1, 
    root=4, 
    amp=1.2, 
)

p2 >> sinepad(P[:4] + var([3,1,-1,-3], 1), dur=P[1/4].duplicate(16).loop(3), sus=1/2, bpm=100)

d1 >> play(P['--------'] & (P['[xx]   x[xx]  '] | P['[xx]  [xx] [xx]x ']) & P['  o   o '], sample=0, bpm=100)

b1 >> keys([(2,4,6), (-4, -2, 0)], dur=4, bpm=100)
