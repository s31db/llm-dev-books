import pypandoc
from typing import Iterator, Union
from pathlib import Path


def export_epub(file: Union[list, str, Path, Iterator], outputfile):
    pypandoc.convert_file(
        source_file=file,
        to="epub",
        outputfile=outputfile,
        sort_files=False,
        extra_args=[
            "--epub-cover-image=../images/cover.png",
            "--metadata",
            "language=fr",
        ],
    )


if __name__ == "__main__":
    export_epub(
        [
            "../chapitres/page_garde.md",
            "../chapitres/sommaire.md",
            "../chapitres/avant_propos.md",
            "../chapitres/chapitre*.md",
            "../chapitres/quatrieme_couverture.md",
        ],
        "../epub/llm_assisted_software_design.epub",
    )
