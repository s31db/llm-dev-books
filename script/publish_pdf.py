from markdown_pdf import MarkdownPdf, Section


def export_pdf(
    files,
    outputfile: str,
    css_file: str,
    paper_size: str | list | tuple,
    title: str,
    meta: dict[str, str],
) -> str:
    with open(css_file, "r", encoding="utf-8") as f:
        css = f.read()

    pdf = MarkdownPdf(toc_level=3, optimize=True)
    pdf.borders = (50, 50, 50, 50)

    borders = (36, 36, -36, -36)

    html_final = ""

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            markdown_text = f.read()
        markdown_text = markdown_text.replace("---", "")

        html_final += pdf.add_section(
            Section(markdown_text, paper_size=paper_size, borders=borders), user_css=css
        )

    pdf.meta["title"] = title
    pdf.meta["author"] = meta["author"]
    pdf.meta["producer"] = meta["publisher"]
    pdf.meta["subject"] = meta["subject"]
    pdf.meta["keywords"] = ", ".join(meta["tags"])

    # Save normalized PDF
    pdf_path = outputfile
    pdf.save(pdf_path)

    return html_final


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
