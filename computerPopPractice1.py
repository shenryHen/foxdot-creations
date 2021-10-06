# G maj 7, F#min7, Abmin7bpf
Clock.bpm = 200

d1 >> play(': ::: ::', amp=0.6)
d2 >> play('PppPp           ', amp=0.4, sample=6)
d3 >> play('d  d  d   d d   ', amp=1)
#p3 >> play('d  d  d   d d   ', amp=0.3, bpm=200)

Root.default.set('F')

m1 >> marimba(
    [ (-1, 1), (-4, 3), (0, 2), (-3, 4)],
    dur=[1.5, 0.5, 1, 1],
    amp=1.3,
    )

m2 >> marimba(
    P[1, 2, 6, 7 ].rotate(3),
    dur=PDur(4,6)*3,
    root=5,
    amp=2
)

m3 >> marimba( (5, 7, 9), dur=1/4)

m1.stop()
m2.stop()
m3.stop()
print(PDur(4,7)*2)
















p1 >> sinepad( [ 
    (-3, -1, 1, 3.5, 6, 8), 
    (-3.5, -2, 0.5, 2, 5, 7.5),
    (-2, 0, 1.5, 4, 5, 7, 8.5), # Ab, C, D#, G, A C D#
    (1.5, 3.5, 5.5), # Fb min 11
  ], dur=[4,8], rate=P[:16, 2], root=[4,4,5,4], amp=0.8) 
  
p2 >> blip( dur=4, sus=4, 
            root=var([4, 5], [16, 4], rate=var([5, 10], [16,4]), amp=0.7 )
        )
  
d1 >> play('[xx]-o--(-x)o-', bpm=Clock.bpm)
d2 >> play('O       ', amp=0.1)

d1.stop()
d2.stop()

d2.stop()
p1.stop()
p2.stop()

print(PDur(4,5)* 2)









