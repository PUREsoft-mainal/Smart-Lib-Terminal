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