# -*- coding: utf-8 -*-

from document.base_document import Document
from document.writable_document import WritableDocument
from project.project import Project

def main():
    doc1 = Document("Read-only content", "readonly.txt")
    doc2 = WritableDocument("Editable content", "editable.txt")

    project = Project()
    project.add_document(doc1)
    project.add_document(doc2)

    print("Opening all documents:")
    project.open_all()

    print("\nSaving writable documents:")
    project.save_all()

if __name__ == "__main__":
    main()
