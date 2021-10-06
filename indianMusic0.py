Clock.meter = (2,2)
Clock.bpm = 200
Root.default.set('C')

p1 >> sitar(P[0, 1, 1, 1, 1, 1, 1, 1].loop(3), dur=[1/2], slide=[0, 0, 0, 0], root=8)
    

print(P[[-1], P[2, 2, 2]].loop(2))
print(P[0] |  P[1, 1, 1].loop(3))

AMP = 0.7
BASS_AMP    = [AMP]*8
BASS_RYTHM  = [  1, 1/2, 1/2, rest(1)]*2
BASS_CHORD1 = (-3, 5)
BASS_CHORD2 = (0, 7)
BASS_CHORD3 = (2, 9)
p1 >> dbass( P[P[BASS_CHORD1,BASS_CHORD1,BASS_CHORD1,0].loop(3) |
             P[BASS_CHORD2,BASS_CHORD2,BASS_CHORD2,0]].loop(4) | 
             P[P[BASS_CHORD1,BASS_CHORD1,BASS_CHORD1,0].loop(2) |
             P[BASS_CHORD3,BASS_CHORD3,BASS_CHORD3,0].loop(2)].loop(2),
             dur=BASS_RYTHM,
             amp=BASS_AMP
)



