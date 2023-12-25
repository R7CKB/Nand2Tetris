## Jack Analyzer Readme

### Project Overview
This Jack Analyzer project is divided into three main parts: `JackTokenizer`, `CompilationEngine`, and `JackAnalyzer`. The project is designed for Project 10 and doesn’t include a code generator. It references concepts from Project 8 and Project 9.

### Project Structure
- **JackTokenizer:** Handles the input by recognizing individual tokens. It classifies tokens into keywords, symbols, identifiers, integer constants, and string constants.

- **CompilationEngine:** Handles the parsing process. It parses the Jack source code, recognizes different structures, and generates corresponding XML output. The output is written to a file specified by the user.

- **JackAnalyzer:** Drives the translation process. It initializes the appropriate components based on whether the input is a single file or a directory.

### Usage
1. **JackAnalyzer Class:**
    - Initialize the `JackAnalyzer` class with the file or directory path as an argument.
    - Use the `compile()` method to start the compilation process.

2. **JackTokenizer Class:**
    - Handles tokenization of the input source code.
    - The `process()` method creates a list of tokens.
    - The `hasMoreTokens()` method checks if there are more tokens.
    - The `advance()` method moves to the next token.
    - Token information can be accessed using methods such as `keyWord()`, `symbol()`, `identifier()`, `intVal()`, and `stringVal()`.

3. **CompilationEngine Class:**
    - Handles parsing of the tokenized input.
    - The `compileClass()`, `compileClassVarDec()`, `compileSubroutine()`, and other methods parse different components of the Jack code.
    - Outputs the parsed structure in XML format.

4. **JackAnalyzer Usage Example:**
    ```python
    from JackAnalyzer import JackAnalyzer

    # Example with a directory
    analyzer = JackAnalyzer("Square")
    analyzer.compile()

    # Example with a single file
    analyzer = JackAnalyzer("Square/Main.jack")
    analyzer.compile()
    ```

### Additional Notes
- The project requires the presence of a Jack source code file or a directory containing multiple Jack files.
- The XML output is generated for each Jack source code file.
- To generate a file containing only tokens (`xxxT.xml`), use the `compileToken()` method.

### Project-Specific Considerations
- Unlike previous projects (8 and 9), this project requires the recognition of individual tokens rather than reading lines.
- The XML output includes tags such as `<keyword>`, `<symbol>`, `<identifier>`, `<integerConstant>`, and `<stringConstant>`.
- The project aims to enhance readability without using excessive indentation.

Feel free to refer to the provided code and modify it according to your project requirements.