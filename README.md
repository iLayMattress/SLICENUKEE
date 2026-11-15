So basically u can run this thing anyhow... it doesn't really matter, but if you want the FL STUDIO PER-NOTE-PITCH controls, you can use a little patcher patch to do that. I think you also need to be on fl studio vers 24 or more recent? I think if you're on a really late version of 21 it should still work but it's not guaranteed.


uhhh so to get that started just copy the SLICENUKE.vst3 folder, SLICENUKE.lib, and SLICENUKE.exp, to your vst 3 folder wherever that is yup do that right now its a good idea.

ok now that you've most likely done that since you're reading this next line, open fl studio and open SLICENUKE ykwim? do like, your channel rack thingy... no clue what its called... and then after you do that right click on it and select "patcherize". 
Once that's done it'll be connected like "from fl studio -> SLICENUKE -> To FL Studio". Right click and add vfx script, open it, and under the script tab, will be the uhhh script.
Basically u want to replace that script with the script inside of SLICENUKE VFX Fine Pitch.py

Then hit compile ok? ok. after it compiles (if it didn't I have no way to help you idk try again to copy and paste it make sure ur not missing any characters or something idfk man), just connect from fl studio to it, and then connect it to SLICENUKE (make sure you had disconnected slicenuke from- "from fl studio" as well so its only getting input from VFX Script).

okok its almost done, open slicenuke and open settings and then uh under the midi section make sure "send note release velocity", "Send MOD X as polyphonic aftertouch" and "send all notes off when playback stops" are enabled

then well it should work. I'd recommend saving this as a patcher preset so each time you want to use this beast you can just open a patcher preset instead of manually setting it up.

And if it doesn't work fuck. I'm sorry bro. I have no clue.

ok have funn!!!

Also if this fl or whatever daw for whatever reason decides to not read ts as a plugin or whatever try disabling “smart app control” in windows security.
