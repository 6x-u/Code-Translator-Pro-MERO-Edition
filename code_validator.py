import re
import ast
import json

class CodeValidator:
    def __init__(self):
        self.validators = {
            'Python': self.validate_python,
            'JavaScript': self.validate_javascript,
            'Java': self.validate_java,
            'C': self.validate_c,
            'C++': self.validate_cpp
        }
    
    def validate_python(self, code):
        errors = []
        try:
            ast.parse(code)
        except SyntaxError as e:
            errors.append({
                'line': e.lineno,
                'column': e.offset,
                'message': f"خطأ في السطر {e.lineno}: {e.msg}",
                'type': 'syntax'
            })
        except Exception as e:
            errors.append({
                'line': 0,
                'column': 0,
                'message': str(e),
                'type': 'error'
            })
        
        lines = code.split('\n')
        for i, line in enumerate(lines, 1):
            if line.strip().endswith(':') and i < len(lines):
                next_line = lines[i].strip() if i < len(lines) else ""
                if next_line and not next_line.startswith((' ', '\t')):
                    errors.append({
                        'line': i + 1,
                        'column': 0,
                        'message': f"السطر {i+1} يحتاج مسافة بادئة",
                        'type': 'indentation'
                    })
            
            if line.count('(') != line.count(')'):
                errors.append({
                    'line': i,
                    'column': 0,
                    'message': f"السطر {i}: اقواس غير متطابقة",
                    'type': 'brackets'
                })
        
        return errors
    
    def validate_javascript(self, code):
        errors = []
        lines = code.split('\n')
        
        brace_count = 0
        paren_count = 0
        
        for i, line in enumerate(lines, 1):
            brace_count += line.count('{') - line.count('}')
            paren_count += line.count('(') - line.count(')')
            
            if 'function' in line and '(' not in line:
                errors.append({
                    'line': i,
                    'column': 0,
                    'message': f"السطر {i}: function بدون اقواس",
                    'type': 'syntax'
                })
            
            if line.strip().startswith('if') and not line.strip().endswith('{'):
                if i < len(lines) and not lines[i].strip().startswith('{'):
                    errors.append({
                        'line': i,
                        'column': 0,
                        'message': f"السطر {i}: if بدون قوس فتح",
                        'type': 'syntax'
                    })
        
        if brace_count != 0:
            errors.append({
                'line': 0,
                'column': 0,
                'message': "اقواس معقوفة غير متطابقة",
                'type': 'brackets'
            })
        
        if paren_count != 0:
            errors.append({
                'line': 0,
                'column': 0,
                'message': "اقواس عادية غير متطابقة",
                'type': 'brackets'
            })
        
        return errors
    
    def validate_java(self, code):
        errors = []
        lines = code.split('\n')
        
        has_class = False
        for i, line in enumerate(lines, 1):
            if 'class ' in line:
                has_class = True
            
            if line.strip().startswith('public ') or line.strip().startswith('private '):
                if not line.strip().endswith('{') and not line.strip().endswith(';'):
                    errors.append({
                        'line': i,
                        'column': 0,
                        'message': f"السطر {i}: method/field بدون ; او {{",
                        'type': 'syntax'
                    })
        
        if not has_class and len(code.strip()) > 0:
            errors.append({
                'line': 0,
                'column': 0,
                'message': "ما في class في الكود",
                'type': 'structure'
            })
        
        return errors
    
    def validate_c(self, code):
        return self.validate_cpp(code)
    
    def validate_cpp(self, code):
        errors = []
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            if line.count('(') != line.count(')'):
                errors.append({
                    'line': i,
                    'column': 0,
                    'message': f"السطر {i}: اقواس غير متطابقة",
                    'type': 'brackets'
                })
            
            if line.count('{') != line.count('}'):
                errors.append({
                    'line': i,
                    'column': 0,
                    'message': f"السطر {i}: اقواس معقوفة غير متطابقة",
                    'type': 'brackets'
                })
        
        return errors
    
    def validate_code(self, code, language):
        if language in self.validators:
            return self.validators[language](code)
        else:
            return [{
                'line': 0,
                'column': 0,
                'message': f"اللغة {language} مو مدعومة للفحص",
                'type': 'unsupported'
            }]
    
    def format_error_message(self, error):
        return f"⚠️ {error['message']}"
