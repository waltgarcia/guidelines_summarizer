# Guidelines Summarizer

The "guidelines_summarizer" is a Python script that generates a summary of the "Guía de Referencia Rápida" a PDF document provided by the Secretaría de Salud of Mexico on the Catálogo Maestro. 
The summary is generated in MD format and includes the main information of each guideline, currently:
- Main definition
- Risk factors
- Diagnosis
- Treatment

## Usage

To use the script, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Place your "Guía de Referencia Rápida" PDF document in the same directory as the `summarizer.py` file.
4. Run the `summarizer.py` script using the following command: 

   ```
   python summarizer.py -i <input_file> -o <output_file>
   ```

   Replace `<input_file>` with the name of your PDF document, and `<output_file>` with the desired name of the output MD file.

5. Check the directory for the output MD file.

## Future Features

In future versions, the "guidelines_summarizer" script will include the following features:

- Exporting graphs and diagrams of the document as a PNG and archiving them in a different folder.
- Iterating within the elements of a folder with not just one guideline, but all the guidelines published by the Secretaría de Salud.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch with your changes.
3. Submit a pull request.

## License

This project is licensed under the MIT License. Please see the `LICENSE` file for more information.

If you have any questions or issues, please feel free to contact the author.
