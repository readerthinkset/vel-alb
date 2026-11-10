"""AI phrase generation with permanent no-repeat history."""

from __future__ import annotations

import json
import random
import time
from datetime import datetime

import requests

import config
from config import CATEGORIES, CATEGORIES_NATIVE, HISTORY_DIR, MAX_RECENT_CATEGORIES

PHRASE_HISTORY_FILE = HISTORY_DIR / "all_generated_phrases.json"
RECENT_CATEGORIES_FILE = HISTORY_DIR / "recent_categories.json"

PHRASE_KEY = config.LANGUAGE["history_key"]
LANGUAGE_NAME = config.LANGUAGE["name"]
NATIVE_NAME = config.LANGUAGE["native_name"]

# ==== FALLBACK PHRASES START ====
FALLBACK_PHRASES = [
    {"english": "Hello, nice to meet you.", "native": "Përshëndetje, kënaqësi të njihemi.", "transliteration": "Përshëndetje, kënaqësi të njihemi."},
    {"english": "Thank you very much.", "native": "Faleminderit shumë.", "transliteration": "Faleminderit shumë."},
    {"english": "Good morning, have a great day.", "native": "Mirëmëngjes, kalofsh një ditë të mbarë.", "transliteration": "Mirëmëngjes, kalofsh një ditë të mbarë."},
    {"english": "I love learning new languages.", "native": "Më pëlqen të mësoj gjuhë të reja.", "transliteration": "Më pëlqen të mësoj gjuhë të reja."},
    {"english": "Never give up on your dreams.", "native": "Mos u dorëzo kurrë nga ëndrrat e tua.", "transliteration": "Mos u dorëzo kurrë nga ëndrrat e tua."},
    {"english": "Every day is a fresh start.", "native": "Çdo ditë është një fillim i ri.", "transliteration": "Çdo ditë është një fillim i ri."},
    {"english": "Believe in yourself always.", "native": "Besoni gjithmonë në vetvete.", "transliteration": "Besoni gjithmonë në vetvete."},
    {"english": "Small steps lead to big changes.", "native": "Hapat e vegjël çojnë në ndryshime të mëdha.", "transliteration": "Hapat e vegjël çojnë në ndryshime të mëdha."},
    {"english": "You are stronger than you think.", "native": "Je më i fortë nga sa mendon.", "transliteration": "Je më i fortë nga sa mendon."},
    {"english": "Happiness is a choice, choose it.", "native": "Lumturia është një zgjedhje, zgjidhe atë.", "transliteration": "Lumturia është një zgjedhje, zgjidhe atë."},
    {"english": "What time is it please.", "native": "Sa është ora, ju lutem.", "transliteration": "Sa është ora, ju lutem."},
    {"english": "Where is the train station.", "native": "Ku është stacioni i trenit.", "transliteration": "Ku është stacioni i trenit."},
    {"english": "How much does this cost.", "native": "Sa kushton kjo.", "transliteration": "Sa kushton kjo."},
    {"english": "Can you help me please.", "native": "Mund të më ndihmoni, ju lutem.", "transliteration": "Mund të më ndihmoni, ju lutem."},
    {"english": "I would like a coffee please.", "native": "Do të doja një kafe, ju lutem.", "transliteration": "Do të doja një kafe, ju lutem."},
    {"english": "The food is delicious today.", "native": "Ushqimi është i shijshëm sot.", "transliteration": "Ushqimi është i shijshëm sot."},
    {"english": "Have a wonderful weekend.", "native": "Kaloni një fundjavë të mrekullueshme.", "transliteration": "Kaloni një fundjavë të mrekullueshme."},
    {"english": "Take care of yourself.", "native": "Kujdesuni për veten tuaj.", "transliteration": "Kujdesuni për veten tuaj."},
    {"english": "See you tomorrow my friend.", "native": "Shihemi nesër mik.", "transliteration": "Shihemi nesër mik."},
    {"english": "The weather is beautiful outside.", "native": "Motit është i bukur jashtë.", "transliteration": "Motit është i bukur jashtë."},
    {"english": "I am very happy today.", "native": "Jam shumë i lumtur sot.", "transliteration": "Jam shumë i lumtur sot."},
    {"english": "Learning a language opens new doors.", "native": "Të mësosh një gjuhë hap dyer të reja.", "transliteration": "Të mësosh një gjuhë hap dyer të reja."},
    {"english": "Keep practicing every single day.", "native": "Vazhdoni të praktikoni çdo ditë.", "transliteration": "Vazhdoni të praktikoni çdo ditë."},
    {"english": "You can achieve anything you want.", "native": "Mund të arrish gjithçka që dëshiron.", "transliteration": "Mund të arrish gjithçka që dëshiron."},
    {"english": "Rest when you are tired.", "native": "Pushoni kur jeni të lodhur.", "transliteration": "Pushoni kur jeni të lodhur."},
    {"english": "Focus on the positive things.", "native": "Fokusohuni te gjërat pozitive.", "transliteration": "Fokusohuni te gjërat pozitive."},
    {"english": "Learn from your mistakes.", "native": "Mësoni nga gabimet tuaja.", "transliteration": "Mësoni nga gabimet tuaja."},
    {"english": "Trust the process completely.", "native": "Besoni procesin plotësisht.", "transliteration": "Besoni procesin plotësisht."},
    {"english": "Breathe deeply and stay calm.", "native": "Merrni frymë thellë dhe qëndroni të qetë.", "transliteration": "Merrni frymë thellë dhe qëndroni të qetë."},
    {"english": "Enjoy the little moments in life.", "native": "Shijoni momentet e vogla në jetë.", "transliteration": "Shijoni momentet e vogla në jetë."},
    {"english": "Smile more, worry less.", "native": "Buzëqeshni më shumë, shqetësohuni më pak.", "transliteration": "Buzëqeshni më shumë, shqetësohuni më pak."},
    {"english": "Be kind to everyone you meet.", "native": "Jini të sjellshëm me këdo që takoni.", "transliteration": "Jini të sjellshëm me këdo që takoni."},
    {"english": "Help others without expecting anything back.", "native": "Ndihmoni të tjerët pa pritur asgjë në këmbim.", "transliteration": "Ndihmoni të tjerët pa pritur asgjë në këmbim."},
    {"english": "Forgive yourself and move forward.", "native": "FALNI veten dhe ecni përpara.", "transliteration": "FALNI veten dhe ecni përpara."},
    {"english": "Stay strong in difficult times.", "native": "Qëndroni të fortë në kohë të vështira.", "transliteration": "Qëndroni të fortë në kohë të vështira."},
    {"english": "Every moment is a new beginning.", "native": "Çdo moment është një fillim i ri.", "transliteration": "Çdo moment është një fillim i ri."},
    {"english": "Listen to your heart always.", "native": "Dëgjoni gjithmonë zemrën tuaj.", "transliteration": "Dëgjoni gjithmonë zemrën tuaj."},
    {"english": "Do what makes you happy.", "native": "Bëni atë që ju bën të lumtur.", "transliteration": "Bëni atë që ju bën të lumtur."},
    {"english": "Your potential is unlimited.", "native": "Potenciali juaj është i pakufishëm.", "transliteration": "Potenciali juaj është i pakufishëm."},
    {"english": "Be brave and take risks.", "native": "Jini të guximshëm dhe merrni rreziqe.", "transliteration": "Jini të guximshëm dhe merrni rreziqe."},
    {"english": "Celebrate your progress every day.", "native": "Festoni përparimin tuaj çdo ditë.", "transliteration": "Festoni përparimin tuaj çdo ditë."},
    {"english": "Surround yourself with good people.", "native": "Rrethoni veten me njerëz të mirë.", "transliteration": "Rrethoni veten me njerëz të mirë."},
    {"english": "Read books and grow your mind.", "native": "Lexoni libra dhe rritni mendjen tuaj.", "transliteration": "Lexoni libra dhe rritni mendjen tuaj."},
    {"english": "Travel and discover new places.", "native": "Udhëtoni dhe zbuloni vende të reja.", "transliteration": "Udhëtoni dhe zbuloni vende të reja."},
    {"english": "Appreciate what you already have.", "native": "Vlerësoni atë që tashmë keni.", "transliteration": "Vlerësoni atë që tashmë keni."},
    {"english": "Dance like nobody is watching.", "native": "Vallëzoni sikur askush të mos po ju shikojë.", "transliteration": "Vallëzoni sikur askush të mos po ju shikojë."},
    {"english": "Sing from your heart out loud.", "native": "Këndoni nga zemra me zë të lartë.", "transliteration": "Këndoni nga zemra me zë të lartë."},
    {"english": "Plant seeds of kindness everywhere.", "native": "Mbillni fara mirësjelljeje kudo.", "transliteration": "Mbillni fara mirësjelljeje kudo."},
    {"english": "Let go of what you cannot control.", "native": "Lëshoni atë që nuk mund ta kontrolloni.", "transliteration": "Lëshoni atë që nuk mund ta kontrolloni."},
    {"english": "Be present in the here and now.", "native": "Jini të pranishëm në këtu dhe tani.", "transliteration": "Jini të pranishëm në këtu dhe tani."},
]
# ==== FALLBACK PHRASES END ====


