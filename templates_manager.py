class TemplatesManager:
    def __init__(self):
        self.templates = {
            'Python': {
                'Flask API': {
                    'description': 'API بسيط Flask',
                    'files': {
                        'app.py': '''from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from API'})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({'received': data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
''',
                        'requirements.txt': 'flask==2.3.0\n'
                    }
                },
                'CLI Tool': {
                    'description': 'سطر اوامر',
                    'files': {
                        'main.py': '''import argparse

def main():
    parser = argparse.ArgumentParser(description='سطر الاوامر')
    parser.add_argument('--name', type=str, help='الاسم')
    args = parser.parse_args()
    
    print(f'مرحبا {args.name}')

if __name__ == '__main__':
    main()
'''
                    }
                }
            },
            'JavaScript': {
                'Express API': {
                    'description': 'API باستخدام Express',
                    'files': {
                        'server.js': '''const express = require('express');
const app = express();

app.use(express.json());

app.get('/api/data', (req, res) => {
    res.json({ message: 'Hello from API' });
});

app.post('/api/data', (req, res) => {
    const data = req.body;
    res.json({ received: data });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(\`Server running on port \${PORT}\`);
});
''',
                        'package.json': '''{
  "name": "express-api",
  "version": "1.0.0",
  "main": "server.js",
  "dependencies": {
    "express": "^4.18.0"
  }
}
'''
                    }
                }
            },
            'Go': {
                'HTTP Server': {
                    'description': 'خادم HTTP بسيط',
                    'files': {
                        'main.go': '''package main

import (
    "encoding/json"
    "log"
    "net/http"
)

type Response struct {
    Message string \`json:"message"\`
}

func handler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(Response{Message: "Hello from Go"})
}

func main() {
    http.HandleFunc("/", handler)
    log.Println("Server starting on :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
'''
                    }
                }
            }
        }
    
    def get_templates(self, language=None):
        if language:
            return self.templates.get(language, {})
        return self.templates
    
    def get_template(self, language, template_name):
        if language in self.templates:
            return self.templates[language].get(template_name)
        return None
