import os
import fitz  # PyMuPDF
from cover_utils import (
    ajouter_couverture,
    ajouter_quatrieme_couverture,
    DEFAULT_MARGIN,
)


def ajouter_couverture_pdf(
    input_pdf: str,
    output_pdf: str,
    cover_image: str,
    back_cover_image: str,
    cover_margin: float = DEFAULT_MARGIN,
    back_cover_margin: float = DEFAULT_MARGIN,
    paper_size: str = "A4",
) -> None:
    """
    Ajoute des pages de couverture et de quatrième de couverture à un PDF.

    Args:
        input_pdf: Chemin vers le fichier PDF d'entrée
        output_pdf: Chemin vers le fichier PDF de sortie
        cover_image: Chemin vers l'image de couverture
        back_cover_image: Chemin vers l'image de quatrième de couverture
        cover_margin: Marge pour la couverture en points
        back_cover_margin: Marge pour la quatrième de couverture en points
        paper_size: Taille du papier (par exemple, "A4" ou "A5")
    """
    print("\n🔄 Ajout des couvertures au PDF...")

    # Vérifier si le fichier d'entrée existe
    if not os.path.exists(input_pdf):
        raise FileNotFoundError(f"Le fichier source {input_pdf} n'existe pas.")

    # Vérifier si les images de couverture existent
    if not os.path.exists(cover_image):
        print(
            f"⚠️ Avertissement: L'image de couverture {cover_image} n'existe pas. La couverture ne sera pas ajoutée."
        )
        cover_image = None

    if back_cover_image and not os.path.exists(back_cover_image):
        print(
            f"⚠️ Avertissement: L'image de quatrième de couverture {back_cover_image} n'existe pas. La quatrième de couverture ne sera pas ajoutée."
        )
        back_cover_image = None

    # Ouvrir le document PDF
    with fitz.open(input_pdf) as doc:
        # Ajouter la couverture si l'image existe
        if cover_image:
            print(f"📕 Ajout de la couverture: {cover_image}")
            ajouter_couverture(doc, cover_image, cover_margin, paper_size)

        # Ajouter la quatrième de couverture si l'image existe
        if back_cover_image:
            print(f"📘 Ajout de la quatrième de couverture: {back_cover_image}")
            ajouter_quatrieme_couverture(
                doc, back_cover_image, back_cover_margin, paper_size
            )

        # Sauvegarder le document
        doc.save(output_pdf)

    print(f"✅ PDF généré avec succès: {output_pdf}\n")
