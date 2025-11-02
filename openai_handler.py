import os

class OpenAIHandler:
    def __init__(self):
        self.api_key = None
        self.available_models = [
            'gpt-4-turbo-preview',
            'gpt-4',
            'gpt-3.5-turbo',
            'gpt-3.5-turbo-16k'
        ]
        self.current_model = 'gpt-3.5-turbo'
        self.is_connected = False
    
    def set_api_key(self, api_key):
        self.api_key = api_key
        os.environ['OPENAI_API_KEY'] = api_key
        return self.test_connection()
    
    def test_connection(self):
        if not self.api_key:
            return False, "ما في مفتاح API"
        
        try:
            import openai
            openai.api_key = self.api_key
            
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "test"}],
                max_tokens=5
            )
            self.is_connected = True
            return True, "المفتاح شغال"
        except ImportError:
            return False, "OpenAI مو مثبت"
        except Exception as e:
            self.is_connected = False
            return False, f"خطأ: {str(e)}"
    
    def chat(self, message, model=None):
        if not self.is_connected:
            return False, "المفتاح مو شغال"
        
        try:
            import openai
            openai.api_key = self.api_key
            
            response = openai.chat.completions.create(
                model=model or self.current_model,
                messages=[
                    {"role": "system", "content": "انت مساعد برمجي ذكي، اجب بالعربي"},
                    {"role": "user", "content": message}
                ],
                max_tokens=2000
            )
            
            return True, response.choices[0].message.content
        except Exception as e:
            return False, f"خطأ: {str(e)}"
    
    def analyze_code(self, code, language):
        prompt = f"""حلل هذا الكود بلغة {language} وعطني:
1. الاخطاء اذا في
2. اقتراحات للتحسين
3. ملاحظات الامان

الكود:
```
{code}
```
"""
        return self.chat(prompt)
    
    def translate_code_with_openai(self, code, source_lang, target_lang):
        prompt = f"""ترجم هذا الكود من {source_lang} الى {target_lang}.
احتفظ بنفس المنطق والبنية.

الكود:
```
{code}
```

اعطني الكود المترجم فقط """

        return self.chat(prompt)
    
    def get_models(self):
        return self.available_models
    
    def set_model(self, model):
        if model in self.available_models:
            self.current_model = model
            return True
        return False
