from pilmoji import Pilmoji
from PIL import Image, ImageDraw, ImageFont
from os import path


def emoji_to_image(emoji_char) -> str:
    emoji_label = "-".join(f"{ord(c):X}" for c in emoji_char)
    filename = f"../emoji/{emoji_label}.png"
    if path.exists(filename):
        return filename

    font_size = 64
    font_path = "seguiemj.ttf"
    # font_path = "Symbola.ttf"  # Ou seguiemj.ttf selon ton système
    font = ImageFont.truetype(font_path, font_size)
    # Si complexe
    if "-" in filename:
        img = Image.new("RGBA", (font_size, font_size + 5), (255, 255, 255, 0))
        with Pilmoji(img) as pilmoji:
            pilmoji.text((0, -font_size + 20), emoji_char, font=font, fill=(0, 0, 0))
    else:
        # Créer une image temporaire pour mesurer le texte
        temp_img = Image.new("RGBA", (1, 1), (255, 255, 255, 0))
        temp_draw = ImageDraw.Draw(temp_img)
        bbox = temp_draw.textbbox((0, 0), emoji_char, font=font)

        # Calculer la taille exacte
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]

        # Créer l'image finale avec dimensions ajustées
        img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        draw.text(
            (-bbox[0], -bbox[1]),
            emoji_char,
            font=font,
            embedded_color=True,
            fill=(0, 0, 0),
        )

    img.save(filename)
    return filename


if __name__ == "__main__":
    p = emoji_to_image(emoji_char="❌")
    print(p)
    p = emoji_to_image(emoji_char="🧑‍💻")
    print(p)
