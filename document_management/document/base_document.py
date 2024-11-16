# -*- coding: utf-8 -*-


class Document:
    def __init__(self, fname, content):
        self.file_name = fname
        self.content = content

    def __str__(self):
        return f"{self.name} - {self.content}"
    
    def open(self):
        print(f"Opening document {self.file_name}")
        return self.content
