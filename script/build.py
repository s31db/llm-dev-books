from pathlib import Path
from re import findall, UNICODE, compile as re_compile, MULTILINE

from emoji_img import emoji_to_image

from base64 import b64encode

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
    "../chapitres/quatrieme_couverture.md",
]


def img64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return b64encode(image_file.read()).decode("utf-8")


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
        for i, file in enumerate(files):
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
                if "quatrieme_couverture" not in file:
                    f.write('<div style="page-break-after: always;"></div>\n')


def pdf():
    unique_md(True, True, True, True, True)
    from publish_pdf import export_pdf

    print("A4")
    export_pdf(
        [
            "../build/llm_assisted_software_design.md",
        ],
        "../pdf/llm_assisted_software_design.pdf",
        "../ressources/pdf.css",
    )

    # print("A5")
    #
    # tmp_pdf = "../build/llm_assisted_software_design_a5.pdf"
    #
    # export_pdf(
    #     [
    #         "../build/llm_assisted_software_design.md",
    #     ],
    #     tmp_pdf,
    #     "../ressources/print.css",
    #     paper_size="A5",
    # )
    # print("Ajout du footer")
    # from add_footer import ajouter_footer_pdf
    #
    # ajouter_footer_pdf(
    #     tmp_pdf,
    #     "../pdf/llm_assisted_software_design_a5.pdf",
    #     8,
    # )


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
    # unique_md(cover=False, images64=False, images=False, emoji=True, emoji_image=False)
    pdf()
    # Test pandoc
    # pdf_pandoc()
    epub()
