import json
import os
from datetime import datetime

class ProjectManager:
    def __init__(self):
        self.projects_file = "projects.json"
        self.projects = self.load_projects()
    
    def load_projects(self):
        if os.path.exists(self.projects_file):
            with open(self.projects_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_projects(self):
        with open(self.projects_file, 'w', encoding='utf-8') as f:
            json.dump(self.projects, f, ensure_ascii=False, indent=2)
    
    def create_project(self, name, source_lang, target_lang, source_code, translated_code=""):
        project_id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.projects[project_id] = {
            'name': name,
            'source_lang': source_lang,
            'target_lang': target_lang,
            'source_code': source_code,
            'translated_code': translated_code,
            'created_at': datetime.now().isoformat()
        }
        self.save_projects()
        return project_id
    
    def get_project(self, project_id):
        return self.projects.get(project_id)
    
    def update_project(self, project_id, **kwargs):
        if project_id in self.projects:
            self.projects[project_id].update(kwargs)
            self.save_projects()
            return True
        return False
    
    def delete_project(self, project_id):
        if project_id in self.projects:
            del self.projects[project_id]
            self.save_projects()
            return True
        return False
    
    def get_all_projects(self):
        return self.projects
