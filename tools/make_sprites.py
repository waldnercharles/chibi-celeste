"""Draws the project's original pixel art: a red-haired climber and an
autotiled dirt-and-snow tileset. Run: python3 tools/make_sprites.py"""
import os
from PIL import Image

ROOT = os.path.join(os.path.dirname(__file__), "..", "content", "images")
PALETTE = {
    "s": (255, 214, 170, 255),  # skin
    "e": (40, 24, 40, 255),  # eye
    "j": (70, 98, 180, 255),  # jacket
    "J": (44, 62, 128, 255),  # jacket shade
    "p": (92, 60, 54, 255),  # trousers
    "b": (38, 30, 40, 255),  # boots
    "k": (20, 16, 28, 255),  # outline
}

# 16x16 frames facing right, feet on the bottom row. The head is open at the
# top and back so the simulated hair behind the sprite shows through.
HEAD = [
    "................",
    "................",
    "................",
    "................",
    "................",
    "................",
    ".......ksssk....",
    ".......ksssek...",
    ".......kssssk...",
]
TORSO = {
    "idle": ["......kJjjjk....", ".....kJjjjjjk...", ".....ksJjjjsk...", "......kJjjjk...."],
    "reach": [".....ks.kjjk....", ".....kJjjjjjk...", "......kJjjjjk...", "......kJjjjk...."],
    "lean": ["......kJjjjjk...", ".....kJjjjjjsk..", "......kJjjjjk...", "......kJjjk....."],
}
LEGS = {
    "stand": ["......kp.kpk....", "......kp.kpk....", ".....kbb.kbbk..."],
    "stride": [".....kpk..kpk...", "....kpk....kpk..", "....kbb....kbbk."],
    "stride2": ["......kpkkpk....", ".....kpk..kpk...", ".....kbbk.kbbk.."],
    "pass": ["......kppppk....", ".......kppk.....", "......kbbbbk...."],
    "tuck": ["......kpppk.....", "......kbbbk.....", "................"],
    "spread": [".....kpk..kpk...", "....kbk....kbk..", "................"],
}


def frame(head, torso, legs, drop=0):
    rows = HEAD[:9] + TORSO[torso] + LEGS[legs]
    rows = rows[drop:] + ["." * 16] * drop if drop < 0 else ["." * 16] * drop + rows[: 16 - drop]
    while len(rows) < 16:
        rows.insert(0, "." * 16)
    return rows[-16:]


def duck():
    rows = ["." * 16] * 9 + [
        ".......ksssk....",
        ".......ksssek...",
        ".....kJjjjjjk...",
        ".....ksJjjjsk...",
        ".....kpppppk....",
        ".....kbb.kbbk...",
    ]
    return ["." * 16] + rows


FRAMES = [
    frame(HEAD, "idle", "stand"),  # 0 idle
    frame(HEAD, "idle", "stand", 1),  # 1 idle, breathing
    frame(HEAD, "lean", "stride"),  # 2 run
    frame(HEAD, "lean", "pass", 1),  # 3 run
    frame(HEAD, "lean", "stride2"),  # 4 run
    frame(HEAD, "lean", "pass", 1),  # 5 run
    frame(HEAD, "reach", "tuck"),  # 6 jump
    frame(HEAD, "idle", "spread"),  # 7 fall
    frame(HEAD, "lean", "spread"),  # 8 dash
    frame(HEAD, "reach", "stand"),  # 9 climb
    frame(HEAD, "reach", "pass"),  # 10 climb
    duck(),  # 11 duck
]


def put(img, ox, rows):
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c != ".":
                img.putpixel((ox + x, y), PALETTE[c])


def climber():
    img = Image.new("RGBA", (16 * len(FRAMES), 16))
    for i, rows in enumerate(FRAMES):
        put(img, i * 16, rows)
    img.save(os.path.join(ROOT, "climber.png"))


DIRT = [(107, 74, 58, 255), (128, 92, 70, 255), (88, 60, 50, 255)]
EDGE = (62, 40, 40, 255)
SNOW = [(236, 242, 255, 255), (190, 206, 240, 255)]


def tile(mask):
    """mask bits: 1 open above, 2 open left, 4 open right, 8 open below."""
    t = Image.new("RGBA", (8, 8))
    for y in range(8):
        for x in range(8):
            n = (x * 7 + y * 13 + (x * y) % 5) % 9
            t.putpixel((x, y), DIRT[1] if n == 0 else DIRT[2] if n == 1 else DIRT[0])
    for i in range(8):
        if mask & 2:
            t.putpixel((0, i), EDGE)
        if mask & 4:
            t.putpixel((7, i), EDGE)
        if mask & 8:
            t.putpixel((i, 7), EDGE)
    if mask & 1:
        for x in range(8):
            t.putpixel((x, 0), SNOW[0])
            t.putpixel((x, 1), SNOW[0] if (x + mask) % 3 else SNOW[1])
            if (x * 5 + mask) % 4 == 0:
                t.putpixel((x, 2), SNOW[1])
    return t


def tileset():
    img = Image.new("RGBA", (8 * 16, 8))
    for mask in range(16):
        img.paste(tile(mask), (mask * 8, 0))
    img.save(os.path.join(ROOT, "tiles.png"))


climber()
tileset()
