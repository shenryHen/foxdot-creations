p1 >> loop('aruarian', dur=[1], bpm=120) # plays for dur/2, repeats on dur+1 beat. loop starts on downbeat with given bpm
#                        start in bpm        how long to play in bpm
l1 >> loop('crave-you0', P[0] | P[13], dur=var([9,2],[9,2]), hpf=2000, amp=4, pshift=0, room=10, verb=7)
l2 >> loop('crave-you0', dur=14, hpf=2000, amp=4, pshift=0, room=10, verb=7, hpr=2)

# loop "the american people"
l3 >> loop('bernie-women', P[8], dur=3, lpf=600, amp=2)
# loop "women"
l3 >> loop('bernie-women', P[13], dur=2, lpf=2000, amp=2, pshift=var([0,6], 2))
# "the american people" x3 + "tired of women"
l3 >> loop('bernie-women', P[8,8,8,11], dur=[2.5, 2.5, 2.5, 3], lpf=1000, amp=2, pshift=0)
