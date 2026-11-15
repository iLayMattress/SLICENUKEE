"""Route FL Studio's per-note Fine Pitch to SLICENUKE as per-note Mod X.

Use this as a VFX Script before SLICENUKE inside Patcher. Set SLICENUKE's
MOD X Target to Pitch +/-12st and enable polyphonic aftertouch in its wrapper.
The incoming MIDI key remains unchanged, so it continues to select the slice.
"""

import flvfx as vfx


class SLICENUKEVoice(vfx.Voice):
    parentVoice = None


def route_fine_pitch(output_voice, source_voice):
    output_voice.copyFrom(source_voice)
    output_voice.note = source_voice.note
    output_voice.finePitch = 0.0
    output_voice.fcut = max(-1.0, min(1.0, source_voice.finePitch / 12.0))


def onTriggerVoice(incomingVoice):
    voice = SLICENUKEVoice(incomingVoice)
    voice.parentVoice = incomingVoice
    route_fine_pitch(voice, incomingVoice)
    voice.trigger()


def onTick():
    for voice in vfx.context.voices:
        if voice.parentVoice is not None:
            route_fine_pitch(voice, voice.parentVoice)


def onReleaseVoice(incomingVoice):
    for voice in vfx.context.voices:
        if voice.parentVoice == incomingVoice:
            voice.release()


def createDialog():
    return vfx.ScriptDialog(
        "SLICENUKE Fine Pitch",
        "Routes each FL note's Fine Pitch to SLICENUKE pitch while preserving its slice key."
    )
