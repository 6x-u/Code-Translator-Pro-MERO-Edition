import json
import os
import base64
from datetime import datetime
import uuid

class ProjectSharing:
    def __init__(self):
        self.shared_projects_file = "shared_projects.json"
        self.load_shared_projects()
    
    def load_shared_projects(self):
        if os.path.exists(self.shared_projects_file):
            with open(self.shared_projects_file, 'r', encoding='utf-8') as f:
                self.shared_projects = json.load(f)
        else:
            self.shared_projects = {}
    
    def save_shared_projects(self):
        with open(self.shared_projects_file, 'w', encoding='utf-8') as f:
            json.dump(self.shared_projects, f, ensure_ascii=False, indent=2)
    
    def create_share_link(self, project_data):
        share_id = str(uuid.uuid4())[:8]
        
        share_data = {
            'id': share_id,
            'project': project_data,
            'created_at': datetime.now().isoformat(),
            'views': 0
        }
        
        self.shared_projects[share_id] = share_data
        self.save_shared_projects()
        
        domain = os.getenv('REPLIT_DOMAINS', 'localhost:5000').split(',')[0]
        share_url = f"http://{domain}?share={share_id}"
        
        return share_id, share_url
    
    def get_shared_project(self, share_id):
        if share_id in self.shared_projects:
            self.shared_projects[share_id]['views'] += 1
            self.save_shared_projects()
            return True, self.shared_projects[share_id]['project']
        return False, None
    
    def export_project_files(self, project_data):
        files = []
        
        if 'source_code' in project_data:
            files.append({
                'name': f"source.{project_data.get('source_lang', 'txt').lower()}",
                'content': project_data['source_code']
            })
        
        if 'translated_code' in project_data:
            files.append({
                'name': f"translated.{project_data.get('target_lang', 'txt').lower()}",
                'content': project_data['translated_code']
            })
        
        return files
    
    def create_shareable_message(self, share_url, project_name):
        message = f"""🔗 مشاركة مشروع: {project_name}

ادخل هنا لرؤية المشروع:
{share_url}

تم انشاء الرابط من Code Translator Pro MERO Edition
"""
        return message
