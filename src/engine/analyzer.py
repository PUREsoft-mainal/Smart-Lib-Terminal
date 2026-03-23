# تحديث بسيط لإضافة خاصية الكاش (Caching)
class ProjectAnalyzer:
    def __init__(self):
        self.cache = set() # لحفظ ما تم حقنه سابقاً وتجنب التكرار

    def get_required_libs(self, project_path):
        # (نفس كود البحث السابق)
        # لكن سنضيف فحصاً بسيطاً:
        new_libs = found_libs - self.cache
        self.cache.update(new_libs)
        return new_libs # إرجاع المكتبات الجديدة فقط التي لم تُحقن بعد