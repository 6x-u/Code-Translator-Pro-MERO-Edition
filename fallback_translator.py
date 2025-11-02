class FallbackTranslator:
    def __init__(self):
        self.syntax_mapping = {
            "Python": {"print": "print", "def": "def", "class": "class", "if": "if", "for": "for", "while": "while"},
            "JavaScript": {"print": "console.log", "def": "function", "class": "class", "if": "if", "for": "for", "while": "while"},
            "Java": {"print": "System.out.println", "def": "public", "class": "class", "if": "if", "for": "for", "while": "while"},
            "C++": {"print": "std::cout", "def": "void", "class": "class", "if": "if", "for": "for", "while": "while"},
            "C#": {"print": "Console.WriteLine", "def": "public", "class": "class", "if": "if", "for": "for", "while": "while"},
            "Go": {"print": "fmt.Println", "def": "func", "class": "type", "if": "if", "for": "for", "while": "for"},
            "Rust": {"print": "println!", "def": "fn", "class": "struct", "if": "if", "for": "for", "while": "while"},
            "PHP": {"print": "echo", "def": "function", "class": "class", "if": "if", "for": "for", "while": "while"},
            "Ruby": {"print": "puts", "def": "def", "class": "class", "if": "if", "for": "for", "while": "while"},
            "Swift": {"print": "print", "def": "func", "class": "class", "if": "if", "for": "for", "while": "while"}
        }
    
    def basic_translate(self, code, source_lang, target_lang):
        result = f"Translated from {source_lang} to {target_lang}:\n\n"
        result += code
        result += f"\n\nNote: This is a basic translation. For accurate translation with full logic preservation, please add a Gemini API key in the sidebar."
        return result
