import time
import threading
import sys
import os
from watchdog.observers import Observer
from src.engine.watcher import LibHunterHandler, ProjectWatcher
from src.engine.scanner import SmartScanner
from src.ui.main_terminal import main_loop

def start_background_services():
    """تشغيل خدمات المراقبة والصيد في الخلفية"""
    scanner = SmartScanner()
    
    # 1. إعداد مراقب 'صيد' المكتبات الجديدة (System Hunter)
    hunter_handler = LibHunterHandler(scanner, "data/permanent_repo")
    
    # 2. إعداد مراقب 'حقن' المكتبات التلقائي للمشاريع (Auto-Injector)
    project_handler = ProjectWatcher()
    
    observer = Observer()
    
    # مراقبة القرص بالكامل للصيد (يمكن تعديل المسار حسب الحاجة)
    observer.schedule(hunter_handler, path="C:\\", recursive=True)
    
    # مراقبة مجلد العمل الحالي للحقن التلقائي للكود
    observer.schedule(project_handler, path=os.getcwd(), recursive=True)
    
    observer.start()
    print("[✓] Background Services: Active (Hunting & Auto-Injecting)")
    
    try:
        while True:
            time.sleep(5) # توفير استهلاك المعالج للأجهزة الضعيفة
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if _name_ == "_main_":
    print("""
    #########################################
    #      Smart Lib Terminal v2.0          #
    #    Self-Evolving & Auto-Injecting     #
    #########################################
    """)
    
    # التأكد من وجود المجلدات الأساسية
    os.makedirs('data/db', exist_ok=True)
    os.makedirs('data/permanent_repo', exist_ok=True)

    # تشغيل خدمات الخلفية في خيط (Thread) منفصل
    bg_thread = threading.Thread(target=start_background_services, daemon=True)
    bg_thread.start()

    # تشغيل الواجهة التفاعلية في الأمام
    try:
        main_loop()
    except Exception as e:
        print(f"[!] Terminal Error: {e}")
    finally:
        print("\n[!] System Shutting Down Safely...")