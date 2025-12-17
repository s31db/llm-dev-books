from pathlib import Path
import os
import hashlib
import shelve

from re import findall, UNICODE, compile as re_compile, MULTILINE, sub

from emoji_img import emoji_to_image
from base64 import b64encode
from add_footer import ajouter_footer_pdf
from add_covers import ajouter_couverture_pdf
from publish_pdf import export_pdf

from cProfile import Profile
from functools import wraps
from pstats import Stats
from io import StringIO
from yaml import safe_load


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
PAGES_EN_US = [
    "../chapitres_en/page_garde.md",
    "../chapitres_en/advertissement.md",
    "../chapitres_en/preface.md",
    "../chapitres_en/sommaire.md",
    "../chapitres_en/avant_propos.md",
    "../chapitres_en/introduction.md",
    "../chapitres_en/anatomie_prompt.md",
    "../chapitres_en/grammaire_intention.md",
    "../chapitres_en/motifs_dialogue.md",
    "../chapitres_en/motif_socratique.md",
    "../chapitres_en/motif_exploration.md",
    "../chapitres_en/motif_specification.md",
    "../chapitres_en/motif_miroir.md",
    "../chapitres_en/motif_clarification.md",
    "../chapitres_en/motif_tdp.md",
    "../chapitres_en/motif_reformulation.md",
    "../chapitres_en/motif_soin_systemique.md",
    "../chapitres_en/motif_synthese.md",
    "../chapitres_en/role_competences.md",
    "../chapitres_en/cartographie_prompt.md",
    "../chapitres_en/motifs.md",
    "../chapitres_en/responsabilite.md",
    "../chapitres_en/agile.md",
    "../chapitres_en/cadre.md",
    "../chapitres_en/apprentissage.md",
    "../chapitres_en/usages.md",
    "../chapitres_en/memoire.md",
    "../chapitres_en/prospectifs.md",
    "../chapitres_en/honte.md",
    "../chapitres_en/histoires.md",
    "../chapitres_en/design_pattern.md",
    "../chapitres_en/nouveaux_design_pattern.md",
    "../chapitres_en/conclusion.md",
    "../chapitres_en/intro_annexe.md",
    "../chapitres_en/fiches_outils.md",
    "../chapitres_en/tdp.md",
    "../chapitres_en/po.md",
    "../chapitres_en/dev.md",
    "../chapitres_en/coach.md",
    "../chapitres_en/manager.md",
    # "../chapitres/quatrieme_couverture.md",
]

# PAGES_EN_US = PAGES_EN_US[:6]


def get_cache_path() -> Path:
    """Retourne le chemin du fichier de cache."""
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
    titre: str,
    pages: list[str],
    cover: bool = True,
    images64: bool = True,
    images: bool = True,
    emoji: bool = True,
    emoji_image: bool = False,
    sommaire_pages: bool = True,
    css_styles: str = "",
    remove_interne_link: bool = False,
) -> None:
    files = pages
    if cover:
        files.insert(0, "../chapitres/cover.md")

    Path("../build").mkdir(parents=False, exist_ok=True)

    with open(f"../build/{titre}.md", "w", encoding="utf-8") as f:
        # Ajouter les styles CSS si spécifiés
        if css_styles:
            f.write(f"<style>{css_styles}</style>\n\n")
        for file in files:
            with open(file, "r", encoding="utf-8") as f2:
                content = f2.read()

                if not sommaire_pages and "sommaire" in file:
                    content = sub(
                        r" ... p. \d+",
                        "",
                        content,
                    )

                if not sommaire_pages:
                    content = content.replace("---\n<a id", "---\n\n<a id")

                if remove_interne_link:
                    content = sub(
                        r"\[(.*?)\]\(.*?\)",
                        r"\1",
                        content,
                    )

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
def pdf(
    titre: str,
    title: str,
    pages: list[str],
    cover_image: str,
    back_cover_image: str,
    start_page_index: int,
    author: str,
    emoji_image: bool = True,
    css_a5_file: str = "../ressources/print.css",
):
    unique_md(
        titre=titre,
        pages=pages,
        cover=False,
        images64=True,
        images=True,
        emoji=True,
        emoji_image=emoji_image,
    )
    pdf_A4(
        titre,
        title=title,
        cover_image=cover_image,
        back_cover_image=back_cover_image,
        start_page_index=start_page_index,
        # css_file=css_file,
        author=author,
    )
    # PDF pour impression format de poche
    # pdf_A5(
    #         titre,
    #         title=title,
    #         cover_image=cover_image,
    #         back_cover_image=back_cover_image,
    #         start_page_index=start_page_index,
    #         css_file=css_a5_file,
    #         author=author,
    #     )


