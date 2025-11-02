import json
import os
from datetime import datetime

class StorageManager:
    def __init__(self):
        self.storage_file = "file_storage.json"
        self.history_file = "translation_history.json"
        self.stats_file = "statistics.json"
        self.storage_data = self.load_storage()
        self.history_data = self.load_history()
        self.stats_data = self.load_stats()
    
    def load_storage(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def load_stats(self):
        if os.path.exists(self.stats_file):
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "total_translations": 0,
            "total_projects": 0,
            "language_usage": {},
            "total_lines_translated": 0
        }
    
    def save_storage(self):
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump(self.storage_data, f, ensure_ascii=False, indent=2)
    
    def save_history(self):
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history_data, f, ensure_ascii=False, indent=2)
    
    def save_stats(self):
        with open(self.stats_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats_data, f, ensure_ascii=False, indent=2)
    
    def save_file(self, filename, content, source_lang, target_lang):
        file_id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.storage_data[file_id] = {
            'filename': filename,
            'content': content,
            'source_lang': source_lang,
            'target_lang': target_lang,
            'created_at': datetime.now().isoformat()
        }
        self.save_storage()
        return file_id
    
    def load_file(self, file_id):
        return self.storage_data.get(file_id)
    
    def delete_file(self, file_id):
        if file_id in self.storage_data:
            del self.storage_data[file_id]
            self.save_storage()
            return True
        return False
    
    def get_all_files(self):
        return self.storage_data
    
    def add_to_history(self, source_code, translated_code, source_lang, target_lang):
        history_entry = {
            'id': datetime.now().strftime("%Y%m%d%H%M%S%f"),
            'source_code': source_code,
            'translated_code': translated_code,
            'source_lang': source_lang,
            'target_lang': target_lang,
            'timestamp': datetime.now().isoformat()
        }
        self.history_data.insert(0, history_entry)
        if len(self.history_data) > 100:
            self.history_data = self.history_data[:100]
        self.save_history()
        self.update_stats(source_lang, target_lang, len(source_code.split('\n')))
    
    def get_history(self, limit=20):
        return self.history_data[:limit]
    
    def clear_history(self):
        self.history_data = []
        self.save_history()
    
    def update_stats(self, source_lang, target_lang, lines):
        self.stats_data["total_translations"] += 1
        self.stats_data["total_lines_translated"] += lines
        
        lang_pair = f"{source_lang}->{target_lang}"
        if lang_pair not in self.stats_data["language_usage"]:
            self.stats_data["language_usage"][lang_pair] = 0
        self.stats_data["language_usage"][lang_pair] += 1
        
        self.save_stats()
    
    def get_stats(self):
        stats = self.stats_data.copy()
        if stats["language_usage"]:
            most_used = max(stats["language_usage"].items(), key=lambda x: x[1])
            stats["favorite_language"] = most_used[0]
        else:
            stats["favorite_language"] = "None"
        return stats
    
    def search_in_history(self, query):
        results = []
        for entry in self.history_data:
            if query.lower() in entry['source_code'].lower() or query.lower() in entry['translated_code'].lower():
                results.append(entry)
        return results
