from src.engine.analyzer import ProjectAnalyzer

def sync_project_dependencies():
    analyzer = ProjectAnalyzer()
    print("[*] Analyzing your project structure...")
    
    # معرفة المكتبات المطلوبة في المجلد الحالي
    required = analyzer.get_required_libs(os.getcwd())
    
    print(f"[*] Found {len(required)} potential dependencies.")
    for lib in required:
        # استدعاء دالة الحقن التي صنعناها سابقاً لكل مكتبة
        auto_inject_library(lib)

# إضافة أمر جديد في قائمة الأوامر
# إذا كتب المستخدم 'sync' سيقوم النظام بفحص المشروع وحقن كل النواقص فوراً.