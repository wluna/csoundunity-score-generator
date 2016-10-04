<Cabbage>
form caption("Character Sounds"), size(300, 200)
button bounds(8, 8, 60, 25), channel("jumpButton"), text("Instrument"), text("Instrument2"), hslider bounds(8, 80, 280, 30), channel("speedSlider"), text("Speed"), range(0, 1, 0)
</Cabbage>
<CsoundSynthesizer>
<CsOptions>
-n -d -m0d
</CsOptions>
<CsInstruments>
sr 	= 	48000 
ksmps 	= 	32
nchnls 	= 	1
0dbfs	=	1 

giSine ftgen 0, 0, 8192, 10, 1

;this instrument is always on and is used to trigger a once off
;jump event. Any time the channel jumpButton changes, JUMP will
;be triggered
instr TriggerInstrument
	kCurrent init 0;
	prints "debugging in csound  ";
	iArr[] array 
	
	
	;Insert output of staffOne.txt here
	
	
	;
	iArr2[] array 
	
	
	;Insert output of staffTwo.txt here
	
	
	;
	kJumpButton chnget "jumpButton"
	if changed(kJumpButton)==1 then
		event "i", "Instrument", 0, 0.5, iArr[kCurrent];
		event "i", "Instrument2", 0, 0.5, iArr2[kCurrent];
		kCurrent = kCurrent + 1;
	endif
endin

;simple jump sound
instr Instrument
	ifrq = p4
	iamp = 0.6
	kampenv linseg 0, 0.1, iamp, (p3 - 0.01), 0
	index = 3
	kindexenv linseg index, p3, 0
	aout foscil kampenv, (p4), 1, 1, kindexenv, giSine
	outs aout, aout
endin


instr Instrument2
	ifrq = p4
	iamp = 0.6
	kampenv linseg 0, 0.1, iamp, (p3 - 0.01), 0
	index = 3
	kindexenv linseg index, p3, 0
	aout foscil kampenv, (p4), 1, 1, kindexenv, giSine
	outs aout, aout
endin


</CsInstruments>
<CsScore>

;turn on the two triggering instruments
i"TriggerInstrument" 0 [3600*12]
i"PLAYER_MOVE" 0 [3600*12]

</CsScore>
</CsoundSynthesizer>
<bsbPanel>
 <label>Widgets</label>
 <objectName/>
 <x>100</x>
 <y>100</y>
 <width>320</width>
 <height>240</height>
 <visible>true</visible>
 <uuid/>
 <bgcolor mode="nobackground">
  <r>255</r>
  <g>255</g>
  <b>255</b>
 </bgcolor>
</bsbPanel>
<bsbPresets>
</bsbPresets>
