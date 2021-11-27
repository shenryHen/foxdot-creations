Scale.default='minor'
Root.default='Gb'
b4 >> space(var([8,4,6], [4,1,1]), dur=1, lpf=0) - var([0,-3], [16,4])

# major scale
a1 >> sawbass(var(P[4,6,7,7].loop(2) | P[4,6,7,7].invert(),[2]), 
    dur=PDur(3,8),
    fmod=PWhite(-1,1), amp=0.8)
