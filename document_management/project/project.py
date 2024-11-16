# -*- coding: utf-8 -*-

from document.writable_document import WritableDocument


class Project:
    def __init__(self):
        self.all_docs = []
        self.writable_docs = []

    def add_document(self, doc):
        self.all_docs.append(doc)
        if isinstance(doc, WritableDocument):
            self.writable_docs.append(doc)

    def open_all(self):
        for doc in self.all_docs:
            doc.open()

    def save_all(self):
        for doc in self.writable_docs:
            doc.save()
