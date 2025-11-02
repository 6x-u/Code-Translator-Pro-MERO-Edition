class TutorialsManager:
    def __init__(self):
        self.tutorials = {
            'من Python الى JavaScript': {
                'steps': [
                    {
                        'title': 'الخطوة 1: طباعة نص',
                        'python': 'print("مرحبا")',
                        'javascript': 'console.log("مرحبا");',
                        'explanation': 'في Python نستخدم print() وفي JavaScript نستخدم console.log()'
                    },
                    {
                        'title': 'الخطوة 2: المتغيرات',
                        'python': 'name = "احمد"\nage = 25',
                        'javascript': 'let name = "احمد";\nlet age = 25;',
                        'explanation': 'JavaScript تحتاج let او const و ; في نهاية السطر'
                    },
                    {
                        'title': 'الخطوة 3: الدوال',
                        'python': 'def hello(name):\n    return f"مرحبا {name}"',
                        'javascript': 'function hello(name) {\n    return `مرحبا ${name}`;\n}',
                        'explanation': 'الدوال في JavaScript تستخدم function وبين {} والقوالب النصية مع ``'
                    }
                ]
            },
            'من JavaScript الى Python': {
                'steps': [
                    {
                        'title': 'الخطوة 1: الطباعة',
                        'javascript': 'console.log("مرحبا");',
                        'python': 'print("مرحبا")',
                        'explanation': 'Python اسهل، نستخدم print() بدون ;'
                    },
                    {
                        'title': 'الخطوة 2: المتغيرات',
                        'javascript': 'const name = "احمد";',
                        'python': 'name = "احمد"',
                        'explanation': 'Python ما تحتاج const او let او ;'
                    }
                ]
            }
        }
    
    def get_tutorial(self, tutorial_name):
        return self.tutorials.get(tutorial_name)
    
    def get_all_tutorials(self):
        return list(self.tutorials.keys())
