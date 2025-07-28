import fitz  # PyMuPDF
from pathlib import Path
from typing import Union, Optional
from os import path
from PIL import Image

# Chemins des images de couverture par défaut
DEFAULT_MARGIN = 0.0  # Marge par défaut pour les couvertures


def ajouter_image_page(
    doc: fitz.Document,
    image_path: Union[str, Path],
    page_number: int,
    margin: float = DEFAULT_MARGIN,
) -> bool:
    """
    Ajoute une image sur toute une page avec une marge donnée.

    Args:
        doc: Document PDF
        image_path: Chemin vers l'image à ajouter
        page_number: Position de la page (0 pour la première, -1 pour la dernière)
        margin: Marge en points autour de l'image

    Returns:
        bool: True si l'image a été ajoutée avec succès, False sinon
    """
    if not path.exists(image_path):
        print(f"Avertissement: Le fichier {image_path} n'existe pas.")
        return False

    try:
        # Créer une nouvelle page vide à la fin
        new_page = doc.new_page(-1)

        # Réorganiser la nouvelle page à la position souhaitée (si valide)
        if 0 <= page_number < len(doc) - 1:  # -1 car on vient d'ajouter une page
            page_count = len(doc)
            new_order = list(range(page_count - 1))  # Toutes les pages sauf la dernière
            new_order.insert(
                page_number, page_count - 1
            )  # Insère la nouvelle page au bon endroit
            doc.select(new_order)
            page = doc[page_number]
        else:
            page = new_page

        # Obtenir les dimensions de la page
        page_rect = page.rect

        # Ouvrir l’image avec PIL pour obtenir ses dimensions
        img = Image.open(image_path)
        img_width, img_height = img.size
        img_ratio = img_width / img_height

        # Calculer la zone disponible avec les marges
        available_width = page_rect.width - 2 * margin
        available_height = page_rect.height - 2 * margin
        available_ratio = available_width / available_height

        # Objectif : largeur totale, et ajuster la hauteur selon les proportions
        display_width = page_rect.width
        display_height = display_width / img_ratio

        # Centrer verticalement si image trop haute
        x0 = page_rect.x0  # pas de marge horizontale
        y0 = page_rect.y0 + (page_rect.height - display_height) / 2
        x1 = x0 + display_width
        y1 = y0 + display_height
        rect = fitz.Rect(x0, y0, x1, y1)

        # Insérer l’image dans la page — proportions déjà gérées, donc keep_proportion=False
        page.insert_image(
            rect, filename=image_path, keep_proportion=False, overlay=True
        )

        return True
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'image {image_path}: {str(e)}")
        return False


def ajouter_couverture(
    doc: fitz.Document,
    image_path: str,
    margin: float = DEFAULT_MARGIN,
) -> bool:
    """Ajoute une page de couverture au début du document."""
    return ajouter_image_page(doc, image_path, 0, margin)


def ajouter_quatrieme_couverture(
    doc: fitz.Document,
    image_path: str,
    margin: float = DEFAULT_MARGIN,
) -> bool:
    """Ajoute une page de quatrième de couverture à la fin du document."""
    return ajouter_image_page(doc, image_path, -1, margin)
