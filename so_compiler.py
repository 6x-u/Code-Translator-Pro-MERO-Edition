import subprocess
import os
import shutil

class SOCompiler:
    def __init__(self):
        self.output_dir = "apk_build"
    
    def compile_to_so(self, python_file, arch="both"):
        try:
            os.makedirs(self.output_dir, exist_ok=True)
            
            result = {
                'success': False,
                'message': '',
                'files': []
            }
            
            check_cython = subprocess.run(['python3', '-m', 'pip', 'list'], 
                                        capture_output=True, text=True)
            
            if 'Cython' not in check_cython.stdout:
                install = subprocess.run(['python3', '-m', 'pip', 'install', 'Cython'],
                                       capture_output=True, text=True)
                if install.returncode != 0:
                    result['message'] = "ما قدرنا نثبت Cython"
                    return result
            
            base_name = os.path.splitext(os.path.basename(python_file))[0]
            
            archs_to_build = ['armeabi-v7a', 'arm64-v8a'] if arch == "both" else [arch]
            
            for target_arch in archs_to_build:
                try:
                    c_file = f"{self.output_dir}/{base_name}_{target_arch}.c"
                    so_file = f"{self.output_dir}/{base_name}_{target_arch}.so"
                    
                    cython_cmd = ['cython', '--embed', '-o', c_file, python_file]
                    cython_result = subprocess.run(cython_cmd, capture_output=True, text=True)
                    
                    if cython_result.returncode == 0 and os.path.exists(c_file):
                        result['files'].append(c_file)
                        result['success'] = True
                    
                except Exception as e:
                    continue
            
            if result['success']:
                result['message'] = f"تم انشاء ملفات C في {self.output_dir}"
            else:
                result['message'] = "ما قدرنا ننشئ الملفات"
            
            return result
            
        except Exception as e:
            return {
                'success': False,
                'message': f"خطأ: {str(e)}",
                'files': []
            }
    
    def compile_all_project(self):
        try:
            python_files = [f for f in os.listdir('.') if f.endswith('.py')]
            
            results = []
            for py_file in python_files:
                if py_file not in ['main.py']:
                    result = self.compile_to_so(py_file, "both")
                    results.append({
                        'file': py_file,
                        'result': result
                    })
            
            return results
        except Exception as e:
            return []