def _load_json(path, default):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return default


def _save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_phrase_history():
    data = _load_json(PHRASE_HISTORY_FILE, {"phrases": [], "last_updated": None})
    data.setdefault("phrases", [])
    return data


def save_phrase_history(data):
    data["last_updated"] = datetime.now().isoformat()
    _save_json(PHRASE_HISTORY_FILE, data)


def is_phrase_used(english):
    english_lower = english.lower().strip()
    for p in load_phrase_history()["phrases"]:
        if p.get("english", "").lower().strip() == english_lower:
            return True
    return False


def _history_native(p):
    for key in (PHRASE_KEY, "vietnamese", "native", "translation", "target"):
        value = p.get(key)
        if value:
            return str(value)
    return ""


def add_phrases_to_history(phrases, category):
    history = load_phrase_history()
    for phrase in phrases:
        history["phrases"].append({
            "english": phrase["english"],
            PHRASE_KEY: phrase["native"],
            "transliteration": phrase.get("transliteration", ""),
            "category": category,
            "generated_at": datetime.now().isoformat(),
        })
    save_phrase_history(history)
    print(f"[content] Saved {len(phrases)} phrases (history total: {len(history['phrases'])})")


def get_available_category():
    data = _load_json(RECENT_CATEGORIES_FILE, {"recent_categories": [], "last_updated": None})
    recent = data.get("recent_categories", [])
    available = [c for c in CATEGORIES if c not in recent]
    if not available:
        recent = recent[-5:]
        available = [c for c in CATEGORIES if c not in recent]
        print("[rotation] Reset recent categories")
    selected = random.choice(available)
    recent.append(selected)
    data["recent_categories"] = recent[-MAX_RECENT_CATEGORIES:]
    data["last_updated"] = datetime.now().isoformat()
    _save_json(RECENT_CATEGORIES_FILE, data)
    print(f"[rotation] Category: {selected} ({len(available)} available)")
    return selected


