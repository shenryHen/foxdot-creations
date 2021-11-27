Scale.default='minorPentatonic'
Clock.bpm = 125

	
################################ A section ################################
a1 >> loop('crave-you0', dur=32, hpf=2000, amp=3, pshift=0, room=10, verb=7)
a2 >> keys(var.keys, dur=PDur(3,8), root=-5, chop=0.5, lpr=2, rate=2, amp=1)

a3 >> sinepad(P[3,5,6,7,6,5].arp([2,3,4,0]), dur=1/4, sus=1, root=0, amp=0.75)
a5 >> blip(a4.pitch, dur=[1/2, 3/2], oct=var([5],4), room=4, verb=3)

a4 >> sawbass(P[5,3,3.5,4].loop(2) | P[4,6,7,7].invert(),
    dur=[2,2,4],
    fmod=PWhite(-1,1), amp=0.8)

a9 >> play(P['x-o-'].amen(), sample=7, amp=0.75, lpf=0)

################################ B Section ################################
l1 >> loop('crave-you0',
    P[0] | P[5.5][:7] | P[14][:4] | P[29][:4], 
    dur=P[5.5] | P[1][:7] | P[1][:7] | P[0.5], 
    hpf=1800, amp=6, pshift=var([0,4,2], [10,4,6]))
    

l1 >> loop('crave-you0',
    P[0][:9] | P[5.5][:7] | P[14][:4] | P[29][:4], 
    dur=P[1][:9] | P[1][:7] | P[1][:7] | P[0.5], 
    hpf=1800, amp=3, pshift=var([0,4,2], [10,4,6]))
    
l2 >> loop('bernie-women', P[8+6-1], dur=2, lpf=2000, amp=3, pshift=var([0,6], 2))

p1 >> spark(P[0,1,2,3, 4,5,1,5][:4].loop(4) | P[3,2,1,0][:1] | P[4,3,1,3].invert().loop(3), dur=1/4, oct=7, amp=linvar([0.4, 1.5], 20))
k3 >> dub(var([var([0,5], [0, 11]), 3, 5, 4, 2,], 4), dur=2, echo=1, chop=2, room=2, oct=5, fmod=1, amp=1)
d1 >> play('<x   x[xx]  ><--------><  o   [o ][oo]>', sample=7, amp=2)


############################## C section ##################################
c1 >> loop('crave-you0',
    P[0] | P[5.5][:7] | P[14][:4] | P[29][:4], 
    dur=P[5.5] | P[1][:7] | P[1][:7] | P[0.5], 
    hpf=1800, amp=6, pshift=var([0,4,2], [10,4,6]))
    
c6 >> loop('bernie-women', P[13], dur=2, lpf=600, amp=2, pshift=var([5,6, 10],[4,2,2]))
c6 >> loop('bernie-women', P[8], dur=8, lpf=600, amp=2, pshift=var([5,6, 10],[4,2,2]))

    
c2 >> blip(P[3,5,6,7,6,5].arp([2,3,4,0]), dur=1/4, sus=1, root=0, amp=0.3, formant=1)
c2 >> sinepad(P[3,5,6,7,6,5].arp([2,3,4,0]), dur=1/4, sus=1, root=0, amp=0.3, formant=1, hpf=var([0, 1000],[16,4]))

c4 >> blip(c3.pitch, oct=6, room=3, formant=0)

c3 >> sawbass(P[2.5,2.5,2.5,2.5][:3] | P[5,7,7,5],
    dur=[1,],
    fmod=PWhite(-1,1), amp=0.8, echo=0, delay=0,)
                            
c9 >> play('<VV VOVOO><---->', sample=0, dur=1/2)


############################### A section - return ########################
a1 >> loop('crave-you0', dur=32, hpf=2000, amp=3, pshift=0, room=10, verb=7)

a3 >> sinepad(P[3,5,6,7,6,5].arp([2,3,4,0]), dur=1/4, sus=1, root=0, amp=0.3, formant=1)

a4 >> sawbass(P[5,3,3,4].loop(2) | P[2,0, 2,0,0,0],
    dur=P[2,2,4,4] | P[2,2, 1,1,1,1],
    fmod=PWhite(-1,1), amp=0.8, echo=0, delay=16)
a4 >> dub(var([var([0,5], [0, 11]), 3, 5, 2, 1, 3], 4), dur=2, echo=1, chop=2, room=2, oct=5, fmod=1, amp=0.5)
a5 >> play('<x  xo xx  x o   ><- - >', dur=1/4)

# use this to close out
@nextBar
def trans2():
    c_all.stop()


########################### NEW SONG #####################################

Scale.default='majorPentatonic'
Root.default='C'

l0 >> loop('bernie-women', P[13], dur=2, lpf=600, amp=2, pshift=var([5,6, 10],[4,2,2])) # starter

l1 >> loop('bernie-women', P[8,8,8,11], dur=[2.5, 2.5, 2.5, 3], lpf=1000, amp=2, pshift=0)
l2 >> loop('bernie-women', P[13.25], dur=2, lpf=600, amp=4, pshift=var([5,6, 10],[4,2,2]))

a1 >> sinepad(P[3,5,6,7,6,5].arp([2,3,4,0]), dur=1/4, sus=1,root=0, amp=0.3, formant=1)
a2 >> blip([0,0,0,0,  5,5,4,4,],dur=[1/2,3/2], sus=2, amp=2)
a3 >> jbass(a6.pitch, dur=[1/2,3/2], sus=1, amp=1.4)

a9 >> play('<x  xo xx  x o   ><- - >', dur=1/4)
