import json
import os
from datetime import datetime, timedelta

class GamificationSystem:
    def __init__(self):
        self.data_file = "gamification_data.json"
        self.data = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            'points': 0,
            'level': 1,
            'badges': [],
            'challenges_completed': [],
            'streak_days': 0,
            'last_activity': None,
            'translations_count': 0,
            'languages_used': set()
        }
    
    def save_data(self):
        data_to_save = self.data.copy()
        if isinstance(data_to_save.get('languages_used'), set):
            data_to_save['languages_used'] = list(data_to_save['languages_used'])
        
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=2)
    
    def add_points(self, points, reason=""):
        self.data['points'] += points
        self.check_level_up()
        self.save_data()
        return points
    
    def check_level_up(self):
        required_points = self.data['level'] * 100
        if self.data['points'] >= required_points:
            self.data['level'] += 1
            return True
        return False
    
    def award_badge(self, badge_name):
        if badge_name not in self.data['badges']:
            self.data['badges'].append(badge_name)
            self.save_data()
            return True
        return False
    
    def complete_translation(self, source_lang, target_lang):
        self.data['translations_count'] += 1
        if isinstance(self.data.get('languages_used'), list):
            self.data['languages_used'] = set(self.data['languages_used'])
        self.data['languages_used'].add(source_lang)
        self.data['languages_used'].add(target_lang)
        
        points = 10
        self.add_points(points)
        
        if self.data['translations_count'] == 1:
            self.award_badge("اول ترجمة")
        elif self.data['translations_count'] == 10:
            self.award_badge("10 ترجمات")
        elif self.data['translations_count'] == 50:
            self.award_badge("50 ترجمة")
        elif self.data['translations_count'] == 100:
            self.award_badge("100 ترجمة")
        
        if len(self.data['languages_used']) >= 5:
            self.award_badge("اللغات")
        if len(self.data['languages_used']) >= 10:
            self.award_badge("خبير لغات")
        
        self.update_streak()
        self.save_data()
        
        return points
    
    def update_streak(self):
        today = datetime.now().date()
        
        if self.data['last_activity']:
            last_date = datetime.fromisoformat(self.data['last_activity']).date()
            if last_date == today:
                return
            elif last_date == today - timedelta(days=1):
                self.data['streak_days'] += 1
                if self.data['streak_days'] >= 7:
                    self.award_badge("اسبوع كامل")
                if self.data['streak_days'] >= 30:
                    self.award_badge("شهر كامل")
            else:
                self.data['streak_days'] = 1
        else:
            self.data['streak_days'] = 1
        
        self.data['last_activity'] = today.isoformat()
    
    def get_daily_challenge(self):
        challenges = [
            {"title": "ترجم من Python الى JavaScript", "points": 20, "lang_from": "Python", "lang_to": "JavaScript"},
            {"title": "ترجم من Java الى Go", "points": 25, "lang_from": "Java", "lang_to": "Go"},
            {"title": "ترجم من C++ الى Rust", "points": 30, "lang_from": "C++", "lang_to": "Rust"},
            {"title": "ترجم اي كود", "points": 15, "lang_from": "any", "lang_to": "any"}
        ]
        
        day_of_year = datetime.now().timetuple().tm_yday
        return challenges[day_of_year % len(challenges)]
    
    def get_stats(self):
        if isinstance(self.data.get('languages_used'), list):
            self.data['languages_used'] = set(self.data['languages_used'])
        
        return {
            'points': self.data['points'],
            'level': self.data['level'],
            'badges': self.data['badges'],
            'streak_days': self.data['streak_days'],
            'translations_count': self.data['translations_count'],
            'languages_count': len(self.data['languages_used'])
        }
