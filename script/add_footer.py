import fitz  # PyMuPDF
from pathlib import Path
from typing import Union

# === Configuration ===
INPUT_PDF: Union[str, Path] = "document.pdf"
OUTPUT_PDF: Union[str, Path] = "document_avec_footer.pdf"
FONT_NAME: str = "helv"
FOOTER_COLOR: tuple = (0, 0, 0)  # Noir
MARGIN_BOTTOM: float = 20.0  # Distance du bas de page en points


def ajouter_footer(
    doc: fitz.Document, texte_footer: str, start_page_index: int, fontsize: int = 9
) -> None:
    """Ajoute un footer à chaque page à partir de start_page_index."""
    for page_index in range(start_page_index, len(doc)):
        page = doc[page_index]
        largeur = page.rect.width - 25
        hauteur = page.rect.height

        # Position centrée en bas
        position = fitz.Point(largeur / 2, hauteur - MARGIN_BOTTOM)
        # Pour lecture, pour impression revoir la mise en forme et la numérotation.
        texte = texte_footer.format(page_number=page_index + 2)

        page.insert_text(
            position,
            texte,
            fontsize=fontsize,
            fontname=FONT_NAME,
            color=FOOTER_COLOR,
            # align=1,  # Centré
        )


def ajouter_footer_pdf(
    entree: Union[str, Path],
    sortie: Union[str, Path],
    start_page_index: int,
    fontsize: int,
) -> None:
    """Charge un PDF, ajoute les footers, puis sauvegarde."""
    with fitz.open(entree) as doc:
        ajouter_footer(
            doc,
            texte_footer="Page {page_number}",
            start_page_index=start_page_index,
            fontsize=fontsize,
        )
        doc.save(sortie)
