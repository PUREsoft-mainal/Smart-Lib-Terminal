import os
import sys

# الحصول على المسار الحقيقي للمجلد الذي يوجد فيه الملف الآن
BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

def get_path(relative_path):
    return os.path.join(BASE_DIR, relative_path)

# الآن بدلاً من كتابة 'config/config.json' سنكتب:
# get_path('config/config.json')
# أضف هذه الدوال داخل كلاس SmartScanner السابق:

    def add_single_file(self, file_path):
        name = os.path.basename(file_path)
        path = os.path.dirname(file_path)
        self.conn.execute("INSERT INTO libs (name, path, type) VALUES (?, ?, ?)", 
                         (name, path, 'File'))
        self.conn.commit()

    def remove_single_file(self, file_path):
        name = os.path.basename(file_path)
        self.conn.execute("DELETE FROM libs WHERE name = ?", (name,))
        self.conn.commit()
