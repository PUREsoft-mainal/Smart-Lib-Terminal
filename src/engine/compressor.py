import zipfile
import os

class SmartCompressor:
    @staticmethod
    def compress_lib(file_path):
        """تحويل المكتبة إلى ملف مضغوط لتوفير المساحة"""
        zip_path = file_path + ".zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        os.remove(file_path) # حذف الأصل لتوفير المساحة
        return zip_path

    @staticmethod
    def decompress_lib(zip_path):
        """فك الضغط فوراً عند الحاجة للمكتبة"""
        extract_path = os.path.dirname(zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(extract_path)
        os.remove(zip_path) # حذف المضغوط بعد الاستخراج
        return zip_path.replace(".zip", "")