from os.path import abspath
from pathlib import Path
from re import search, findall

# from shutil import copyfile
from base64 import b64encode


def img64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return b64encode(image_file.read()).decode("utf-8")


def unique_md(cover: bool = True, images: bool = True) -> None:
    files = [
        "../chapitres/page_garde.md",
        "../chapitres/preface.md",
        "../chapitres/sommaire.md",
        "../chapitres/avant_propos.md",
        "../chapitres/introduction.md",
        "../chapitres/anatomie_prompt.md",
        "../chapitres/grammaire_intention.md",
        "../chapitres/motifs_dialogue.md",
        "../chapitres/role_competences.md",
        "../chapitres/cartographie_prompt.md",
        "../chapitres/motifs.md",
        # "../chapitres/temp/tdp.md",
        "../chapitres/responsabilite.md",
        "../chapitres/agile.md",
        "../chapitres/cadre.md",
        "../chapitres/apprentissage.md",
        "../chapitres/prospectifs.md",
        "../chapitres/conclusion.md",
        "../chapitres/quatrieme_couverture.md",
    ]
    if cover:
        files.insert(0, "../chapitres/cover.md")

    Path("../build").mkdir(parents=False, exist_ok=True)

    # copy all images in images dir to build folder
    # for file in Path("../images").iterdir():
    #    print(file)
    # copyfile(file, "../build/" + file.name)

    i_chapitre = 1

    with open("../build/llm_assisted_software_design.md", "w", encoding="utf-8") as f:
        for file in files:
            with open(file, "r", encoding="utf-8") as f2:
                content = f2.read()

                # print(f"file:///{abspath(file).replace('\\', '/')}")
                if "## Chapitre" in content:
                    content = content.replace(
                        "## Chapitre", f"## Chapitre {i_chapitre}"
                    )
                    i_chapitre += 1
                # try:
                #    title = search(r"## Chapitre \d* — (.*)", content).group(1)
                #    print(f"{file[:-3].replace('../chapitres/', '')} - {title}")
                # except AttributeError:
                #    print(f"{file.replace('../chapitres/', '')} n'a pas de titre")
                ## f.write(f"## {file[:-3]}\n")

                if not images:
                    for find in findall(r'<img src="../images/.*.png".*/>', content):
                        content = content.replace(find, "")

                for find in findall(r"../images/.*.png", content):
                    content = content.replace(
                        find, f"data:image/png;base64,{img64(find)}"
                    )
                content = content.replace("../images/", "")
                f.write(f"{content}\n")
                if "quatrieme_couverture" not in file:
                    f.write('<div style="page-break-after: always;"></div>\n')


if __name__ == "__main__":
    unique_md()
    from publish_pdf import export_pdf

    export_pdf(
        [
            "../build/llm_assisted_software_design.md",
        ]
    )

    from publish_epub import export_epub

    # TODO epub avec image
    unique_md(False, False)
    export_epub(
        [
            "../build/llm_assisted_software_design.md",
        ],
        "../epub/llm_assisted_software_design.epub",
        extra_args=[
            "--epub-cover-image=../images/cover.png",
            "--metadata",
            "language=fr",
        ],
    )
