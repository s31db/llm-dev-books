from markdown_pdf import MarkdownPdf, Section
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

"""


def export_pdf():

    pdf = MarkdownPdf(toc_level=3, optimize=True)
    pdf.borders = (50, 50, 50, 50)

    regex = re.compile(r"## Chapitre \d* — ")
    for file in [
        "../chapitres/page_garde.md",
        "../chapitres/sommaire.md",
        "../chapitres/avant_propos.md",
        "../chapitres/chapitre01.md",
        "../chapitres/chapitre02.md",
        "../chapitres/chapitre03.md",
        "../chapitres/chapitre04.md",
        "../chapitres/chapitre05.md",
        "../chapitres/chapitre06.md",
        "../chapitres/chapitre07.md",
        "../chapitres/chapitre08.md",
        "../chapitres/chapitre09.md",
        "../chapitres/chapitre10.md",
        "../chapitres/chapitre11.md",
        "../chapitres/quatrieme_couverture.md",
    ]:
        with open(file, "r", encoding="utf-8") as f:
            markdown_text = f.read()
        markdown_text = markdown_text.replace("---", "")
        markdown_text = markdown_text.replace("> **Encadré : ", "> **")
        # markdown_text = markdown_text.replace("images/", "../chapitres/images/")

        # regex = re.compile(r"## Chapitre %d*")
        markdown_text = regex.sub("## ", markdown_text)
        pdf.add_section(Section(markdown_text), user_css=css)

    pdf.meta["title"] = (
        "LLM-Assisted Software Design, a Pattern Language of New Development Practices"
    )
    pdf.meta["author"] = "S@M depuis idée de OAZ avec ChatGPT et Microsoft Copilot"

    # Save normalized PDF
    pdf_path = "../pdf/llm_assisted_software_design.pdf"
    pdf.save(pdf_path)


if __name__ == "__main__":
    export_pdf()
