import os
import json

class FileEditor:
    def __init__(self):
        self.supported_extensions = ['.py', '.js', '.java', '.cpp', '.c', '.go', '.rs', 
                                     '.php', '.rb', '.swift', '.kt', '.ts', '.html', 
                                     '.css', '.txt', '.md', '.json', '.xml', '.yaml']
    
    def list_files(self, directory="."):
        try:
            files = []
            for root, dirs, filenames in os.walk(directory):
                dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
                
                for filename in filenames:
                    if not filename.startswith('.'):
                        filepath = os.path.join(root, filename)
                        ext = os.path.splitext(filename)[1]
                        if ext in self.supported_extensions:
                            files.append(filepath)
            return files
        except Exception as e:
            return []
    
    def read_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return True, f.read()
        except Exception as e:
            return False, str(e)
    
    def write_file(self, filepath, content):
        try:
            os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "تم الحفظ"
        except Exception as e:
            return False, str(e)
    
    def delete_file(self, filepath):
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                return True, "تم الحذف"
            return False, "الملف مو موجود"
        except Exception as e:
            return False, str(e)
    
    def get_file_info(self, filepath):
        try:
            if os.path.exists(filepath):
                stat = os.stat(filepath)
                return {
                    'size': stat.st_size,
                    'modified': stat.st_mtime,
                    'extension': os.path.splitext(filepath)[1]
                }
            return None
        except:
            return None
