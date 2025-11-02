import streamlit as st
from translator import CodeTranslator
from fallback_translator import FallbackTranslator
from project_manager import ProjectManager
from storage_manager import StorageManager
from github_explorer import GitHubExplorer
from dependency_checker import DependencyChecker
from gamification import GamificationSystem
from templates_manager import TemplatesManager
from error_checker import ErrorChecker
from tutorials import TutorialsManager
from python_runner import PythonRunner
from file_editor import FileEditor
from so_compiler import SOCompiler
from openai_handler import OpenAIHandler
from code_validator import CodeValidator
from project_sharing import ProjectSharing
from languages import get_language_list, get_language_count
from snippets import get_snippets
from translations import get_translation
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter
import os
import base64
import json
from datetime import datetime

st.set_page_config(
    page_title="Code Translator Pro MERO Edition",
    page_icon="icon",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'translator' not in st.session_state:
    st.session_state.translator = CodeTranslator()
if 'fallback_translator' not in st.session_state:
    st.session_state.fallback_translator = FallbackTranslator()
if 'project_manager' not in st.session_state:
    st.session_state.project_manager = ProjectManager()
if 'storage_manager' not in st.session_state:
    st.session_state.storage_manager = StorageManager()
if 'github_explorer' not in st.session_state:
    st.session_state.github_explorer = GitHubExplorer()
if 'dependency_checker' not in st.session_state:
    st.session_state.dependency_checker = DependencyChecker()
if 'gamification' not in st.session_state:
    st.session_state.gamification = GamificationSystem()
if 'templates_manager' not in st.session_state:
    st.session_state.templates_manager = TemplatesManager()
if 'error_checker' not in st.session_state:
    st.session_state.error_checker = ErrorChecker()
if 'tutorials_manager' not in st.session_state:
    st.session_state.tutorials_manager = TutorialsManager()
if 'python_runner' not in st.session_state:
    st.session_state.python_runner = PythonRunner()
if 'file_editor' not in st.session_state:
    st.session_state.file_editor = FileEditor()
if 'so_compiler' not in st.session_state:
    st.session_state.so_compiler = SOCompiler()
if 'openai_handler' not in st.session_state:
    st.session_state.openai_handler = OpenAIHandler()
if 'code_validator' not in st.session_state:
    st.session_state.code_validator = CodeValidator()
if 'project_sharing' not in st.session_state:
    st.session_state.project_sharing = ProjectSharing()
if 'source_code' not in st.session_state:
    st.session_state.source_code = ""
if 'translated_code' not in st.session_state:
    st.session_state.translated_code = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'current_project' not in st.session_state:
    st.session_state.current_project = None
if 'ui_language' not in st.session_state:
    st.session_state.ui_language = "ar"
if 'theme_mode' not in st.session_state:
    st.session_state.theme_mode = "dark"
if 'font_size' not in st.session_state:
    st.session_state.font_size = 14
if 'show_line_numbers' not in st.session_state:
    st.session_state.show_line_numbers = True
if 'auto_save' not in st.session_state:
    st.session_state.auto_save = False

languages = get_language_list()

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

def apply_custom_css(theme="dark", font_size=14):
    bg_image = get_base64_image("space_background.png")
    
    if theme == "dark":
        bg_color = "rgba(15, 15, 30, 0.97)"
        text_color = "#ffffff"
        card_bg = "rgba(25, 25, 45, 0.85)"
        input_bg = "#1a1a2e"
        input_text = "#e0e0e0"
        border_color = "rgba(100, 100, 200, 0.3)"
    else:
        bg_color = "rgba(245, 245, 255, 0.97)"
        text_color = "#1a1a2e"
        card_bg = "rgba(255, 255, 255, 0.95)"
        input_bg = "#ffffff"
        input_text = "#1a1a2e"
        border_color = "rgba(100, 100, 200, 0.2)"
    
    css = f"""
    <style>
    .stApp {{
        background-image: url('data:image/png;base64,{bg_image}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main {{
        background: {bg_color};
        backdrop-filter: blur(12px);
    }}
    .stTextArea textarea {{
        font-family: 'Courier New', 'Monaco', monospace;
        font-size: {font_size}px;
        background-color: {input_bg};
        color: {input_text};
        border-radius: 8px;
        border: 1px solid {border_color};
        line-height: 1.6;
    }}
    .stButton>button {{
        background: linear-gradient(90deg, #2193b0 0%, #6dd5ed 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        padding: 12px 32px;
        font-size: 15px;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(33, 147, 176, 0.4);
    }}
    h1, h2, h3, h4 {{
        color: {text_color};
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
        font-weight: 700;
    }}
    .card {{
        background: {card_bg};
        padding: 24px;
        border-radius: 12px;
        text-align: center;
        color: {text_color};
        margin: 16px 0;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
        border: 1px solid {border_color};
    }}
    .stat-box {{
        background: {card_bg};
        padding: 16px;
        border-radius: 10px;
        margin: 8px 0;
        border: 1px solid {border_color};
    }}
    .history-item {{
        background: {card_bg};
        padding: 12px;
        border-radius: 8px;
        margin: 8px 0;
        border-left: 4px solid #2193b0;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def t(key, **kwargs):
    return get_translation(st.session_state.ui_language, key, **kwargs)

apply_custom_css(st.session_state.theme_mode, st.session_state.font_size)

st.markdown(f"""
<div style='text-align: center; padding: 24px;'>
    <h1>{t('app_title')}</h1>
    <p style='color: white; font-size: 1.3em; text-shadow: 2px 2px 6px rgba(0,0,0,0.5);'>{t('subtitle')}</p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class='card'>
    <h3>{t('developer')}</h3>
    <p>{t('telegram')}</p>
    <p>{t('supports', count=get_language_count())}</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(f"## {t('settings')}")
    
    lang_col1, lang_col2 = st.columns(2)
    with lang_col1:
        if st.button("English", use_container_width=True, key="lang_en"):
            st.session_state.ui_language = "en"
            st.rerun()
    with lang_col2:
        if st.button("العربية", use_container_width=True, key="lang_ar"):
            st.session_state.ui_language = "ar"
            st.rerun()
    
    api_key = st.text_input(t('api_key'), type="password", 
                            value=os.getenv("GEMINI_API_KEY", ""),
                            help=t('api_key_help'))
    
    if api_key:
        os.environ["GEMINI_API_KEY"] = api_key
        st.session_state.translator = CodeTranslator()
        st.success(t('api_key_set'))
    else:
        st.info("التطبيق يعمل بدون مفتاح في الوضع الاساسي. اضف المفتاح للحصول على ترجمة بالذكاء الاصطناعي.")
    
    st.markdown("---")
    st.markdown("### OpenAI API (اختياري)")
    
    openai_key = st.text_input("مفتاح OpenAI", type="password", 
                               help="احصل على مفتاح من platform.openai.com", key="openai_key_input")
    
    if openai_key:
        success, msg = st.session_state.openai_handler.set_api_key(openai_key)
        if success:
            st.success(msg)
            
            selected_model = st.selectbox("اختار النموذج", 
                                         st.session_state.openai_handler.get_models(),
                                         key="openai_model_select")
            st.session_state.openai_handler.set_model(selected_model)
        else:
            st.error(msg)
    
    st.markdown("---")
    st.markdown(f"## {t('theme')}")
    
    theme_col1, theme_col2 = st.columns(2)
    with theme_col1:
        if st.button(t('dark_mode'), use_container_width=True, key="theme_dark"):
            st.session_state.theme_mode = "dark"
            st.rerun()
    with theme_col2:
        if st.button(t('light_mode'), use_container_width=True, key="theme_light"):
            st.session_state.theme_mode = "light"
            st.rerun()
    
    st.markdown("---")
    st.markdown(f"## {t('advanced_settings')}")
    
    st.session_state.font_size = st.slider(t('font_size'), 10, 24, st.session_state.font_size)
    st.session_state.show_line_numbers = st.checkbox(t('line_numbers'), value=st.session_state.show_line_numbers)
    st.session_state.auto_save = st.checkbox(t('auto_save'), value=st.session_state.auto_save)
    
    st.markdown("---")
    st.markdown(f"## {t('projects')}")
    
    projects = st.session_state.project_manager.get_all_projects()
    
    if projects:
        project_names = {pid: p['name'] for pid, p in projects.items()}
        selected_project = st.selectbox(t('projects'), 
                                       [t('new_project')] + list(project_names.values()), key="proj_select")
        
        if selected_project != t('new_project'):
            for pid, name in project_names.items():
                if name == selected_project:
                    project_data = st.session_state.project_manager.get_project(pid)
                    st.session_state.source_code = project_data['source_code']
                    st.session_state.translated_code = project_data.get('translated_code', '')
                    st.session_state.current_project = pid
                    st.info(t('loaded', name=selected_project))
                    
                    if st.button(t('delete_project'), key="del_proj"):
                        st.session_state.project_manager.delete_project(pid)
                        st.session_state.current_project = None
                        st.rerun()
                    break
    
    st.markdown("---")
    st.markdown(f"## {t('snippets')}")
    
    snippet_lang = st.selectbox(t('snippet_lang'), languages, key="snippet_lang_sel")
    snippets = get_snippets(snippet_lang)
    
    if snippets:
        snippet_name = st.selectbox(t('select_snippet'), list(snippets.keys()), key="snippet_sel")
        if st.button(t('insert_snippet'), key="insert_snip"):
            st.session_state.source_code = snippets[snippet_name]
            st.rerun()

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16 = st.tabs([
    t('translator'), 
    t('analysis'),
    t('files'),
    t('history'),
    t('statistics'),
    "GitHub Explorer",
    "Dependency Checker",
    "Templates",
    "Tutorials",
    "Gamification",
    "محرر الملفات",
    "Python Runner",
    "SO Compiler",
    "تحدث مع AI",
    "معرفة اخطاء الكود",
    "مشاركة المشروع"
])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### {t('source_code')}")
        source_lang = st.selectbox(t('source_lang'), languages, key="source_lang")
        
        uploaded_file = st.file_uploader(t('upload_file'), 
                                        type=['py', 'js', 'java', 'cpp', 'c', 'go', 'rs', 'php', 'rb', 
                                              'swift', 'kt', 'cs', 'html', 'css', 'sql', 'txt', 'json', 
                                              'xml', 'yaml', 'sh', 'bat', 'ps1'], 
                                        key="upload_src")
        if uploaded_file:
            st.session_state.source_code = uploaded_file.read().decode('utf-8')
            st.toast(t('file_loaded'))
        
        source_code = st.text_area(t('write_code'), 
                                   value=st.session_state.source_code,
                                   height=450,
                                   key="source_input")
        st.session_state.source_code = source_code
        
        if st.session_state.source_code:
            lines = len(st.session_state.source_code.split('\n'))
            chars = len(st.session_state.source_code)
            st.caption(f"{t('lines_of_code')}: {lines} | {t('characters')}: {chars}")
    
    with col2:
        st.markdown(f"### {t('translated_code')}")
        target_lang = st.selectbox(t('target_lang'), languages, key="target_lang")
        
        if st.session_state.translated_code:
            st.code(st.session_state.translated_code, language=target_lang.lower(), line_numbers=True)
            lines_t = len(st.session_state.translated_code.split('\n'))
            chars_t = len(st.session_state.translated_code)
            st.caption(f"{t('lines_of_code')}: {lines_t} | {t('characters')}: {chars_t}")
        else:
            st.info("النتيجة راح تطلع هون")
    
    col_btn1, col_btn2, col_btn3, col_btn4, col_btn5 = st.columns(5)
    
    with col_btn1:
        if st.button(t('translate_code'), use_container_width=True, key="translate_btn"):
            if source_code:
                with st.spinner(t('translating')):
                    if api_key:
                        result = st.session_state.translator.translate_code(
                            source_code, source_lang, target_lang
                        )
                    else:
                        result = st.session_state.fallback_translator.basic_translate(
                            source_code, source_lang, target_lang
                        )
                    st.session_state.translated_code = result
                    st.session_state.storage_manager.add_to_history(
                        source_code, result, source_lang, target_lang
                    )
                    points_earned = st.session_state.gamification.complete_translation(source_lang, target_lang)
                    st.toast(f"{t('notification_success')} +{points_earned} نقطة")
                    st.rerun()
            else:
                st.warning(t('enter_code_first'))
    
    with col_btn2:
        project_name_input = st.text_input(t('project_name'), 
                                          key="project_name_input", 
                                          placeholder=t('enter_project_name'))
        if st.button(t('save_project'), use_container_width=True, key="save_proj_btn"):
            if project_name_input and source_code:
                pid = st.session_state.project_manager.create_project(
                    project_name_input, source_lang, target_lang, 
                    source_code, st.session_state.translated_code
                )
                st.success(t('project_saved', name=project_name_input))
                st.toast(t('project_saved', name=project_name_input))
                st.rerun()
            elif not project_name_input:
                st.warning(t('enter_project_name_warning'))
            else:
                st.warning(t('enter_source_code'))
    
    with col_btn3:
        if st.button(t('copy_code'), use_container_width=True, key="copy_btn"):
            if st.session_state.translated_code:
                st.code(st.session_state.translated_code, language=target_lang.lower())
                st.info(t('code_ready'))
                st.toast(t('code_ready'))
    
    with col_btn4:
        if st.button(t('format_code'), use_container_width=True, key="format_btn"):
            if st.session_state.source_code:
                st.toast("تم تنسيق الكود")
    
    with col_btn5:
        if st.button(t('clear_all'), use_container_width=True, key="clear_btn"):
            st.session_state.source_code = ""
            st.session_state.translated_code = ""
            st.toast(t('notification_success'))
            st.rerun()

with tab2:
    st.markdown(f"### {t('analysis')}")
    
    if st.button(t('analyze_source'), key="analyze_btn"):
        if st.session_state.source_code:
            with st.spinner(t('analyzing')):
                analysis = st.session_state.translator.analyze_code(
                    st.session_state.source_code, source_lang
                )
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(t('lines_of_code'), analysis['lines'])
                with col2:
                    st.metric(t('characters'), analysis['characters'])
                with col3:
                    st.metric(t('language'), analysis['language'])
                
                if 'ai_analysis' in analysis:
                    st.markdown(f"#### {t('ai_analysis')}")
                    st.write(analysis['ai_analysis'])
                
                st.toast(t('notification_success'))
        else:
            st.warning(t('enter_code_to_analyze'))

with tab3:
    st.markdown(f"### {t('file_storage')}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"#### {t('upload_file')}")
        uploaded_file_storage = st.file_uploader("اختار ملف الكود", 
                                                 type=['py', 'js', 'java', 'cpp', 'c', 'go', 'rs', 
                                                       'php', 'rb', 'swift', 'kt', 'cs', 'html', 'css', 
                                                       'sql', 'txt', 'json', 'xml', 'yaml'],
                                                 key="upload_storage")
        if uploaded_file_storage:
            content = uploaded_file_storage.read().decode('utf-8')
            filename = uploaded_file_storage.name
            
            if st.button(t('save_to_storage'), key="save_storage_btn"):
                file_id = st.session_state.storage_manager.save_file(
                    filename, content, source_lang, target_lang
                )
                st.success(t('file_saved'))
                st.toast(t('file_saved'))
                st.rerun()
    
    with col2:
        st.markdown(f"#### {t('storage_files')}")
        stored_files = st.session_state.storage_manager.get_all_files()
        
        if stored_files:
            for file_id, file_data in stored_files.items():
                with st.expander(file_data['filename']):
                    st.write(f"اللغة: {file_data['source_lang']} -> {file_data['target_lang']}")
                    st.write(f"التاريخ: {file_data['created_at']}")
                    st.code(file_data['content'][:200] + "..." if len(file_data['content']) > 200 else file_data['content'])
                    
                    col_a, col_b = st.columns(2)
                    with col_a:
                        if st.button(t('load_from_storage'), key=f"load_{file_id}"):
                            st.session_state.source_code = file_data['content']
                            st.toast(t('file_loaded'))
                            st.rerun()
                    with col_b:
                        if st.button(t('delete_file'), key=f"del_{file_id}"):
                            st.session_state.storage_manager.delete_file(file_id)
                            st.toast(t('file_deleted'))
                            st.rerun()
        else:
            st.info(t('no_files'))
    
    st.markdown("---")
    st.markdown(f"#### {t('download_file')}")
    if st.session_state.translated_code:
        file_extension = ".txt"
        if target_lang.lower() == "python":
            file_extension = ".py"
        elif target_lang.lower() in ["javascript", "js"]:
            file_extension = ".js"
        elif target_lang.lower() == "java":
            file_extension = ".java"
        elif target_lang.lower() in ["c++", "cpp"]:
            file_extension = ".cpp"
        
        col_d1, col_d2, col_d3 = st.columns(3)
        with col_d1:
            st.download_button(
                label=t('download_file'),
                data=st.session_state.translated_code,
                file_name=f"translated_code{file_extension}",
                mime="text/plain",
                use_container_width=True,
                key="download_main"
            )
        with col_d2:
            json_export = json.dumps({
                'source_code': st.session_state.source_code,
                'translated_code': st.session_state.translated_code,
                'source_lang': source_lang,
                'target_lang': target_lang,
                'timestamp': datetime.now().isoformat()
            }, ensure_ascii=False, indent=2)
            st.download_button(
                label=t('export_json'),
                data=json_export,
                file_name="translation.json",
                mime="application/json",
                use_container_width=True,
                key="download_json"
            )
        with col_d3:
            txt_export = f"المصدر ({source_lang}):\n{st.session_state.source_code}\n\n{'='*50}\n\nالمترجم ({target_lang}):\n{st.session_state.translated_code}"
            st.download_button(
                label=t('export_txt'),
                data=txt_export,
                file_name="translation.txt",
                mime="text/plain",
                use_container_width=True,
                key="download_txt"
            )

with tab4:
    st.markdown(f"### {t('history')}")
    
    col_h1, col_h2 = st.columns([3, 1])
    with col_h1:
        search_query = st.text_input(t('search'), placeholder=t('search_placeholder'), key="search_hist")
    with col_h2:
        if st.button(t('clear_history'), key="clear_hist_btn"):
            st.session_state.storage_manager.clear_history()
            st.toast(t('notification_success'))
            st.rerun()
    
    if search_query:
        history = st.session_state.storage_manager.search_in_history(search_query)
        st.info(f"تم العثور على {len(history)} نتيجة")
    else:
        history = st.session_state.storage_manager.get_history(20)
    
    if history:
        for i, entry in enumerate(history):
            with st.expander(f"{entry['source_lang']} -> {entry['target_lang']} | {entry['timestamp'][:16]}"):
                col_e1, col_e2 = st.columns(2)
                with col_e1:
                    st.markdown(f"**{t('original')}:**")
                    st.code(entry['source_code'][:300] + "..." if len(entry['source_code']) > 300 else entry['source_code'])
                with col_e2:
                    st.markdown(f"**{t('translated')}:**")
                    st.code(entry['translated_code'][:300] + "..." if len(entry['translated_code']) > 300 else entry['translated_code'])
                
                if st.button("استخدم هذه الترجمة", key=f"use_hist_{i}"):
                    st.session_state.source_code = entry['source_code']
                    st.session_state.translated_code = entry['translated_code']
                    st.rerun()
    else:
        st.info(t('no_history'))

with tab5:
    st.markdown(f"### {t('statistics')}")
    
    stats = st.session_state.storage_manager.get_stats()
    
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    
    with col_s1:
        st.markdown("<div class='stat-box'>", unsafe_allow_html=True)
        st.metric(t('total_translations'), stats['total_translations'])
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_s2:
        st.markdown("<div class='stat-box'>", unsafe_allow_html=True)
        st.metric(t('total_projects'), len(st.session_state.project_manager.get_all_projects()))
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_s3:
        st.markdown("<div class='stat-box'>", unsafe_allow_html=True)
        st.metric(t('lines_of_code'), stats['total_lines_translated'])
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_s4:
        st.markdown("<div class='stat-box'>", unsafe_allow_html=True)
        st.metric(t('favorite_language'), stats['favorite_language'])
        st.markdown("</div>", unsafe_allow_html=True)
    
    if stats['language_usage']:
        st.markdown("#### استخدام اللغات")
        for lang_pair, count in sorted(stats['language_usage'].items(), key=lambda x: x[1], reverse=True)[:10]:
            st.write(f"{lang_pair}: {count} ترجمة")

with tab6:
    st.markdown("### GitHub Explorer - تصفح مشاريع GitHub")
    
    search_query = st.text_input("ابحث عن مشاريع GitHub", placeholder="مثال: python web scraper")
    
    col_g1, col_g2 = st.columns([3, 1])
    
    with col_g1:
        search_lang = st.selectbox("فلتر حسب اللغة", ["الكل"] + languages[:20], key="github_lang")
    
    with col_g2:
        search_btn = st.button("ابحث", key="github_search_btn", use_container_width=True)
    
    if search_btn and search_query:
        with st.spinner("قاعد يدور..."):
            lang_filter = None if search_lang == "الكل" else search_lang
            repos = st.session_state.github_explorer.search_repositories(search_query, lang_filter, 5)
            
            if repos:
                for repo in repos:
                    with st.expander(f"{repo['name']} - {repo['stargazers_count']} نجمة"):
                        st.write(f"**الوصف:** {repo.get('description', 'ما في وصف')}")
                        st.write(f"**اللغة:** {repo.get('language', 'غير محدد')}")
                        st.write(f"**الرابط:** {repo['html_url']}")
                        
                        if st.button(f"شوف الملفات", key=f"view_{repo['id']}", use_container_width=True):
                            st.session_state[f'show_files_{repo["id"]}'] = True
                        
                        if st.session_state.get(f'show_files_{repo["id"]}', False):
                            contents = st.session_state.github_explorer.get_repository_contents(
                                repo['owner']['login'], repo['name']
                            )
                            if contents:
                                st.markdown("**الملفات:**")
                                for item in contents[:15]:
                                    col_f1, col_f2 = st.columns([4, 1])
                                    with col_f1:
                                        if item['type'] == 'file':
                                            st.write(f"📄 {item['name']}")
                                        else:
                                            st.write(f"📁 {item['name']}")
                                    
                                    with col_f2:
                                        if item['type'] == 'file':
                                            if st.button("شوف", key=f"read_{item['name']}_{repo['id']}"):
                                                file_content = st.session_state.github_explorer.get_file_content(
                                                    repo['owner']['login'], repo['name'], item['path']
                                                )
                                                if file_content:
                                                    st.code(file_content[:1000], language='text')
                                                    if st.button("حمل للترجمة", key=f"load_{item['name']}"):
                                                        st.session_state.source_code = file_content
                                                        st.toast("تم تحميل الكود")
                                                        st.rerun()
            else:
                st.info("ما في نتائج")

with tab7:
    st.markdown("### Dependency Checker - فحص المكتبات")
    
    if st.session_state.source_code:
        if st.button("فحص المكتبات", key="check_deps_btn"):
            deps_analysis = st.session_state.dependency_checker.analyze_code(
                st.session_state.source_code, source_lang
            )
            
            st.markdown(f"#### وجدنا {deps_analysis['count']} مكتبة:")
            for dep in deps_analysis['dependencies']:
                st.write(f"- {dep}")
            
            if deps_analysis['count'] > 0:
                st.markdown("#### بدائل للغات اخرى:")
                for dep in deps_analysis['dependencies']:
                    with st.expander(f"بدائل لـ {dep}"):
                        for target_l in ['Python', 'JavaScript', 'Java', 'Go']:
                            if target_l != source_lang:
                                alt = st.session_state.dependency_checker.suggest_alternatives(dep, source_lang, target_l)
                                st.write(f"**{target_l}:** {alt}")
    else:
        st.info("اكتب كود اول عشان نفحص المكتبات")

with tab8:
    st.markdown("### Templates - قوالب جاهزة")
    
    template_lang = st.selectbox("اختار اللغة", ['Python', 'JavaScript', 'Go'], key="template_lang_sel")
    templates = st.session_state.templates_manager.get_templates(template_lang)
    
    if templates:
        template_name = st.selectbox("اختار القالب", list(templates.keys()), key="template_name_sel")
        template = templates[template_name]
        
        st.markdown(f"**الوصف:** {template['description']}")
        
        for filename, content in template['files'].items():
            with st.expander(f"📄 {filename}"):
                st.code(content, language=template_lang.lower())
                if st.button(f"استخدم {filename}", key=f"use_template_{filename}"):
                    st.session_state.source_code = content
                    st.toast("تم نسخ القالب")
                    st.rerun()

with tab9:
    st.markdown("### Tutorials - دروس تفاعلية")
    
    tutorials_list = st.session_state.tutorials_manager.get_all_tutorials()
    selected_tutorial = st.selectbox("اختار الدرس", tutorials_list, key="tutorial_sel")
    
    if selected_tutorial:
        tutorial = st.session_state.tutorials_manager.get_tutorial(selected_tutorial)
        
        for i, step in enumerate(tutorial['steps'], 1):
            with st.expander(f"{step['title']}"):
                st.markdown(f"**الشرح:** {step['explanation']}")
                
                col_t1, col_t2 = st.columns(2)
                with col_t1:
                    st.markdown("**Python:**")
                    st.code(step['python'], language='python')
                with col_t2:
                    st.markdown("**JavaScript:**")
                    st.code(step['javascript'], language='javascript')

with tab10:
    st.markdown("### Gamification - التحديات والانجازات")
    
    stats_game = st.session_state.gamification.get_stats()
    
    col_g1, col_g2, col_g3, col_g4 = st.columns(4)
    
    with col_g1:
        st.metric("النقاط", stats_game['points'])
    with col_g2:
        st.metric("المستوى", stats_game['level'])
    with col_g3:
        st.metric("سلسلة الايام", stats_game['streak_days'])
    with col_g4:
        st.metric("عدد الترجمات", stats_game['translations_count'])
    
    st.markdown("### الانجازات:")
    if stats_game['badges']:
        cols = st.columns(4)
        for i, badge in enumerate(stats_game['badges']):
            with cols[i % 4]:
                st.success(f"🏆 {badge}")
    else:
        st.info("ابدأ الترجمة عشان تحصل على انجازات")
    
    st.markdown("### التحدي اليومي:")
    challenge = st.session_state.gamification.get_daily_challenge()
    st.info(f"{challenge['title']} - {challenge['points']} نقطة")

with tab11:
    st.markdown("### محرر الملفات - فتح وتعديل الملفات")
    
    files_list = st.session_state.file_editor.list_files(".")
    
    if files_list:
        selected_file = st.selectbox("اختار ملف", ["-- اختار ملف --"] + files_list, key="file_editor_sel")
        
        if selected_file != "-- اختار ملف --":
            success, content = st.session_state.file_editor.read_file(selected_file)
            
            if success:
                st.markdown(f"**الملف:** {selected_file}")
                edited_content = st.text_area("عدل الملف:", value=content, height=400, key="file_editor_content")
                
                col_e1, col_e2, col_e3 = st.columns(3)
                
                with col_e1:
                    if st.button("احفظ التعديلات", key="save_file_btn"):
                        save_success, save_msg = st.session_state.file_editor.write_file(selected_file, edited_content)
                        if save_success:
                            st.success(save_msg)
                        else:
                            st.error(save_msg)
                
                with col_e2:
                    if st.button("حمل الملف للترجمة", key="load_to_trans_btn"):
                        st.session_state.source_code = edited_content
                        st.toast("تم تحميل الكود للمترجم")
                        st.rerun()
                
                with col_e3:
                    file_info = st.session_state.file_editor.get_file_info(selected_file)
                    if file_info:
                        st.caption(f"الحجم: {file_info['size']} بايت")
            else:
                st.error(content)
    else:
        st.info("ما في ملفات للعرض")
    
    st.markdown("---")
    st.markdown("### انشئ ملف جديد")
    new_file_name = st.text_input("اسم الملف الجديد", placeholder="example.py", key="new_file_name")
    new_file_content = st.text_area("محتوى الملف:", height=200, key="new_file_content")
    
    if st.button("انشئ الملف", key="create_file_btn"):
        if new_file_name:
            success, msg = st.session_state.file_editor.write_file(new_file_name, new_file_content)
            if success:
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)
        else:
            st.warning("اكتب اسم الملف")

with tab12:
    st.markdown("### Python Runner - شغل سكريبتات Python")
    
    py_available, py_version = st.session_state.python_runner.check_python()
    
    if py_available:
        st.success(f"Python موجود: {py_version}")
    else:
        st.error("Python مو موجود")
    
    st.markdown("#### شغل سكريبت Python:")
    python_code = st.text_area("اكتب السكريبت:", height=300, key="python_code_input",
                               value="print('مرحبا من Python')")
    
    if st.button("شغل السكريبت", key="run_python_btn"):
        if python_code:
            with st.spinner("قاعد يشتغل..."):
                success, output = st.session_state.python_runner.run_script(python_code)
                if success:
                    st.markdown("**النتيجة:**")
                    st.code(output, language="text")
                else:
                    st.error(f"خطأ: {output}")
        else:
            st.warning("اكتب كود اول")
    
    st.markdown("---")
    st.markdown("#### ثبت مكتبة Python:")
    
    col_p1, col_p2 = st.columns([3, 1])
    
    with col_p1:
        package_name = st.text_input("اسم المكتبة", placeholder="requests", key="package_name_input")
    
    with col_p2:
        if st.button("ثبت", key="install_package_btn"):
            if package_name:
                with st.spinner(f"قاعد يثبت {package_name}..."):
                    success, msg = st.session_state.python_runner.install_package(package_name)
                    if success:
                        st.success(msg)
                    else:
                        st.error(msg)
            else:
                st.warning("اكتب اسم المكتبة")
    
    if st.button("شوف المكتبات المثبتة", key="show_packages_btn"):
        packages = st.session_state.python_runner.get_installed_packages()
        st.code(packages, language="text")

with tab13:
    st.markdown("### SO Compiler - حول لملفات SO للاندرويد")
    
    st.info("هذي الاداة تحول ملفات Python ل C عشان الاندرويد (32/64 bit)")
    
    py_files_in_project = [f for f in os.listdir('.') if f.endswith('.py') and not f.startswith('.')]
    
    if py_files_in_project:
        st.markdown("#### اختار ملف للتحويل:")
        selected_py_file = st.selectbox("الملف:", py_files_in_project, key="so_file_sel")
        
        arch_option = st.radio("العمارة:", ["both", "armeabi-v7a (32-bit)", "arm64-v8a (64-bit)"], 
                              key="arch_sel", index=0)
        
        arch_map = {
            "both": "both",
            "armeabi-v7a (32-bit)": "armeabi-v7a",
            "arm64-v8a (64-bit)": "arm64-v8a"
        }
        
        if st.button("حول الملف", key="compile_so_btn"):
            with st.spinner("قاعد يحول..."):
                result = st.session_state.so_compiler.compile_to_so(selected_py_file, arch_map[arch_option])
                
                if result['success']:
                    st.success(result['message'])
                    if result['files']:
                        st.markdown("**الملفات المنشأة:**")
                        for f in result['files']:
                            st.write(f"- {f}")
                else:
                    st.error(result['message'])
        
        st.markdown("---")
        st.markdown("#### حول كل المشروع:")
        if st.button("حول كل الملفات", key="compile_all_btn"):
            with st.spinner("قاعد يحول كل الملفات..."):
                results = st.session_state.so_compiler.compile_all_project()
                
                if results:
                    for r in results:
                        if r['result']['success']:
                            st.success(f"{r['file']}: {r['result']['message']}")
                        else:
                            st.error(f"{r['file']}: {r['result']['message']}")
                else:
                    st.warning("ما في ملفات للتحويل")
    else:
        st.info("ما في ملفات Python في المشروع")
    
    st.markdown("---")
    st.markdown("### ملاحظات:")
    st.write("- الملفات المحولة راح تكون في مجلد `apk_build`")
    st.write("- التحويل يحتاج Cython (راح يتثبت تلقائي)")
    st.write("- بعد التحويل تقدر تستخدم الملفات في تطبيق اندرويد")

with tab14:
    st.markdown("### تحدث مع AI - محادثة ذكية")
    
    if st.session_state.openai_handler.is_connected:
        st.success("OpenAI متصل")
        
        for msg in st.session_state.chat_history:
            if msg['role'] == 'user':
                st.markdown(f"**انت:** {msg['content']}")
            else:
                st.markdown(f"**AI:** {msg['content']}")
        
        user_input = st.text_area("اسأل AI اي شي عن البرمجة:", height=100, key="ai_chat_input")
        
        if st.button("ارسل", key="send_ai_btn"):
            if user_input:
                st.session_state.chat_history.append({'role': 'user', 'content': user_input})
                
                with st.spinner("AI قاعد يفكر..."):
                    success, response = st.session_state.openai_handler.chat(user_input)
                    
                    if success:
                        st.session_state.chat_history.append({'role': 'assistant', 'content': response})
                        st.rerun()
                    else:
                        st.error(response)
        
        if st.button("امسح المحادثة", key="clear_chat_btn"):
            st.session_state.chat_history = []
            st.rerun()
    else:
        st.warning("حط مفتاح OpenAI في الاعدادات عشان تستخدم هذي الميزة")

with tab15:
    st.markdown("### معرفة اخطاء الكود - فحص دقيق")
    
    validator_lang = st.selectbox("اختار اللغة للفحص:", 
                                  ['Python', 'JavaScript', 'Java', 'C', 'C++'],
                                  key="validator_lang_sel")
    
    code_to_validate = st.text_area("حط الكود هنا:", height=400, key="code_validator_input")
    
    if st.button("فحص الاخطاء", key="validate_code_btn"):
        if code_to_validate:
            errors = st.session_state.code_validator.validate_code(code_to_validate, validator_lang)
            
            if errors:
                st.markdown(f"### وجدنا {len(errors)} خطأ:")
                
                for error in errors:
                    error_type = error.get('type', 'error')
                    
                    if error_type == 'syntax':
                        st.error(f"🔴 {error['message']}")
                    elif error_type == 'indentation':
                        st.warning(f"🟡 {error['message']}")
                    elif error_type == 'brackets':
                        st.error(f"🔴 {error['message']}")
                    else:
                        st.info(f"ℹ️ {error['message']}")
                
                st.markdown("---")
                st.markdown("### الكود مع الاخطاء:")
                
                lines = code_to_validate.split('\n')
                error_lines = {e['line'] for e in errors if e.get('line', 0) > 0}
                
                highlighted_code = []
                for i, line in enumerate(lines, 1):
                    if i in error_lines:
                        highlighted_code.append(f"❌ {i}: {line}")
                    else:
                        highlighted_code.append(f"   {i}: {line}")
                
                st.code('\n'.join(highlighted_code), language='text')
            else:
                st.success("✅ ما في اخطاء! الكود تمام")
        else:
            st.warning("اكتب كود اول")

with tab16:
    st.markdown("### مشاركة المشروع - شارك شغلك")
    
    if st.session_state.source_code:
        project_share_name = st.text_input("اسم المشروع للمشاركة:", 
                                          placeholder="مشروع رهيب", key="share_name_input")
        
        if st.button("انشئ رابط مشاركة", key="create_share_btn"):
            if project_share_name:
                share_data = {
                    'name': project_share_name,
                    'source_code': st.session_state.source_code,
                    'translated_code': st.session_state.translated_code,
                    'source_lang': source_lang if 'source_lang' in locals() else 'Python',
                    'target_lang': target_lang if 'target_lang' in locals() else 'JavaScript'
                }
                
                share_id, share_url = st.session_state.project_sharing.create_share_link(share_data)
                
                message = st.session_state.project_sharing.create_shareable_message(share_url, project_share_name)
                
                st.success("تم انشاء الرابط!")
                st.code(share_url, language='text')
                
                st.markdown("### رسالة المشاركة:")
                st.text_area("انسخ هذي الرسالة:", value=message, height=150, key="share_msg_display")
            else:
                st.warning("اكتب اسم المشروع")
    else:
        st.info("اكتب كود اول عشان تقدر تشاركه")
    
    st.markdown("---")
    st.markdown("### تحميل الملفات:")
    
    if st.session_state.source_code or st.session_state.translated_code:
        if st.button("صدر الملفات", key="export_files_btn"):
            files = st.session_state.project_sharing.export_project_files({
                'source_code': st.session_state.source_code,
                'translated_code': st.session_state.translated_code,
                'source_lang': 'py',
                'target_lang': 'js'
            })
            
            for file in files:
                st.download_button(
                    label=f"حمل {file['name']}",
                    data=file['content'],
                    file_name=file['name'],
                    key=f"download_{file['name']}"
                )

with tab1:
    st.markdown(f"""
    ### عن البرنامج - Code Translator Pro MERO Edition
    
    **مترجم الاكواد -
    #### المميزات الرئيسية:
    - ترجمة بالذكاء الاصطناعي باستخدام Google Gemini
    - يعمل بدون مفتاح API في الوضع الاساسي
    - وضع ليلي ونهاري مع تبديل فوري
    - واجهة متعددة اللغات (عربي/انجليزي)
    - رفع وتنزيل ملفات الاكواد
    - نظام كامل لادارة المشاريع
    - تخزين دائم للملفات
    - سجل كامل للترجمات
    - احصائيات مفصلة
    - بحث في السجل
    - تصدير بصيغ متعددة (TXT, JSON)
    - مكتبة قوالب جاهزة لكل اللغات
    - تحليل للاكواد
    - اعدادات (حجم الخط، ارقام الاسطر، حفظ تلقائي)
    - محرر كود مع syntax highlighting
    
    #### اللغات المدعومة ({get_language_count()}+):
    Python, JavaScript, TypeScript, Java, C, C++, C#, Go, Rust, PHP, Ruby, Swift, 
    Kotlin, Dart, Scala, R, MATLAB, Perl, Haskell, Elixir, WebAssembly, و180+ لغة اخرى
    
    #### معلومات المطور:
    - الاسم: MERO
    - التواصل: @QP4RM (تلجرام)
    
    #### المفتاح (اختياري):
    - البرنامج يعمل بدون مفتاح في الوضع الاساسي
    - اضف مفتاح Gemini للحصول على ترجمة بالذكاء الاصطناعي
    - احصل على مفتاح مجاني: https://makersuite.google.com/app/apikey
    
  
     MERO | @QP4RM
    """)

st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: white; padding: 20px; text-shadow: 2px 2px 6px rgba(0,0,0,0.5);'>
    <p>{t('developer')} | {t('telegram')}</p>
    <p>{t('supports', count=get_language_count())} | </p>
</div>
""", unsafe_allow_html=True)
