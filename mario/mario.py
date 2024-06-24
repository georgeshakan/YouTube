from wave import open
from struct import Struct
from math import floor


frame_rate = 44_100


def encode(x: float):
    i = int(x * 16384.0)
    return Struct("h").pack(i)


def play(sampler, name="mario.wav", seconds=2):
    with open(name, "wb") as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(frame_rate)
        out.setnframes(frame_rate * seconds)
        t = 0
        while t < seconds * frame_rate:
            sample = sampler(t)
            out.writeframes(encode(sample))
            t += 1


def tri(frequency, amplitude=0.3):
    period = frame_rate // frequency

    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave

    return sampler


octave = 0.5

# https://mixbutton.com/mixing-articles/music-note-to-frequency-chart/
c_freq = 261.63
e_freq = 329.63
g_freq = 392.00
a_freq = 440.00
b_freq = 493.88
b_sharp_freq = 466.16
f_freq = 349.23
d_freq = 293.66
f_sharp_freq = 369.99
d_sharp_freq = 311.13
g_sharp_freq = 415.30
e_flat_freq = 311.13
d_freq = 293.66
g_flat_freq = 369.99
a_flat_freq = 466.16
b_flat_freq = 493.88

E5 = tri(2 * e_freq * octave)
C5 = tri(2 * c_freq * octave)
G5 = tri(2 * g_freq * octave)
G4 = tri(g_freq * octave)
E4 = tri(e_freq * octave)
A5 = tri(2 * a_freq * octave)
B5 = tri(2 * b_freq * octave)
D5 = tri(2 * d_freq * octave)
F5 = tri(2 * f_freq * octave)
B5_flat = tri(2 * b_sharp_freq * octave)
A4 = tri(a_freq * octave)
B4 = tri(b_freq * octave)
B4_flat = tri(b_sharp_freq * octave)
C6 = tri(4 * c_freq * octave)
F5_sharp = tri(2 * f_sharp_freq * octave)
D5_sharp = tri(2 * d_sharp_freq * octave)
G5_sharp = tri(2 * g_sharp_freq * octave)
G4_sharp = tri(g_sharp_freq * octave)
E5_flat = tri(2 * e_freq * octave)
D3 = tri(0.5 * d_freq * octave)
G3 = tri(0.5 * g_freq * octave)
C3 = tri(0.5 * c_freq * octave)
G2 = tri(0.25 * g_freq * octave)
E3 = tri(0.5 * e_freq * octave)
F3 = tri(0.5 * f_freq * octave)
C4 = tri(c_freq * octave)
A3 = tri(0.5 * a_freq * octave)
F4 = tri(f_freq * octave)
D4 = tri(d_freq * octave)
B3 = tri(0.5 * b_freq * octave)
G3_flat = tri(0.5 * g_flat_freq * octave)
A3_flat = tri(0.5 * a_flat_freq * octave)
B3_flat = tri(0.5 * b_flat_freq * octave)


def p(t):
    """
    p is short for pause
    """
    return 0


def both(f, g):
    return lambda t: f(t) + g(t)


def chord(*args):
    return lambda t: sum(f(t) for f in args)


