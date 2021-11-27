Scale.default.set("major")
Root.default.set("C")
Clock.bpm=248


# low F = -4, high F = +3
# same rhythm in cut time
# proper merengue rhythm

# keep claves at sample = 4 or 0, tambales = 6
m1 >> play(': ::: ::', amp=0.1)
t1 >> play(P['P '] | P['  '].duplicate(3) | P['  '].duplicate(2) | P['pPPp'], amp=0.5, sample=2, bpm=248)
c1 >> play(P['d  d  d   d d   '], sample=4, bpm=248)


############# prod music ################# 
# better pecussion pattern
## pattern concatted

c1 >> play(P['d  d  d   d d   '], sample=4)

t1 >> play(P['P '] | P['  '].duplicate(3) | P['  '].duplicate(2) | P['pPPp'], amp=0.5, sample=2)

m1 >> play(': ::: ::', amp=0.1)

# 1/2 = quarter note
# 1/4 = eigth noto
pattern = [rest(1/8),      1,    0.5, rest(1/8),      1,    0.5,        1,       1,       1, rest(1/8),     0.5,]   
k1 >> marimba(
        [       99, (-1,1), (-4,3),        99, (-1,1), (-4,3),  (-3, 4), (-1, 1), (-4, 3),        99, (-3, 4),         99, (0, 2), (-2, 5),        99, (0, 2), (-2, 5),  (-3, 4), (0,2), (-2, 5),        99, (-3, 4)], 
    dur=[rest(1/4),    1/2,    1/4, rest(1/4),    1/2,    1/4,      1/2,     1/2,     1/2, rest(1/4),     1/4,  rest(1/4),    1/2,     1/4,  rest(1/4),    1/2,    1/4,      1/2,   1/2,     1/2, rest(1/4),    1/4], 
    sus=P[0, 1, 0.5, 0,  1, 0.5, 1, 1, 1, 0, 0.5, 0, 1, 0.5, 0, 1, 0.5, 1, 1, 1, 0, 0.5 ],
    root=5,
    amp = 1,
)


##############################
# Todo: learn random note selection and generation, also learn more pattern methods
m1 >> marimba(
    [ (-1, 1), (-4, 3), (0, 2), (-3, 4)],
    dur=[rest(1/4)] | PDur(13,15)*2,
    amp=1.3,
    bpm=Clock.bpm
)

## not really merengue, but like a walking carnival theme
m2 >> marimba(
    P[(-1,1) , (2,6), (-3,2.5), (1, 8)].splice(P[(-1, 1), (-4, 3), (-3, 4)]),
    dur=[rest(1/4)] | PDur(2,7),
    root=5,
    amp=1,
    bpm=238
)
