import google.generativeai as genai
import os

class CodeTranslator:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
    
    def translate_code(self, source_code, source_lang, target_lang):
        if not self.model:
            return f"Error: GEMINI_API_KEY not set"
        
        prompt = f"""Translate the following {source_lang} code to {target_lang}.
Preserve all logic, structure, variables, functions, comments, and control flow.
Output ONLY the translated code without explanations.

Source Code ({source_lang}):
{source_code}

Translated Code ({target_lang}):"""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Translation Error: {str(e)}"
    
    def analyze_code(self, code, language):
        lines = code.split('\n')
        analysis = {
            'lines': len(lines),
            'characters': len(code),
            'language': language
        }
        
        if not self.model:
            analysis['ai_analysis'] = "AI analysis unavailable: GEMINI_API_KEY not set"
            return analysis
        
        prompt = f"""Analyze this {language} code and provide:
1. Code quality score (1-10)
2. Potential issues
3. Optimization suggestions

Code:
{code}"""
        
        try:
            response = self.model.generate_content(prompt)
            analysis['ai_analysis'] = response.text
        except:
            analysis['ai_analysis'] = "Analysis unavailable"
        
        return analysis
