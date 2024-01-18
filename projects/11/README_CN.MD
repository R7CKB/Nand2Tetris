# JackCompiler: README

## 概述
JackCompiler项目是一个全面的系统，旨在将Jack编程语言代码转换为虚拟机（VM）代码。该项目分为几个关键组件：JackTokenizer、JackCompiler、CompilationEngine、SymbolTable和VMWriter。它是前一个项目（项目10）的扩展和优化，基于类似的原则。

## 组件
### JackTokenizer
`JackTokenizer` 负责将Jack源文件分解为其组成的标记。它处理各种标记类型，如关键字、符号、整数、字符串和标识符。它还管理注释删除和标记解析。

### CompilationEngine
`CompilationEngine` 接收`JackTokenizer`生成的标记，并将它们编译成VM代码。它处理类、类变量声明、子程序、参数列表、子程序主体以及各种语句和表达式的编译。

### SymbolTable
`SymbolTable` 用于跟踪标识符（如变量和子程序名称）的范围和属性。它管理不同种类标识符的索引（静态、字段、参数、局部），支持定义新变量、重置表格以及查询变量类型和索引等操作。

### VMWriter
`VMWriter` 负责将VM代码写入输出文件。它提供了写入VM命令的函数，包括推送和弹出操作、算术/逻辑操作、标签声明、跳转语句、函数调用和返回语句。

### JackCompiler（主驱动程序）
这个类驱动整个编译过程。它可以处理单个文件和目录输入，管理编译流程，并利用`CompilationEngine`处理找到的每个Jack文件。

## 使用方法
要使用`JackCompiler`，请实例化它，并提供指向Jack文件或包含Jack文件的目录的路径。然后，调用`compile()`方法。例如：

```python
compiler = JackCompiler("path/to/JackFile.jack")
compiler.compile()
```

## 依赖关系
- Python标准库
  - 用于文件操作的`glob`和`os.path`
  - 用于正则表达式处理的`re`
  - 用于定义枚举类的`enum`

## 贡献
这个项目欢迎贡献。对于重大更改，请先提出问题，以讨论您想要进行的更改。请确保适当更新测试。

## 致谢
这个项目在一定程度上基于Sherry Dang在 [此链接](https://github.com/sherrydang/Nand2Tetris/blob/master/project11/CompilationEngine.py) 上的工作。为了适应新的要求，进行了重大修改和优化。

## 联系方式
如有进一步的问题或贡献，请联系 R7CKB@qq.com。