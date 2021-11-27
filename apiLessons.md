# drum beats
1. `P[].layer("mirror")`
plays the last sound twice
	
1. `play()` Params
`play(... , pan=(-1,1), dur=PDur(5,8), rate=var())`
	1. pan: pans the sound from right to left, 0 being center
	1. PDur: creates a duration array, based on PEuclid(5,8). useful for interesting "double beat" rythems
	1. rate: sets the playback rate
	1. lpf: low pass filter - filters out frequencies above a given freq
	1. formant: muffles. technically called a resonance filter
	1. shape: 
	1. fmod: adds x val to original frequency and plays it over another channel, x = 20, plays 440 and 460
	1. crush
	1. tremolo: modulates the amplitude x times in a beat
	1. pshift
	1. blur: tie notes
	1. delay: starts the synth after x beats

# Pattern methods learned
1. `arp([0,1,2])`
1. `reverse()`
1. `layer('inverse')`
1. `inverse()`
1. `stutter(3)`
1. `splice()`
1. `replace(note, replaceWith)`
1. `amen()`

# Pattern funcions
1. `PDur(3,8)`
1. `PEuclid(7,16)`
1. `PEuclid2(7,16, 'p', 'P')`
1. `PSum(5,4)`, Returns a Pattern of length n whose sum is equal to total and each value is roughly equal. All values are divisible by lim, which is also the smallest possible value for each element.
1. `PBern(8)`
1. `PBeat('x xxx x')`
1. `PWhite(x, y)`, returns floating point nums in range (x,y)
1. `PStep(4, (0,9), 0)`

# foxdot tips
## echo
```python 
# We don't hear any echo effect
d1 >> play("x-o-", dur=1, echo=0.75)

# Add reverb and we do
d1 >> play("x-o-", dur=1, echo=0.75, room=0.5)
```

## stop call
```python

p1 >> pluck().every(4, 'stutter', 4)

p1.stop_calling('stutter')
```

# music theory
1. diminshed triad chord: 3rd is dim, tonic + 3/2 steps + 5th
1. verse-chorus songwriting formats
	1. ABAB
	1. AABA
	1. ABABCB
	1. ACAB?

1. You dont need to go up and down a scale. repeating notes in quick succession is fine.	
1. PDur(5,8) = P[0.5, 0.25, 0.5, 0.25, 0.5]

# lofi chords
1. Dmin11 – Ebmin11: (D, F, A, C, E, G) + (Eb, Gb, Bb, Db, F, Ab)
2. Dmin11 – Gmin7 – Dmin11 – Ebmin11 – C#dim7: 
	(D, F, A, C, E, G) + (G, A#, D, F) + Dmin11 + (Eb, Gb, Bb, Db, F, Ab) + (C#, E, G, A#)
3. Gmaj7, F#min7, Amin7b5
4. Cmin11 -Fmin9 – Cmin11 – G7#5

# FoxDot and SC setup
print(Player.get_attributes())

## Changing SC output
1. make sure SC server is off and foxdot is off. SC server can technically be on, but it might introduce complecations
1. print outputs 
	```
	ServerOptions.outDevices
	for (0,4, {arg i; (i + ServerOptions.outDevices[i]).postln})
	```
1. set output 
```
Server.default.options.outDevice_(ServerOptions.outDevices[i])
```
1. start server or reboot server.
1. start foxdot

## semi-edm lesson

k1 >> spark(
    P[var.keys],
    amp=3/4,
    oct=[7, 5],
    dur=[1/4, 1/4, 1/2]    
)
k2 >> spark(
    P[var.keys, 2] + (0,4),
    amp=1,
    oct=[(4,5), (4,6)],
    dur=PDur(var([[3,5], 7]),8 )    
)