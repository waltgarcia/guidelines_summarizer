import os
import PyPDF2
import markdown
import argparse

# Create argument parser
parser = argparse.ArgumentParser(description='Summarize a PDF file')
parser.add_argument('-i', '--input', type=str, required=True, help='Input PDF file path')
parser.add_argument('-o', '--output', type=str, required=True, help='Output Markdown file path')
args = parser.parse_args()

# Open the PDF file
with open(args.input, "rb") as pdf_file:
    # Read the contents of the PDF file
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_paginas = pdf_reader.getNumPages()

    # Search for sections in each page of the PDF file
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

# Create the summary in Markdown format
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

# Write the summary to a Markdown file
with open(args.output, "w") as md_file:
    md_file.write(markdown.markdown(resumen_md))
