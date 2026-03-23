import threading
import time
import os
import sys

# استيراد المكونات التي برمجناها في الملفات المنفصلة
from src.engine.scanner import SmartScanner
from src.engine.watcher import LibHunterHandler, ProjectWatcher
from src.engine.analyzer import ProjectAnalyzer
from src.ui.main_terminal import main_loop
from watchdog.observers import Observer

def run_background_services():
    """تشغيل مراقب النظام (الصياد) ومراقب المشاريع (الحاقن)"""
    scanner = SmartScanner()
    repo_path = "data/permanent_repo"
    
    # التأكد من وجود المجلدات
    os.makedirs(repo_path, exist_ok=True)
    
    # إعداد المحركات
    hunter = LibHunterHandler(scanner, repo_path)
    project_injector = ProjectWatcher() # يضم المحلل (Analyzer) بداخله
    
    observer = Observer()
    
    # 1. مراقبة الهاردسك لصيد مكتبات جديدة (C:\ أو /)
    # ملاحظة: للأجهزة الضعيفة جداً يمكن تحديد مجلدات معينة بدل الهاردسك بالكامل
    observer.schedule(hunter, path="C:\\", recursive=True)
    
    # 2. مراقبة مجلد العمل الحالي للحقن التلقائي للكود
    observer.schedule(project_injector, path=os.getcwd(), recursive=True)
    
    observer.start()
    print("[✓] الخدمات الخلفية تعمل: (صيد المكتبات + الحقن التلقائي) نشط.")
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if _name_ == "_main_":
    print("-" * 40)
    print("   Smart Lib Terminal v2.0 - Active   ")
    print("   خدمة الأجهزة الضعيفة والتطوير الذكي   ")
    print("-" * 40)

    # تشغيل خدمات الخلفية في Thread منفصل لكي لا تعطل الـ Terminal
    bg_thread = threading.Thread(target=run_background_services, daemon=True)
    bg_thread.start()

    # تشغيل واجهة الأوامر الرئيسية
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\n[!] إغلاق النظام... شكراً لاستخدامك Smart Lib Terminal")
        sys.exit(0)
