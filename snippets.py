SNIPPETS = {
    "Python": {
        "Hello World": "print('Hello, World!')",
        "Function": "def function_name(param):\n    return param",
        "Class": "class ClassName:\n    def __init__(self):\n        pass",
        "For Loop": "for i in range(10):\n    print(i)",
        "If Statement": "if condition:\n    pass\nelse:\n    pass"
    },
    "JavaScript": {
        "Hello World": "console.log('Hello, World!');",
        "Function": "function functionName(param) {\n    return param;\n}",
        "Arrow Function": "const func = (param) => {\n    return param;\n};",
        "Class": "class ClassName {\n    constructor() {\n    }\n}",
        "For Loop": "for (let i = 0; i < 10; i++) {\n    console.log(i);\n}"
    },
    "Java": {
        "Hello World": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}",
        "Method": "public int methodName(int param) {\n    return param;\n}",
        "Class": "public class ClassName {\n    private int value;\n    public ClassName() {\n    }\n}"
    },
    "C++": {
        "Hello World": "#include <iostream>\n\nint main() {\n    std::cout << \"Hello, World!\" << std::endl;\n    return 0;\n}",
        "Function": "int functionName(int param) {\n    return param;\n}",
        "Class": "class ClassName {\npublic:\n    ClassName() {}\n};"
    },
    "C#": {
        "Hello World": "using System;\n\nclass Program {\n    static void Main() {\n        Console.WriteLine(\"Hello, World!\");\n    }\n}",
        "Method": "public int MethodName(int param) {\n    return param;\n}",
        "Class": "public class ClassName {\n    public ClassName() {\n    }\n}"
    },
    "Go": {
        "Hello World": "package main\n\nimport \"fmt\"\n\nfunc main() {\n    fmt.Println(\"Hello, World!\")\n}",
        "Function": "func functionName(param int) int {\n    return param\n}",
        "Struct": "type StructName struct {\n    Field int\n}"
    },
    "Rust": {
        "Hello World": "fn main() {\n    println!(\"Hello, World!\");\n}",
        "Function": "fn function_name(param: i32) -> i32 {\n    param\n}",
        "Struct": "struct StructName {\n    field: i32,\n}"
    },
    "PHP": {
        "Hello World": "<?php\necho 'Hello, World!';\n?>",
        "Function": "function functionName($param) {\n    return $param;\n}",
        "Class": "class ClassName {\n    public function __construct() {\n    }\n}"
    },
    "Ruby": {
        "Hello World": "puts 'Hello, World!'",
        "Method": "def method_name(param)\n  param\nend",
        "Class": "class ClassName\n  def initialize\n  end\nend"
    },
    "Swift": {
        "Hello World": "print(\"Hello, World!\")",
        "Function": "func functionName(param: Int) -> Int {\n    return param\n}",
        "Class": "class ClassName {\n    init() {\n    }\n}"
    }
}

def get_snippets(language):
    return SNIPPETS.get(language, {})

def get_all_snippets():
    return SNIPPETS
