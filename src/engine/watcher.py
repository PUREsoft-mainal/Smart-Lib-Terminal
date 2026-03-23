from src.engine.analyzer import ProjectAnalyzer
from src.ui.main_terminal import auto_inject_library

class ProjectWatcher(FileSystemEventHandler):
    def __init__(self):
        self.analyzer = ProjectAnalyzer()

    def on_modified(self, event):
        # إذا قمت بتعديل ملف كود (حفظ التغييرات)
        if event.src_path.endswith(('.py', '.cpp', '.h', '.js')):
            print(f"[*] Detected changes in: {os.path.basename(event.src_path)}")
            self.auto_sync(os.path.dirname(event.src_path))

    def auto_sync(self, project_dir):
        # تحليل المشروع بحثاً عن المكتبات المطلوبة
        required_libs = self.analyzer.get_required_libs(project_dir)
        for lib in required_libs:
            # محاولة حقن المكتبة إذا كانت ناقصة
            auto_inject_library(lib)