# https://musescore.com/user/27687306/scores/4913846
notes = [
    E5,
    E5,
    p,
    E5,
    p,
    C5,
    (E5, 2),
    (G5, 2),
    p,
    p,
    (G4, 2),
    p,
    p,
    (C5, 2),
    p,
    (G4, 2),
    p,
    (E4, 2),
    p,
    (A4, 2),
    (B4, 2),
    B4_flat,
    (A4, 2),
    (G4, 4.0 / 3),
    (E5, 4.0 / 3),
    (G5, 4.0 / 3),
    (A5, 2),
    F5,
    G5,
    p,
    (E5, 2),
    C5,
    D5,
    (B4, 2),
    p,
    (C5, 2),
    p,
    (G4, 2),
    p,
    (E4, 2),
    p,
    (A4, 2),
    (B4, 2),
    B4_flat,
    (A4, 2),
    (G4, 4.0 / 3),
    (E5, 4.0 / 3),
    (G5, 4.0 / 3),
    (A5, 2),
    F5,
    G5,
    p,
    (E5, 2),
    C5,
    D5,
    (B4, 2),
    p,
    p,
    p,
    G5,
    F5_sharp,
    F5,
    (D5_sharp, 2),
    E5,
    p,
    G4_sharp,
    A4,
    C5,
    p,
    A4,
    C5,
    D5,
    p,
    p,
    G5,
    F5_sharp,
    F5,
    (D5_sharp, 2),
    E5,
    p,
    (chord(G4, C6), 2),
    chord(G4, C6),
    (chord(G4, C6), 2),
    p,
    p,
    p,
    p,
    G5,
    F5_sharp,
    F5,
    (D5_sharp, 2),
    E5,
    p,
    G4_sharp,
    A4,
    C5,
    p,
    A4,
    C5,
    D5,
    p,
    p,
    (E5_flat, 2),
    p,
    (F5, 2),
    p,
    (C5, 2),
    p,
    p,
    p,
    p,
    p,
    p,
]


bass_notes = [
    D3,
    D3,
    p,
    D3,
    p,
    D3,
    (D3, 2),
    (G3, 2),
    p,
    p,
    (G2, 2),
    p,
    p,
    (G3, 2),
    p,
    (E3, 2),
    p,
    (C3, 2),
    p,
    (F3, 2),
    (G3, 2),
    G3_flat,
    (F3, 2),
    (E3, 4.0 / 3),
    (C4, 4.0 / 3),
    (E4, 4.0 / 3),
    (F4, 2),
    D4,
    E4,
    p,
    (C4, 2),
    A3,
    B3,
    (G3, 2),
    p,
    (G3, 2),
    p,
    (E3, 2),
    p,
    (C3, 2),
    p,
    (F3, 2),
    (G3, 2),
    G3_flat,
    (F3, 2),
    (E3, 4.0 / 3),
    (C4, 4.0 / 3),
    (E4, 4.0 / 3),
    (F4, 2),
    D4,
    E4,
    p,
    (C4, 2),
    A3,
    B3,
    (G3, 2),
    p,
    (C3, 2),
    p,
    G3,
    p,
    p,
    (C4, 2),
    (F4, 2),
    p,
    C4,
    (C4, 2),
    (F4, 2),
    (C3, 2),
    p,
    G3,
    p,
    p,
    G3,
    C4,
    p,
    p,
    p,
    p,
    p,
    p,
    (G3, 2),
    (C3, 2),
    p,
    G3,
    p,
    p,
    (C4, 2),
    (F3, 2),
    p,
    C4,
    (C4, 2),
    (F3, 2),
    (C3, 2),
    (A3_flat, 2),
    p,
    (B3_flat, 2),
    p,
    (C4, 2),
    p,
    G3,
    (G3, 2),
    (C3, 2),
]


def note(f, start, end, fade=0.01):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif end < seconds:
            return 0
        elif seconds < start + fade:
            return ((seconds - start) / fade) * f(t)
        elif end - fade < seconds:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)

    return sampler


def create_song(notes):
    song = lambda t: 0
    z = 0
    for x in notes:

        if type(x) == type((1,)):
            length = x[1]  # type: ignore
            song = both(song, note(x[0], z, z + 1.0 * length / 8))
            z += length / 8
        else:
            song = both(song, note(x, z, z + 1 / 8))
            z += 1 / 8
    return song, z


# song, total_time = create_song(notes)
# play(song, seconds=int(total_time) + 1)

song, total_time = create_song(notes)
bass, total_time = create_song(bass_notes)
final_song = both(song, bass)
play(final_song, seconds=int(total_time) + 1)