def sample_book_pdf(
    titre: str,
    title: str,
    pages,
    cover_image: str,
    back_cover_image: str,
    nb_pages: int,
    author: str,
    css_a5_file: str,
    start_page_index: int = 0,
    emoji_image: bool = True,
):
    unique_md(
        titre + "_sample_book",
        pages=pages[:nb_pages],
        cover=False,
        images64=True,
        images=True,
        emoji=True,
        emoji_image=emoji_image,
        remove_interne_link=True,
    )
    pdf_A4(
        titre + "_sample_book",
        title=title,
        cover_image=cover_image,
        back_cover_image=back_cover_image,
        start_page_index=start_page_index,
        # css_a5_file=css_a5_file,
        author=author,
    )


def pdf_A5(
    titre: str,
    title: str,
    cover_image: str,
    back_cover_image: str,
    start_page_index: int,
    css_a5_file: str,
    author: str,
):
    print(f"A5 {titre}")
    tmp_pdf = f"../build/{titre}.pdf"
    tmp_footer_pdf = f"../build/{titre}_footer.pdf"
    final_pdf = f"../pdf/{titre}_format_poche.pdf"

    Path("../pdf").mkdir(parents=False, exist_ok=True)

    # Générer le PDF de base
    export_pdf(
        [f"../build/{titre}.md"],
        tmp_pdf,
        css_file=css_a5_file,
        paper_size="A5",
        title=title,
        author=author,
    )

    # Ajouter les footers
    print("Ajout du footer")
    ajouter_footer_pdf(
        tmp_pdf, tmp_footer_pdf, start_page_index=start_page_index, fontsize=9
    )

    # Ajouter les couvertures
    ajouter_couverture_pdf(
        input_pdf=tmp_footer_pdf,
        output_pdf=final_pdf,  # Écrase le fichier avec les couvertures
        cover_margin=0.0,
        back_cover_margin=0.0,
        cover_image=cover_image,
        back_cover_image=back_cover_image,
        paper_size="A5",
    )


def pdf_A4(
    titre: str,
    title: str,
    author: str,
    cover_image: str,
    back_cover_image: str,
    start_page_index: int,
    css_file: str = "../ressources/pdf.css",
):
    print(f"A4 {titre}")
    tmp_pdf = f"../build/{titre}_A4.pdf"
    tmp_footer_pdf = f"../build/{titre}_footer_A4.pdf"
    final_pdf = f"../pdf/{titre}.pdf"

    Path("../pdf").mkdir(parents=False, exist_ok=True)

    export_pdf(
        [f"../build/{titre}.md"],
        outputfile=tmp_pdf,
        css_file=css_file,
        paper_size="A4",
        title=title,
        author=author,
    )

    # Ajouter les footers
    print("A4 Ajout du footer")

    ajouter_footer_pdf(
        tmp_pdf, tmp_footer_pdf, start_page_index=start_page_index, fontsize=11
    )

    # Ajouter les couvertures
    ajouter_couverture_pdf(
        input_pdf=tmp_footer_pdf,
        output_pdf=final_pdf,
        cover_margin=0.0,
        back_cover_margin=0.0,
        cover_image=cover_image,
        back_cover_image=back_cover_image,
        paper_size="A4",
    )


def epub(titre: str, pages: list[str], cover_image: str, extra_args: list):
    from publish_epub import export_epub

    Path("../epub").mkdir(parents=False, exist_ok=True)

    unique_md(
        titre=titre,
        pages=pages,
        cover=False,
        images64=False,
        sommaire_pages=False,
    )
    export_epub(
        [
            f"../build/{titre}.md",
        ],
        f"../epub/{titre}.epub",
        extra_args=[
            f"--epub-cover-image={cover_image}",
            "--resource-path=../images",
        ]
        + extra_args,
    )
    print(f"📖 Epub {titre} done")


