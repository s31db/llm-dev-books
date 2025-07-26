from pathlib import Path
import os
import hashlib
import shelve

# import argparse
from re import findall, UNICODE, compile as re_compile, MULTILINE
from functools import wraps
from time import time
from typing import Dict, List, Callable

# Import du module de profilage
# from profiler import profile, Profiler

from emoji_img import emoji_to_image
from base64 import b64encode
from add_footer import ajouter_footer_pdf
from add_covers import ajouter_couverture_pdf
from publish_pdf import export_pdf

from cProfile import Profile
from functools import wraps
from pstats import Stats
from io import StringIO


def profile0(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = Profile()
        # profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        profiler.print_stats(sort="time")
        return result

    return wrapper


def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pr = Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        s = StringIO()
        ps = Stats(pr, stream=s).sort_stats("time")
        ps.print_stats(10)
        print("📊 Top 10 des appels les plus longs :")
        print(s.getvalue())
        return result

    return wrapper


PAGES = [
    "../chapitres/page_garde.md",
    "../chapitres/preface.md",
    "../chapitres/sommaire.md",
    "../chapitres/avant_propos.md",
    "../chapitres/introduction.md",
    "../chapitres/anatomie_prompt.md",
    "../chapitres/grammaire_intention.md",
    "../chapitres/motifs_dialogue.md",
    "../chapitres/motif_socratique.md",
    "../chapitres/motif_exploration.md",
    "../chapitres/motif_specification.md",
    "../chapitres/motif_miroir.md",
    "../chapitres/motif_clarification.md",
    "../chapitres/motif_tdp.md",
    "../chapitres/motif_reformulation.md",
    "../chapitres/motif_soin_systemique.md",
    "../chapitres/motif_synthese.md",
    "../chapitres/role_competences.md",
    "../chapitres/cartographie_prompt.md",
    "../chapitres/motifs.md",
    "../chapitres/responsabilite.md",
    "../chapitres/agile.md",
    "../chapitres/cadre.md",
    "../chapitres/apprentissage.md",
    "../chapitres/usages.md",
    "../chapitres/memoire.md",
    "../chapitres/prospectifs.md",
    "../chapitres/honte.md",
    "../chapitres/histoires.md",
    "../chapitres/design_pattern.md",
    "../chapitres/nouveaux_design_pattern.md",
    "../chapitres/conclusion.md",
    "../chapitres/intro_annexe.md",
    "../chapitres/fiches_outils.md",
    "../chapitres/tdp.md",
    "../chapitres/po.md",
    "../chapitres/dev.md",
    "../chapitres/coach.md",
    "../chapitres/manager.md",
    # "../chapitres/quatrieme_couverture.md",
]
# PAGES = PAGES[:2]


def get_cache_path() -> Path:
    """Retourne le chemin du fichier de cache."""
    # cache_dir = Path.home() / ".llm-dev-books-cache"
    cache_dir = Path("../build/.llm-dev-books-cache")
    cache_dir.mkdir(exist_ok=True)
    return cache_dir / "image_cache.db"


def clear_image_cache() -> None:
    """Vide le cache des images encodées."""
    cache_file = get_cache_path()
    if cache_file.exists():
        os.remove(cache_file)


# @profile
def img64(image_path: str) -> str:
    """
    Encode une image en base64 avec mise en cache des résultats.

    Args:
        image_path: Chemin vers le fichier image

    Returns:
        Chaîne encodée en base64 de l'image
    """
    # Obtenir le chemin absolu normalisé pour la clé de cache
    abs_path = str(Path(image_path).resolve())

    # Créer une empreinte du chemin pour la clé de cache
    key = hashlib.sha256(abs_path.encode("utf-8")).hexdigest()

    # Vérifier la date de modification du fichier pour l'invalidation du cache
    file_mtime = os.path.getmtime(abs_path)

    with shelve.open(str(get_cache_path())) as cache:
        cache_key = f"{key}_{file_mtime}"

        # Vérifier si le résultat est en cache
        if cache_key in cache:
            return cache[cache_key]

        print(f"image non en cache : {image_path}")

        # Si non en cache, lire et encoder l'image
        with open(abs_path, "rb") as image_file:
            encoded = b64encode(image_file.read()).decode("utf-8")

            # Mettre en cache le résultat
            cache[cache_key] = encoded

            # Nettoyer les entrées obsolètes pour ce fichier
            for k in list(cache.keys()):
                if k.startswith(key + "_") and k != cache_key:
                    del cache[k]

            return encoded


# @profile
def unique_md(
    cover: bool = True,
    images64: bool = True,
    images: bool = True,
    emoji: bool = True,
    emoji_image: bool = False,
) -> None:
    files = PAGES
    if cover:
        files.insert(0, "../chapitres/cover.md")

    Path("../build").mkdir(parents=False, exist_ok=True)

    with open("../build/llm_assisted_software_design.md", "w", encoding="utf-8") as f:
        for file in files:
            with open(file, "r", encoding="utf-8") as f2:
                content = f2.read()

                pattern = (
                    "["
                    "👩‍💻"  # Personnes complexe
                    "\U0001f600-\U0001f64f"  # Emoticons
                    "\U0001f300-\U0001f5ff"  # Symboles & pictogrammes
                    "\U0001f680-\U0001f6ff"  # Transport & cartes
                    "\U0001f1e6-\U0001f1ff"  # Drapeaux (lettres régionales)
                    "\U00002700-\U000027bf"  # Divers symboles
                    "\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
                    "\U0001fa70-\U0001faff"  # Symbols for legacy computing
                    "\U00002600-\U000026ff"  # Divers symboles
                    "]+"
                )
                if not emoji:
                    emoji_patterns = (
                        re_compile(
                            pattern + " ",
                            flags=UNICODE,
                        ),
                        re_compile(
                            pattern,
                            flags=UNICODE,
                        ),
                    )

                    for emoji_pattern in emoji_patterns:
                        for emoji in emoji_pattern.findall(content):
                            content = content.replace(emoji, "")

                if not images:
                    for find in findall(r'<img src="../images/.*.png".*/>', content):
                        content = content.replace(find, "")

                if emoji_image:
                    emoji_pattern = re_compile(
                        pattern,
                        flags=UNICODE,
                    )
                    for emoji in emoji_pattern.findall(content):
                        path = emoji_to_image(emoji)
                        content = content.replace(
                            emoji,
                            f'<img src="{path}" style="height:1em; vertical-align:middle;"/>',
                        )

                if images64:
                    for find in findall(r"../images/.*?.png", content):
                        content = content.replace(
                            find, f"data:image/png;base64,{img64(find)}"
                        )
                    for find in findall(r"../emoji/.*?.png", content):
                        content = content.replace(
                            find, f"data:image/png;base64,{img64(find)}"
                        )
                else:
                    content = content.replace("../images/", "")
                f.write(f"{content}\n")
                # if "quatrieme_couverture" not in file:
                if file != files[-1]:
                    f.write('<div style="page-break-after: always;"></div>\n')


# @profile
def pdf():
    # unique_md(True, True, True, True, True)
    unique_md(False, True, True, True, True)
    pdf_A4()
    # PDF pour impression format de poche
    # pdf_A5()


def pdf_A5():
    print("A5")
    tmp_pdf = "../build/llm_assisted_software_design_a5.pdf"
    final_pdf = "../pdf/llm_assisted_software_design_a5.pdf"

    # Générer le PDF de base
    export_pdf(
        ["../build/llm_assisted_software_design.md"],
        tmp_pdf,
        "../ressources/print.css",
        paper_size="A5",
    )

    # Ajouter les footers
    print("Ajout du footer")
    ajouter_footer_pdf(tmp_pdf, final_pdf, 8, fontsize=9)

    # Ajouter les couvertures
    ajouter_couverture_pdf(
        input_pdf=final_pdf,
        output_pdf=final_pdf,  # Écrase le fichier avec les couvertures
        cover_margin=0.0,
        back_cover_margin=0.0,
        cover_image="../../images/cover2.png",
        back_cover_image="../../images/quatrieme_couverture.png",
    )


def pdf_A4():
    print("A4")
    tmp_pdf = "../build/llm_assisted_software_design.pdf"
    tmp_footer_pdf = "../build/llm_assisted_software_design_footer.pdf"
    final_pdf = "../pdf/llm_assisted_software_design.pdf"

    # Générer le PDF de base
    export_pdf(
        ["../build/llm_assisted_software_design.md"],
        tmp_pdf,
        "../ressources/pdf.css",
    )

    # Ajouter les footers
    print("A4 Ajout du footer")
    ajouter_footer_pdf(tmp_pdf, tmp_footer_pdf, 8, fontsize=11)

    # Ajouter les couvertures
    ajouter_couverture_pdf(
        input_pdf=tmp_footer_pdf,
        output_pdf=final_pdf,
        cover_margin=0.0,
        back_cover_margin=0.0,
        cover_image="../images/cover2.png",
        back_cover_image="../images/quatrieme_couverture.png",
    )


def epub():
    from publish_epub import export_epub

    unique_md(False, False)
    export_epub(
        [
            "../build/llm_assisted_software_design.md",
        ],
        "../epub/llm_assisted_software_design.epub",
        extra_args=[
            "--epub-cover-image=../images/cover2.png",
            "--metadata",
            "language=fr",
            "--resource-path=../images",
        ],
    )
    print("📖 Epub done")


def pdf_pandoc():
    # unique_md(True, True)
    unique_md(False, False, False)
    from publish_pdf_pandoc import export_pdf

    print("A4")
    export_pdf(
        [
            "../build/llm_assisted_software_design.md",
        ],
        "../pdf/llm_assisted_software_design.pdf",
        "../ressources/pdf.css",
    )


def check_pages():
    print("Checking if all files in chapitres is used")
    pages = set([p[13:] for p in PAGES])
    all_files = set(f.name for f in Path("../chapitres").glob("*.md"))
    unused_files = all_files - pages
    if unused_files:
        print(f"Unused files: {', '.join(sorted(unused_files))}")


def check_chapters_sommaire():
    with open("../chapitres/sommaire.md", "r", encoding="utf-8") as f:
        sommaire_content = f.read()
    sommaire_content = sommaire_content.replace("*", "").replace(" ", " ")
    # print(sommaire_content)
    for page in PAGES:
        if page[13:-3] in (
            "preface",
            "sommaire",
            "page_garde",
            "avant_propos",
            "introduction",
            "intro_annexe",
            "quatrieme_couverture",
        ):
            continue
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()
            titles = findall(r"^## .*", content, flags=MULTILINE)
            for title in titles:
                title = title.replace("*", "").replace(" ", " ")
                if title and title not in sommaire_content:
                    print(f"{page[13:]} - Chapter {title} is not in sommaire.md")


if __name__ == "__main__":
    # check_pages()
    # check_chapters_sommaire()
    # To send file to LLM
    # main()
    # unique_md(cover=False, images64=False, images=False, emoji=True, emoji_image=False)

    pdf()
    # cProfile.run("pdf()")
    # Test pandoc
    # pdf_pandoc()
    epub()
    print("Done")
