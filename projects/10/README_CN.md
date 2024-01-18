## Jack分析器自述文件

### 项目概述
这个Jack分析器项目分为三个主要部分：`JackTokenizer`、`CompilationEngine`和`JackAnalyzer`。该项目设计为项目10，不包括代码生成器。它参考了项目8和项目9中的概念。

### 项目结构
- **JackTokenizer：** 处理输入，通过识别单个标记将其分类为关键字、符号、标识符、整数常量和字符串常量。

- **CompilationEngine：** 处理解析过程。它解析Jack源代码，识别不同的结构，并生成相应的XML输出。输出写入用户指定的文件。

- **JackAnalyzer：** 驱动翻译过程。它根据输入是单个文件还是目录，初始化相应的组件。

### 使用方法
1. **JackAnalyzer类：**
   - 使用文件或目录路径初始化`JackAnalyzer`类。
   - 使用`compile()`方法启动编译过程。

2. **JackTokenizer类：**
   - 处理输入源代码的标记化。
   - `process()`方法创建标记列表。
   - `hasMoreTokens()`方法检查是否还有更多标记。
   - `advance()`方法移动到下一个标记。
   - 可以使用`keyWord()`、`symbol()`、`identifier()`、`intVal()`和`stringVal()`等方法访问标记信息。

3. **CompilationEngine类：**
   - 处理标记化输入的解析。
   - `compileClass()`、`compileClassVarDec()`、`compileSubroutine()`等方法解析Jack代码的不同组件。
   - 以XML格式输出解析的结构。

4. **JackAnalyzer使用示例:**
    ```python
    from JackAnalyzer import JackAnalyzer

    # 示例使用目录
    analyzer = JackAnalyzer("Square")
    analyzer.compile()

    # 示例使用单个文件
    analyzer = JackAnalyzer("Square/Main.jack")
    analyzer.compile()
    ```

### 其他注意事项
- 项目要求存在一个Jack源代码文件或包含多个Jack文件的目录。
- 为每个Jack源代码文件生成XML输出。
- 要生成仅包含标记的文件（`xxxT.xml`），请使用`compileToken()`方法。

### 项目特定注意事项
- 与之前的项目（8和9）不同，该项目要求识别单个标记而不是读取行。
- XML输出包括标签，如 `<keyword>`、`<symbol>`、`<identifier>`、`<integerConstant>` 和 `<stringConstant>`。
- 该项目旨在提高可读性，而不使用过多的缩进。

随意参考提供的代码，并根据项目需求进行修改。