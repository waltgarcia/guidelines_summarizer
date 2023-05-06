import os
import PyPDF2
import markdown

# Ruta del archivo PDF a analizar
archivo_pdf = os.path.join(os.path.expanduser("~"), "Desktop", "GRRs", "vaginitis.pdf")

# Abre el archivo PDF en modo lectura binaria
with open(archivo_pdf, "rb") as pdf_file:
    # Lee el contenido del archivo PDF
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_paginas = pdf_reader.getNumPages()

    # Busca los apartados en cada página del PDF
    definicion = ""
    factores_riesgo = ""
    interrogatorio = ""
    cuadro_clinico = ""
    diagnostico = ""
    tratamiento = ""
    escalas = ""

    for pagina in range(num_paginas):
        pagina_actual = pdf_reader.getPage(pagina)
        pagina_texto = pagina_actual.extractText()

        if "Definición" in pagina_texto:
            definicion = pagina_texto.split("Definición", 1)[-1]
        if "Factores de riesgo" in pagina_texto:
            factores_riesgo = pagina_texto.split("Factores de riesgo", 1)[-1]
        if "Interrogatorio" in pagina_texto:
            interrogatorio = pagina_texto.split("Interrogatorio", 1)[-1]
        if "Cuadro clínico" in pagina_texto:
            cuadro_clinico = pagina_texto.split("Cuadro clínico", 1)[-1]
        if "Diagnóstico" in pagina_texto:
            diagnostico = pagina_texto.split("Diagnóstico", 1)[-1]
        if "Tratamiento" in pagina_texto:
            tratamiento = pagina_texto.split("Tratamiento", 1)[-1]
        if "Escalas" in pagina_texto:
            escalas = pagina_texto.split("Escalas", 1)[-1]

# Crea el resumen en formato Markdown
resumen_md = f"""\
# Guía de práctica clínica: Vaginitis

## Definición
{definicion}

## Factores de riesgo
{factores_riesgo}

## Interrogatorio
{interrogatorio}

## Cuadro clínico
{cuadro_clinico}

## Diagnóstico
{diagnostico}

## Tratamiento
{tratamiento}

## Escalas
{escalas}
"""

# Escribe el resumen en un archivo de texto en formato Markdown
archivo_md = os.path.join(os.path.expanduser("~"), "Desktop", "GRRs", "resumen_vaginitis.md")
with open(archivo_md, "w") as md_file:
    md_file.write(markdown.markdown(resumen_md))
