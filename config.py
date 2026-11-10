"""VELOCITY ALBANIAN - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY ALBANIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "ALBANIAN"
HANDLE = "@velocityalbanian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "sq",
    "name": "Albanian",
    "native_name": "Shqip",
    "history_key": "albanian",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "sq-AL-IlirNeural",
    "native_fallback_voice": "sq-AL-AnilaNeural",
    "native_engine": "edge",
    "native_lang_code": "sq",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "SHQIP",
    "translit_label": "SAY IT LIKE",
    "greeting": "Përshëndetje!",
    "encouragement": "Shumë mirë!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Përshëndetje", "hand", "#1CB0F6"),
    ("Basic Phrases", "Fraza Bazë", "chat", "#58CC02"),
    ("Common Expressions", "Shprehje të Zakonshme", "chat", "#1CB0F6"),
    ("Travel", "Udhëtim", "plane", "#1CB0F6"),
    ("Restaurant", "Restorant", "fork", "#FF7A00"),
    ("Shopping", "Pazar", "bag", "#E056A0"),
    ("Emergency", "Emergjencë", "siren", "#FF4B4B"),
    ("Family Terms", "Terma Familjarë", "heart", "#E056A0"),
    ("Numbers", "Numrat", "hash", "#A560E8"),
    ("Time", "Koha", "clock", "#00A889"),
    ("Motivation", "Motivim", "rocket", "#A560E8"),
    ("Love", "Dashuri", "heart", "#FF4B4B"),
    ("Success", "Sukses", "trophy", "#F5A700"),
    ("Wisdom", "Urtësi", "book", "#A560E8"),
    ("Happiness", "Lumturi", "smile", "#F5A700"),
    ("Self Improvement", "Vetëpërmirësim", "leaf", "#58CC02"),
    ("Gratitude", "Mirënjohje", "heart", "#FF7A00"),
    ("Friendship", "Miqësi", "users", "#00A889"),
    ("Hope", "Shpresë", "sun", "#FF7A00"),
    ("Creativity", "Kreativitet", "palette", "#E056A0"),
    ("Inner Peace", "Paqe e Brendshme", "lotus", "#00A889"),
    ("Confidence", "Vetëbesim", "shield", "#1CB0F6"),
    ("Perseverance", "Këmbëngulje", "mountain", "#FF7A00"),
    ("Inspiration", "Frymëzim", "sparkles", "#A560E8"),
    ("Positive Life", "Jetë Pozitive", "sun", "#58CC02"),
    ("Courage", "Guxim", "shield", "#FF4B4B"),
    ("Kindness", "Mirësi", "heart", "#E056A0"),
    ("Patience", "Durim", "hourglass", "#00A889"),
    ("Forgiveness", "Falje", "hands", "#FF7A00"),
    ("Strength", "Forcë", "dumbbell", "#FF4B4B"),
    ("Joy", "Gëzim", "smile", "#F5A700"),
    ("Balance", "Bilanci", "scale", "#00A889"),
    ("Growth", "Rritje", "sprout", "#58CC02"),
    ("Purpose", "Qëllim", "target", "#A560E8"),
    ("Mindfulness", "Vetëdije", "lotus", "#00A889"),
    ("Daily Routine", "Rutina e Përditshme", "calendar", "#1CB0F6"),
    ("Weather", "Moti", "cloud", "#1CB0F6"),
    ("Feelings", "Ndjenjat", "smile", "#E056A0"),
    ("Food", "Ushqimi", "fork", "#FF7A00"),
    ("Health", "Shëndeti", "heart", "#58CC02"),
    ("Work", "Puna", "briefcase", "#1CB0F6"),
    ("Technology", "Teknologjia", "chip", "#A560E8"),
    ("Nature", "Natyra", "leaf", "#58CC02"),
    ("Animals", "Kafshët", "paw", "#FF7A00"),
    ("Colors", "Ngjyrat", "palette", "#E056A0"),
    ("Directions", "Drejtimet", "compass", "#1CB0F6"),
    ("Body Parts", "Pjesët e Trupit", "hand", "#00A889"),
    ("Clothes", "Rrobat", "shirt", "#E056A0"),
    ("Music", "Muzika", "music", "#A560E8"),
    ("Sports", "Sportet", "ball", "#FF7A00"),
    ("Holidays", "Festat", "gift", "#FF4B4B"),
    ("Education", "Arsimi", "book", "#1CB0F6"),
    ("Culture", "Kultura", "globe", "#00A889"),
    ("Finance", "Financat", "coin", "#58CC02"),
    ("Relationships", "Marrëdhëniet", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnalbanian",
    "#albanianlessons",
    "#albanianforbeginners",
    "#languagelearning",
    "#albanianvocabulary",
    "#velocityalbanian",
    "#dailyalbanian",
    "#albanian",
    "#learnlanguages",
    "#speakalbanian",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
