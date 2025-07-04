from markdown_pdf import MarkdownPdf, Section
from os import path
import re

css = """
/* Empêche la césure automatique des mots */
body, h1, h2, h3, h4, h5, h6, p {
  hyphens: none;
  -webkit-hyphens: none;
  -ms-hyphens: none;
  word-break: keep-all;
  overflow-wrap: break-word;
}

/* Améliore l'espacement des paragraphes */
p {
  line-height: 1.5;
  margin-bottom: 12pt;
}

/* Évite les sauts de page après les titres */
h1, h2, h3 {
  page-break-after: avoid;
  page-break-inside: avoid;
}

img {
  margin-top: 10px;
  margin-bottom: 20px;
}


body {
  background-color: #fef6e4;
  font-family: 'Helvetica Neue', sans-serif;
}

h1, h2 {
  font-weight: bold;
  letter-spacing: 1px;
}

hr {
  border: none;
  border-top: 3px dotted #8bd3dd;
}

@page {
  margin: 50pt;
}

blockquote {
  border: 2px solid #444;
  background: #fef6e4;
  padding: 4px;
  border-radius: 1px;
  page-break-after: avoid;
  page-break-inside: avoid;
}

th, td { 
  border:0.5px solid black; 
  border-collapse: collapse;
}

"""


def export_pdf(files):

    pdf = MarkdownPdf(toc_level=3, optimize=True)
    pdf.borders = (50, 50, 50, 50)

    # base_dir = path.dirname(path.dirname(path.abspath(__file__)))
    # image_path = path.join(base_dir, "images", "cover.png")
    # print(image_path)
    # cover_image_md = f'![Couverture]({image_path})\n\n<div style="page-break-after: always;"></div>\n'

    cover_page = "<img src='images/cover.png' alt='Cover' width='80%'/>"
    cover_page = '![Page de couverture](cover.png)\n\n<div style="page-break-after: always;"></div>'
    # cover_page = f"![Page de couverture]({image_path})"

    # pdf.add_section(Section(cover_page, toc=False), user_css=css)

    regex = re.compile(r"## Chapitre \d* — ")
    regex_sommaire = re.compile(r"### \*\*Chapitre \d* — ")
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            markdown_text = f.read()
        markdown_text = markdown_text.replace("---", "")
        markdown_text = markdown_text.replace(" **Encadré : ", " **")
        markdown_text = markdown_text.replace(" **Encadré — ", " **")
        # markdown_text = markdown_text.replace("images/", "../chapitres/images/")

        # regex = re.compile(r"## Chapitre %d*")

        # markdown_text = regex.sub("## ", markdown_text)
        # markdown_text = regex_sommaire.sub("### **", markdown_text)
        pdf.add_section(Section(markdown_text), user_css=css)

    pdf.meta["title"] = (
        "LLM-Assisted Software Design, a Pattern Language of New Development Practices"
    )
    pdf.meta["author"] = "S@M depuis idée de OAZ avec ChatGPT et Microsoft Copilot"

    # Save normalized PDF
    pdf_path = "../pdf/llm_assisted_software_design.pdf"
    pdf.save(pdf_path)


if __name__ == "__main__":
    export_pdf(
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
            "../chapitres/quatrieme_couverture.md",
        ]
    )