def _normalize_phrase(item):
    if not isinstance(item, dict):
        return None
    english = str(item.get("english", "")).strip()
    native = str(
        item.get(PHRASE_KEY)
        or item.get("native")
        or item.get("vietnamese")
        or item.get("translation")
        or ""
    ).strip()
    translit = str(item.get("transliteration") or item.get("romanization") or item.get("romaji") or "").strip()
    if not english or not native:
        return None
    if len(english.split()) > 16:
        return None
    if "/" in native or "|" in native:
        native = native.split("/")[0].split("|")[0].strip()
    return {
        "english": english.replace("  ", " ").strip(),
        "native": native.strip(),
        "transliteration": translit.strip().strip("[]"),
    }


def _history_keys(history):
    used_en = set()
    used_nat = set()
    for p in history.get("phrases", []):
        en = str(p.get("english", "")).lower().strip()
        nat = _history_native(p).lower().strip()
        if en:
            used_en.add(en)
        if nat:
            used_nat.add(nat)
    return used_en, used_nat


def generate_phrases(category_english: str, num_phrases: int = 5) -> list:
    category_native = CATEGORIES_NATIVE[category_english]
    history = load_phrase_history()
    used_en, used_nat = _history_keys(history)
    recent_english = [
        p["english"] for p in history["phrases"] if p.get("category") == category_english
    ][-30:]

    models = [config.AI_MODEL]
    if "gemini-fast" not in models:
        models.append("gemini-fast")

    if config.POLLINATIONS_API_KEY:
        for attempt in range(5):
            model = models[0] if attempt < 3 else models[-1]
            try:
                phrases = _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model)
                unique = []
                for item in phrases:
                    p = _normalize_phrase(item)
                    if not p:
                        continue
                    key_en = p["english"].lower().strip()
                    key_nat = p["native"].lower().strip()
                    if key_en in used_en or key_nat in used_nat:
                        continue
                    if any(key_en == u["english"].lower().strip() for u in unique):
                        continue
                    used_en.add(key_en)
                    used_nat.add(key_nat)
                    unique.append(p)
                    if len(unique) >= num_phrases:
                        break
                if len(unique) >= num_phrases:
                    add_phrases_to_history(unique[:num_phrases], category_english)
                    return unique[:num_phrases]
                print(f"[content] Attempt {attempt + 1}: only {len(unique)} fresh phrases (need {num_phrases})")
            except Exception as exc:  # noqa: BLE001 - network boundary
                print(f"[content] Attempt {attempt + 1} failed ({model}): {exc}")
            time.sleep(1.5 * (attempt + 1))
    else:
        print("[content] No POLLINATIONS_API_KEY, using fallback phrases")

    fresh_fallback = []
    for p in FALLBACK_PHRASES:
        if p["english"].lower().strip() in used_en or p["native"].lower().strip() in used_nat:
            continue
        fresh_fallback.append(p)
    if not fresh_fallback:
        raise RuntimeError("Phrase API unavailable and no unused fallback phrases left; refusing to reuse phrases")
    chosen = fresh_fallback[:num_phrases]
    if len(chosen) < num_phrases:
        print(f"[content] Only {len(chosen)} fresh fallback phrases; building a shorter lesson")
    add_phrases_to_history(chosen, category_english)
    return chosen


