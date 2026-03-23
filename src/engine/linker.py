import os
import ctypes
import platform

class SmartLinker:
    @staticmethod
    def create_link(original_path, target_folder):
        """
        تقوم هذه الدالة بإنشاء وصلة (Link) للمكتبة الأصلية داخل مجلد مشروعك الجديد
        """
        # استخراج اسم الملف من المسار الأصلي
        file_name = os.path.basename(original_path)
        # تحديد المسار الجديد حيث سيتم وضع "الوصلة"
        destination = os.path.join(target_folder, file_name)

        try:
            if platform.system() == "Windows":
                # في ويندوز نحتاج صلاحيات المسؤول لعمل Symbolic Link للملفات
                os.symlink(original_path, destination)
            else:
                # في لينكس وماك الأمر أسهل
                os.symlink(original_path, destination)
            
            return f"Success: Linked {file_name} to your project!"
        except OSError as e:
            return f"Error: Could not create link. {e}"
        except FileExistsError:
            return "Note: Library already linked in this folder."

# مثال تجريبي سريع:
# linker = SmartLinker()
# print(linker.create_link('C:/OtherApp/bin/library.dll', './my_project/'))