# -*- coding: utf-8 -*-

from .base_document import Document



class WritableDocument(Document):

    def save(self):
        print(f"Saving document {self.file_name}")
