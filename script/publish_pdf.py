from markdown_pdf import MarkdownPdf, Section


def export_pdf(files, outputfile: str, css_file: str, paper_size: str = "A4"):
    with open(css_file, "r", encoding="utf-8") as f:
        css = f.read()

    pdf = MarkdownPdf(toc_level=3, optimize=True)
    pdf.borders = (50, 50, 50, 50)

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            markdown_text = f.read()
        markdown_text = markdown_text.replace("---", "")
        markdown_text = markdown_text.replace(" **Encadré : ", " **")
        markdown_text = markdown_text.replace(" **Encadré — ", " **")

        pdf.add_section(Section(markdown_text, paper_size=paper_size), user_css=css)

    pdf.meta["title"] = (
        "LLM-Assisted Software Design, a Pattern Language of New Development Practices"
    )
    pdf.meta["author"] = "S@M depuis idée de OAZ avec ChatGPT et Microsoft Copilot"

    # Save normalized PDF
    pdf_path = outputfile
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
        ],
        "../build/valided_llm_assisted_software_design.pdf",
        "../ressources/pdf.css",
    )
