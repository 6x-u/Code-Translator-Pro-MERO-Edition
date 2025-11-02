import subprocess
import sys
import os

class PythonRunner:
    def __init__(self):
        self.python_cmd = sys.executable
    
    def check_python(self):
        try:
            result = subprocess.run([self.python_cmd, '--version'], 
                                  capture_output=True, text=True)
            return True, result.stdout.strip()
        except:
            return False, "Python مو موجود"
    
    def install_package(self, package_name):
        try:
            result = subprocess.run([self.python_cmd, '-m', 'pip', 'install', package_name],
                                  capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                return True, f"تم تثبيت {package_name}"
            else:
                return False, result.stderr
        except subprocess.TimeoutExpired:
            return False, "انتهى الوقت"
        except Exception as e:
            return False, str(e)
    
    def run_script(self, code):
        temp_file = "/tmp/temp_script.py"
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(code)
            
            result = subprocess.run([self.python_cmd, temp_file],
                                  capture_output=True, text=True, timeout=30)
            
            output = result.stdout if result.stdout else result.stderr
            return True, output
        except subprocess.TimeoutExpired:
            return False, "السكريبت اخذ وقت طويل"
        except Exception as e:
            return False, str(e)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
    
    def get_installed_packages(self):
        try:
            result = subprocess.run([self.python_cmd, '-m', 'pip', 'list'],
                                  capture_output=True, text=True)
            return result.stdout
        except:
            return "ما قدرنا نجيب القائمة"
