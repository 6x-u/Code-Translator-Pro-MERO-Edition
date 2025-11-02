LANGUAGES = [
    "Python", "JavaScript", "TypeScript", "Java", "C", "C++", "C#", "Go", "Rust",
    "PHP", "Ruby", "Swift", "Kotlin", "Dart", "Scala", "R", "MATLAB", "Perl",
    "Haskell", "Elixir", "Erlang", "Clojure", "F#", "OCaml", "Lua", "Julia",
    "Groovy", "Assembly", "COBOL", "Fortran", "Ada", "Pascal", "Delphi",
    "VB.NET", "PowerShell", "Bash", "Shell", "Awk", "Sed", "SQL", "PL/SQL",
    "T-SQL", "MySQL", "PostgreSQL", "MongoDB", "Redis", "HTML", "CSS", "SCSS",
    "SASS", "Less", "XML", "JSON", "YAML", "TOML", "Markdown", "LaTeX",
    "Objective-C", "Verilog", "VHDL", "Solidity", "Move", "Cairo", "Vyper",
    "Racket", "Scheme", "Common Lisp", "Crystal", "Nim", "Zig", "V", "D",
    "Chapel", "Pony", "Elm", "PureScript", "ReasonML", "Hack", "ActionScript",
    "CoffeeScript", "Apex", "ABAP", "LabVIEW", "Scratch", "Smalltalk", "Prolog",
    "Mercury", "Idris", "Agda", "Coq", "Lean", "Isabelle", "ML", "SML",
    "Standard ML", "Cyclone", "Eiffel", "Modula-2", "Modula-3", "Oberon",
    "Objective-J", "Pike", "PL/I", "Rexx", "Ring", "Raku", "REBOL", "Red",
    "S", "SAS", "Simula", "SPARK", "Squirrel", "Stata", "Tcl", "Vala",
    "APL", "Bash", "Boo", "ColdFusion", "Component Pascal", "Curl", "E",
    "Eiffel", "Erlang", "Euphoria", "F*", "Falcon", "Fantom", "Felix",
    "Forth", "Fortress", "FoxPro", "GAP", "Genie", "Golo", "Gosu", "Groovy",
    "Haxe", "Hope", "Icon", "Inform", "Io", "Ioke", "J", "JASS", "JScript",
    "Jolie", "Joy", "K", "Korn Shell", "LabVIEW", "Lasso", "Limbo", "Lingo",
    "Lisp", "Logo", "Logtalk", "LotusScript", "LPC", "Lustre", "M4", "Maple",
    "Mathematica", "Max", "MEL", "Metafont", "Miranda", "Miva", "ML", "Modula",
    "Monkey", "MQL4", "MS-DOS Batch", "MUMPS", "NATURAL", "Nemerle", "nesC",
    "NetLogo", "NetRexx", "NewLISP", "NEWP", "NQC", "NSIS", "Nu", "NXT-G",
    "Obix", "Object Pascal", "Occam", "OpenCL", "OpenEdge ABL", "Oz", "ParaSail",
    "PARI/GP", "PEARL", "PeopleCode", "Pico", "PL/0", "Pliant", "PLEX",
    "PostScript", "PPL", "Processing", "Q", "Qore", "QtScript", "Rapira",
    "RPG", "S-Lang", "SAM76", "SASL", "Sather", "Sawzall", "Scilab", "Self",
    "SETL", "SIGNAL", "SLIP", "SMALL", "SNOBOL", "SPARK", "Speedcode", "SPIN",
    "StataQL", "Strand", "Stutter", "SuperCollider", "SVG", "TACL", "TAL",
    "Tcl", "Tea", "TECO", "TELCOMP", "TeX", "TIE", "TMG", "Toi", "TOM",
    "Transcript", "TTCN", "Turing", "TUTOR", "TXL", "TypeScript", "Ubercode",
    "UNITY", "UnrealScript", "Verilog-AMS", "Visual Basic", "Visual DataFlex",
    "Visual DialogScript", "Visual FoxPro", "Visual J#", "Visual LISP", "Visual Objects",
    "Visual Prolog", "VSXu", "WATFIV", "WebAssembly", "WebDNA", "Whiley", "Winbatch",
    "Wolfram", "XBase", "XBase++", "XC", "XMOS", "XOTcl", "XPL", "XPL0", "XQuery",
    "XSB", "XSLT", "Xtend", "Yorick", "YQL", "Zeno", "ZPL", "ZSH"
]

def get_language_list():
    return sorted(LANGUAGES)

def get_language_count():
    return len(LANGUAGES)
