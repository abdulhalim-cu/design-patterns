# Document Management System

This project demonstrates a document management system designed using the **SOLID principles** of object-oriented programming. It handles both read-only and writable documents, ensuring modularity, maintainability, and extensibility.

## Design Overview

### Core Design Principles
1. **Single Responsibility Principle (SRP)**:
   - The `Document` class handles the responsibility of reading/opening documents.
   - The `WritableDocument` class extends `Document` to add the responsibility of saving documents.

2. **Liskov Substitution Principle (LSP)**:
   - Any instance of `WritableDocument` can be used wherever `Document` is expected without breaking the functionality.
   - By separating writable functionality into a subclass, the base class (`Document`) remains compatible with client code.

3. **Open-Closed Principle (OCP)**:
   - The design is open for extension. For example, new types of documents like `EncryptedDocument` can be added without modifying the existing codebase.
   - The `Project` class works with the `Document` abstraction, making it flexible to accommodate new behaviors.

## Project Structure
# Document Management System

This project implements a **Document Management System** following the **SOLID principles** of object-oriented design. It allows managing both read-only and writable documents in a modular, extensible, and maintainable manner.

## Key Principles Used

### 1. Single Responsibility Principle (SRP)
- **Document**: Handles reading/opening documents.
- **WritableDocument**: Extends `Document` to handle saving functionality.

### 2. Liskov Substitution Principle (LSP)
- Objects of the `WritableDocument` subclass can seamlessly replace objects of the `Document` superclass without breaking functionality. This ensures that the subclass extends the behavior of the parent class without altering it.

### 3. Open-Closed Principle (OCP)
- The codebase is open for extension but closed for modification. For example:
  - New document types (e.g., `EncryptedDocument`) can be added without changing existing code.
  - The `Project` class works with the `Document` abstraction, making it adaptable for new behaviors.


## Project Structure

The project is divided into packages for better modularity:

```
document_management/
│
├── document/
│   ├── __init__.py
│   ├── base_document.py         # Base class for read-only documents
│   ├── writable_document.py     # Subclass for writable documents
│
├── project/
│   ├── __init__.py
│   ├── project.py               # Class to manage a collection of documents
│
└── main.py                      # Entry point to demonstrate functionality
```

## Classes and Responsibilities

### 1. Document (`document/base_document.py`)
Represents a general, read-only document.

- **Attributes**:
  - `data`: Content of the document.
  - `filename`: Name of the document file.
- **Methods**:
  - `open()`: Opens and displays the content of the document.


### 2. WritableDocument (`document/writable_document.py`)
Extends the `Document` class to add saving functionality.

- **Methods**:
  - `save()`: Saves the document and displays a confirmation message.


### 3. Project (`project/project.py`)
Manages both read-only and writable documents in a project.

- **Attributes**:
  - `all_docs`: List of all documents in the project.
  - `writable_docs`: List of writable documents in the project.
- **Methods**:
  - `add_document(doc)`: Adds a document to the project.
  - `open_all()`: Opens all documents in the project.
  - `save_all()`: Saves all writable documents in the project.


## Code Example

```python
from document.base_document import Document
from document.writable_document import WritableDocument
from project.project import Project

def main():
    # Create documents
    doc1 = Document("This is a read-only document.", "readonly.txt")
    doc2 = WritableDocument("This is a writable document.", "writable.txt")

    # Create a project and add documents
    project = Project()
    project.add_document(doc1)
    project.add_document(doc2)

    # Open and save documents
    print("Opening all documents:")
    project.open_all()

    print("\nSaving writable documents:")
    project.save_all()

if __name__ == "__main__":
    main()
```

## Running the Project

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd document_management
   ```

2. **Run the Project**:
   ```bash
   python main.py
   ```

## Example Output

```
Opening all documents:
Opening document: readonly.txt
Content: This is a read-only document.
Opening document: writable.txt
Content: This is a writable document.

Saving writable documents:
Saving document: writable.txt
```

## Advantages of the Design

1. **Separation of Concerns**:
   - Read-only and writable functionality are encapsulated in separate classes.
2. **Adherence to SOLID Principles**:
   - Enables extensibility and maintainability without altering existing code.
3. **Extensibility**:
   - Adding new document types (e.g., encrypted or compressed documents) is straightforward and does not require modifications to the core classes.
4. **Maintainability**:
   - Modular design allows easy testing and debugging.


## Future Enhancements

- Add support for `EncryptedDocument` or `CompressedDocument` by extending the `Document` base class.
- Implement additional project-level operations, such as archiving documents or generating reports.
