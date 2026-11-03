import random


def process_text(text: str):
    text = text.upper()

    text = text.replace("И", "1")
    text = text.replace("Е", "3")
    text = text.replace("Ё", "3")
    text = text.replace("А", "4")
    text = text.replace("Т", "7")
    text = text.replace("О", "0")

    if random.random() < 0.35:
        kawaii_inserts = [" *кусь* ", " *ня~*"]
        text += random.choice(kawaii_inserts)

    points = ["。", "!!!", "¡¡", "¡¡!"]
    points_weight = [2, 1, 1, 1]
    point = random.choices(points, weights=points_weight)[0]

    questions = ["??", "¿", "¿¿", "¿¿?"]
    question = random.choices(questions)[0]

    exclamations = ["¡", "!!", "¡¡", "¡¡!"]
    exclamation = random.choices(exclamations)[0]

    text = text.replace(".", point)
    text = text.replace("!", exclamation)
    text = text.replace("?", question)
    text = text.replace(",", "⹁")
    text = text.replace("-", "—")

    ending_syms = [
        ":3", ":33", "^^", "^-^", "(*≧ω≦*)",
        "(⁠≧⁠▽⁠≦⁠)", "o(>ω<)o", "(｡• ᵕ •｡)", "(*/ω＼*)",
        "(>_<)", "(๑>&lt;๑)"
    ]
    ending_sym = random.choices(ending_syms)[0]

    emojis = [
        "🌸", "🪽", "🍪", "🐠", "🎀", "✨", "🍬",
        "🍓", "🍡", "🤍", "🌙"
    ]
    emoji = random.choices(emojis)[0]

    decorations = [("✧*", "*✧"), ("꒰", "꒱"), ("✦", "✦"), ("✿", "✿")]
    dec_left, dec_right = random.choice(decorations)

    tilde = "~" if random.random() < 0.6 else ""
    text = f"{text}{tilde} {ending_sym}"

    return f"{dec_left} [{emoji}] — «{text}» {dec_right}"