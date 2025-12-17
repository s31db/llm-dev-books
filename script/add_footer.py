import fitz  # PyMuPDF
from pathlib import Path
from typing import Union

# === Configuration ===
INPUT_PDF: Union[str, Path] = "document.pdf"
OUTPUT_PDF: Union[str, Path] = "document_avec_footer.pdf"
FONT_NAME: str = "helv"
# FONT_NAME: str = "Helvetica Neue"
FOOTER_COLOR: tuple = (0, 0, 0)  # Noir
WATERMARK_SIZE: tuple = (30, 30)  # Largeur, Hauteur en points
WATERMARK_MARGIN: int = 25


def ajouter_footer(
    doc: fitz.Document,
    texte_footer: str,
    start_page_index: int,
    fontsize: int,
    decalage: int,
    watermark_path: str | Path | None,
    margin_bootom: float = 25.0,
) -> None:
    """Ajoute un footer à chaque page à partir de start_page_index."""
    for page_index in range(start_page_index, len(doc)):
        page = doc[page_index]
        largeur = page.rect.width - 25
        hauteur = page.rect.height

        if watermark_path:
            if page_index % 2 == 0:
                x = largeur - 35 - len(str(page_index))
                x_image_right = x - WATERMARK_MARGIN
                x_image = x_image_right - WATERMARK_SIZE[0]
            else:
                x = 45
                x_image = x + WATERMARK_MARGIN + 10
                x_image_right = x_image + WATERMARK_SIZE[0]

            position = fitz.Point(x, hauteur - margin_bootom)

            rect = fitz.Rect(
                x_image,
                position[1] - WATERMARK_SIZE[1] * 2 / 3,
                x_image_right,
                position[1] + WATERMARK_SIZE[1] / 3,
            )

            page.insert_image(rect, filename=str(watermark_path))
        else:
            # Position centrée en bas
            position = fitz.Point(largeur / 2, hauteur - margin_bootom)

        # Pour lecture, pour impression revoir la mise en forme et la numérotation.
        texte = texte_footer.format(page_number=page_index + 1 + decalage)

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
    watermark_path: str | Path | None,
    decalage: int = 1,
) -> None:
    """Charge un PDF, ajoute les footers, puis sauvegarde."""
    with fitz.open(entree) as doc:
        ajouter_footer(
            doc,
            texte_footer="{page_number}",
            start_page_index=start_page_index,
            fontsize=fontsize,
            decalage=decalage,
            watermark_path=watermark_path
        )
        doc.save(sortie)
