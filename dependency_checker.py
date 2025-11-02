import re

class DependencyChecker:
    def __init__(self):
        self.language_patterns = {
            'Python': {
                'import': r'(?:from\s+(\S+)\s+)?import\s+(\S+)',
                'common_libs': ['numpy', 'pandas', 'requests', 'flask', 'django', 'fastapi', 'tensorflow', 'pytorch']
            },
            'JavaScript': {
                'import': r'(?:import\s+.*?\s+from\s+[\'"](\S+)[\'"]|require\([\'"](\S+)[\'"]\))',
                'common_libs': ['express', 'react', 'vue', 'axios', 'lodash', 'moment', 'jquery']
            },
            'Java': {
                'import': r'import\s+([\w\.]+);',
                'common_libs': ['spring', 'hibernate', 'junit', 'gson', 'jackson']
            },
            'Go': {
                'import': r'import\s+(?:"([^"]+)"|[(]([^)]+)[)])',
                'common_libs': ['gin', 'gorm', 'viper', 'cobra', 'logrus']
            }
        }
        
        self.alternatives = {
            'Python': {
                'requests': {'JavaScript': 'axios', 'Java': 'HttpClient', 'Go': 'net/http'},
                'numpy': {'JavaScript': 'mathjs', 'Java': 'Apache Commons Math', 'Go': 'gonum'},
                'flask': {'JavaScript': 'express', 'Java': 'Spring Boot', 'Go': 'gin'}
            },
            'JavaScript': {
                'express': {'Python': 'flask', 'Java': 'Spring Boot', 'Go': 'gin'},
                'axios': {'Python': 'requests', 'Java': 'HttpClient', 'Go': 'net/http'},
                'react': {'Python': 'streamlit', 'Java': 'Vaadin', 'Go': 'templ'}
            }
        }
    
    def extract_dependencies(self, code, language):
        if language not in self.language_patterns:
            return []
        
        pattern = self.language_patterns[language]['import']
        matches = re.findall(pattern, code)
        
        dependencies = set()
        for match in matches:
            if isinstance(match, tuple):
                dependencies.update([m for m in match if m])
            else:
                dependencies.add(match)
        
        return list(dependencies)
    
    def suggest_alternatives(self, dependency, source_lang, target_lang):
        if source_lang in self.alternatives:
            if dependency in self.alternatives[source_lang]:
                return self.alternatives[source_lang][dependency].get(target_lang, 'بحث يدوي مطلوب')
        return 'بحث يدوي مطلوب'
    
    def analyze_code(self, code, language):
        deps = self.extract_dependencies(code, language)
        analysis = {
            'dependencies': deps,
            'count': len(deps),
            'suggestions': {}
        }
        
        for dep in deps:
            for target_lang in ['Python', 'JavaScript', 'Java', 'Go']:
                if target_lang != language:
                    alt = self.suggest_alternatives(dep, language, target_lang)
                    if alt not in analysis['suggestions']:
                        analysis['suggestions'][alt] = []
                    analysis['suggestions'][alt].append(f"{dep} -> {target_lang}")
        
        return analysis
