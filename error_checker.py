import re

class ErrorChecker:
    def __init__(self):
        self.checks = {
            'Python': [
                {'pattern': r'^\s*if\s+.*:\s*$', 'error': 'if بدون محتوى', 'suggestion': 'اضف كود داخل if'},
                {'pattern': r'print\(([^)]*)\)[^;]*$', 'error': None, 'suggestion': None},
                {'pattern': r'def\s+\w+\([^)]*\):\s*$', 'error': 'دالة فارغة', 'suggestion': 'اضف pass او كود'},
            ],
            'JavaScript': [
                {'pattern': r'console\.log\([^)]*\)\s*$', 'error': None, 'suggestion': None},
                {'pattern': r'function\s+\w+\([^)]*\)\s*{\s*}', 'error': 'دالة فارغة', 'suggestion': 'اضف كود داخل الدالة'},
                {'pattern': r'if\s*\([^)]+\)\s*{\s*}', 'error': 'if فارغ', 'suggestion': 'اضف كود داخل if'},
            ],
            'Java': [
                {'pattern': r'System\.out\.println\([^)]*\);', 'error': None, 'suggestion': None},
                {'pattern': r'public\s+\w+\s+\w+\([^)]*\)\s*{\s*}', 'error': 'دالة فارغة', 'suggestion': 'اضف return او كود'},
            ]
        }
    
    def check_code(self, code, language):
        if language not in self.checks:
            return {'errors': [], 'warnings': [], 'suggestions': []}
        
        errors = []
        warnings = []
        suggestions = []
        
        lines = code.split('\n')
        for i, line in enumerate(lines, 1):
            for check in self.checks[language]:
                if re.search(check['pattern'], line):
                    if check['error']:
                        errors.append({
                            'line': i,
                            'message': check['error'],
                            'suggestion': check['suggestion']
                        })
        
        if not code.strip():
            errors.append({'line': 0, 'message': 'الكود فارغ', 'suggestion': 'اكتب كود'})
        
        return {
            'errors': errors,
            'warnings': warnings,
            'suggestions': suggestions,
            'has_issues': len(errors) > 0 or len(warnings) > 0
        }