def sample_book_epub(
    titre: str,
    pages: list[str],
    cover_image: str,
    nb_pages: int,
    extra_args,
):
    from publish_epub import export_epub

    Path("../epub").mkdir(parents=False, exist_ok=True)

    unique_md(
        titre=titre,
        pages=pages[:nb_pages],
        cover=False,
        images64=False,
        sommaire_pages=False,
    )
    export_epub(
        [
            f"../build/{titre}_sample_book.md",
        ],
        f"../epub/{titre}_sample_book.epub",
        extra_args=[
            f"--epub-cover-image={cover_image}",
            "--resource-path=../images",
        ]
        + extra_args,
    )
    print(f"📖 Epub {titre}_sample_book done")


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


def publish(
    titre: str,
    title: str,
    pages: list[str],
    cover_image: str,
    back_cover_image: str,
    nb_pages: int,
    extra_args: list,
    author: str,
    emoji_image: bool = True,
    pages_epub: list[str] | None = None,
    start_page_index: int = 0,
    css_a5_file: str = "../ressources/print.css",
):
    pages_epub = pages_epub or pages
    # To send file to LLM
    unique_md(
        titre=titre + "_md",
        cover=False,
        images64=False,
        images=False,
        emoji=True,
        emoji_image=False,
        pages=pages,
    )

    pdf(
        titre,
        title=title,
        pages=pages,
        cover_image=cover_image,
        back_cover_image=back_cover_image,
        emoji_image=emoji_image,
        start_page_index=start_page_index,
        css_a5_file=css_a5_file,
        author=author,
    )
    sample_book_pdf(
        titre,
        title=title,
        pages=pages,
        cover_image=cover_image,
        back_cover_image=back_cover_image,
        emoji_image=emoji_image,
        nb_pages=nb_pages,
        start_page_index=start_page_index,
        css_a5_file=css_a5_file,
        author=author,
    )

    # epub(
    #     titre,
    #     pages=pages_epub,
    #     cover_image=cover_image,
    #     extra_args=extra_args,
    # )
    #
    # sample_book_epub(
    #     titre,
    #     pages=pages_epub,
    #     cover_image=cover_image,
    #     nb_pages=nb_pages,
    #     extra_args=extra_args,
    # )


def llm_assisted():
    with open("../chapitres/meta.yaml", "r", encoding="utf-8") as fichier:
        meta = safe_load(fichier)

    publish(
        titre="llm_assisted_software_design",
        title=meta["title"],
        pages=PAGES,
        cover_image="../images/cover2.png",
        back_cover_image="../images/quatrieme_couverture.png",
        nb_pages=2,
        extra_args=["--metadata-file=../chapitres/meta.yaml"],
        pages_epub=PAGES[1:],
        start_page_index=8,
        css_a5_file="../ressources/print.css",
        author=meta["title"],
    )


def llm_assisted_en():
    with open("../chapitres_en/meta.yaml", "r", encoding="utf-8") as fichier:
        meta = safe_load(fichier)

    publish(
        titre="llm_assisted_software_design_en_us",
        title=meta["title"],
        pages=PAGES_EN_US,
        cover_image="../images/cover2_en.png",
        back_cover_image="../images/quatrieme_couverture_en.png",
        nb_pages=7,
        extra_args=["--metadata-file=../chapitres_en/meta.yaml"],
        pages_epub=PAGES_EN_US[1:],
        start_page_index=8,
        css_a5_file="../ressources/print.css",
        author=meta["title"],
    )


if __name__ == "__main__":
    # check_pages()
    # check_chapters_sommaire()

    # llm_assisted()
    llm_assisted_en()

    # To send file to LLM
    # unique_md(cover=False, images64=False, images=False, emoji=True, emoji_image=False)

    # pdf()
    # Test pandoc
    # pdf_pandoc()
    # epub()
    print("Done")
