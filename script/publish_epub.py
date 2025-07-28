import pypandoc
from typing import Iterator, Union
from pathlib import Path


def export_epub(file: Union[list, str, Path, Iterator], outputfile, extra_args):
    pypandoc.convert_file(
        source_file=file,
        to="epub",
        outputfile=outputfile,
        sort_files=False,
        extra_args=extra_args,
    )


if __name__ == "__main__":
    export_epub(
        [
            "../chapitres/page_garde.md",
            "../chapitres/sommaire.md",
            "../chapitres/avant_propos.md",
            "../chapitres/introduction.md",
            "../chapitres/grammaire_intention.md",
            "../chapitres/motifs_dialogue.md",
            "../chapitres/anatomie_prompt.md",
            "../chapitres/cartographie_prompt.md",
            "../chapitres/motifs.md",
            "../chapitres/role_competences.md",
            "../chapitres/responsabilite.md",
            "../chapitres/prospectifs.md",
            "../chapitres/cadre.md",
            "../chapitres/conclusion.md",
            # "../chapitres/chapitre*.md",
            "../chapitres/quatrieme_couverture.md",
        ],
        "../epub/llm_assisted_software_design.epub",
        extra_args=[
            "--epub-cover-image=../images/cover.png",
            "--metadata",
            "language=fr",
        ],
    )
