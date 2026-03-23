Set WinScriptHost = CreateObject("WScript.Shell")
' تشغيل ملف main.py باستخدام pythonw (النسخة الصامتة من بايثون)
WinScriptHost.Run "pythonw.exe main.py", 0
Set WinScriptHost = Nothing