def _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model=None):
    avoid = ""
    if recent_english:
        avoid = "\nDo NOT reuse any of these phrases:\n" + "\n".join(f"- {p}" for p in recent_english)

    prompt = f"""Create {num_phrases * 6} unique {category_english} phrases for English speakers learning {LANGUAGE_NAME}.
{avoid}

Rules:
1. Keep every phrase short and natural (4-11 words in English).
2. Use natural commas for TTS breathing pauses.
3. Each phrase must be speakable in 2-4 seconds.
4. Write clean {LANGUAGE_NAME} in {NATIVE_NAME} with correct accents and orthography. One translation only, no slashes.
5. Transliteration is a friendly Roman-script pronunciation guide for English speakers (not IPA).
6. Vary the sentence patterns and emotions. No duplicates.
7. Phrases must feel like real everyday language, not textbook filler.

Return ONLY a JSON array:
[{{"english": "...", "native": "...", "transliteration": "..."}}]"""

    response = requests.post(
        "https://gen.pollinations.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {config.POLLINATIONS_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model or config.AI_MODEL,
            "messages": [
                {"role": "system", "content": f"You are a {LANGUAGE_NAME} teacher creating short, natural, varied bilingual phrases. Reply with JSON only."},
                {"role": "user", "content": prompt},
            ],
            "temperature": min(0.95 + attempt * 0.02, 1.0),
        },
        timeout=90,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"].strip()

    if "```json" in content:
        content = content.split("```json", 1)[1].split("```", 1)[0].strip()
    elif "```" in content:
        content = content.split("```", 1)[1].split("```", 1)[0].strip()

    start = content.find("[")
    end = content.rfind("]")
    if start >= 0 and end > start:
        content = content[start:end + 1]

    data = json.loads(content)
    if not isinstance(data, list):
        raise ValueError("AI did not return a JSON array")
    return data
