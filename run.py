from src.engine.scanner import SmartScanner
import os

# التأكد من وجود مجلد قاعدة البيانات
os.makedirs('data/db', exist_ok=True)

print("Starting Initial System Scan...")
scanner = SmartScanner()
scanner.start_scan('C:\\') # أو قم بتغييره لمجلد محدد للتجربة
print("System Ready!")