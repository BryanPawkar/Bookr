# Contributing to Bookr

First off, thank you for considering contributing to Bookr! It's people like you that make Bookr such a great tool.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Workflow](#development-workflow)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Examples of behavior that contributes to creating a positive environment include:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Examples of unacceptable behavior include:**
- The use of sexualized language or imagery
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate

---

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- Basic understanding of Django
- Familiarity with HTML/CSS

### Setting Up Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork locally:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/bookr.git
   cd bookr
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

5. **Set up the database:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**How to submit a good bug report:**

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code snippets, screenshots)
- **Describe the behavior you observed** and what you expected
- **Include details about your environment** (OS, Python version, Django version)

**Bug report template:**
```markdown
## Description
A clear description of what the bug is.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g., Windows 10, macOS 12.0]
- Python version: [e.g., 3.9.5]
- Django version: [e.g., 3.2.0]
- Browser: [e.g., Chrome 95]

## Screenshots
If applicable, add screenshots.

## Additional Context
Any other context about the problem.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues.

**How to submit a good enhancement suggestion:**

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List some examples** of how it would be used

### Your First Code Contribution

Unsure where to begin? Look for issues labeled:
- `good first issue` - Simple issues for beginners
- `help wanted` - Issues that need attention
- `documentation` - Documentation improvements

### Pull Requests

- Fill in the required template
- Follow the style guidelines
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline

---

## Development Workflow

### 1. Create an Issue

Before starting work, create or claim an issue describing what you plan to do.

### 2. Create a Branch

Branch naming conventions:
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation
- `refactor/description` - Code refactoring
- `test/description` - Test additions/fixes

Example:
```bash
git checkout -b feature/add-book-recommendations
```

### 3. Make Your Changes

Follow our coding standards and write tests for new functionality.

### 4. Test Your Changes

```bash
# Run all tests
python manage.py test

# Run specific tests
python manage.py test reviews.tests.YourTestCase

# Check code style
flake8 .

# Check for security issues
bandit -r .
```

### 5. Commit Your Changes

Follow our commit message guidelines (see below).

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Create a Pull Request

Open a PR against the `main` branch with a clear title and description.

---

## Style Guidelines

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

**Key Points:**
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters (not 79)
- Use descriptive variable names
- Add docstrings to functions and classes
- Use type hints where helpful

**Example:**
```python
from typing import List, Optional

class Book:
    """Represents a published book."""
    
    def __init__(self, title: str, isbn: str):
        """
        Initialize a Book instance.
        
        Args:
            title: The book's title
            isbn: The book's ISBN number
        """
        self.title = title
        self.isbn = isbn
    
    def get_reviews(self, limit: Optional[int] = None) -> List['Review']:
        """
        Retrieve reviews for this book.
        
        Args:
            limit: Maximum number of reviews to return
            
        Returns:
            List of Review objects
        """
        reviews = self.review_set.all()
        if limit:
            reviews = reviews[:limit]
        return list(reviews)
```

### Django-Specific Guidelines

**Models:**
```python
class Book(models.Model):
    """A published book."""
    
    # Fields ordered: required, optional, relationships
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['title']
        verbose_name = 'book'
        verbose_name_plural = 'books'
    
    def __str__(self):
        return self.title
```

**Views:**
```python
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def book_detail(request, pk):
    """Display detailed information about a book."""
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    
    context = {
        'book': book,
        'reviews': reviews,
    }
    return render(request, 'reviews/book_detail.html', context)
```

### HTML/CSS Style Guide

**HTML:**
- Use 2 spaces for indentation
- Use semantic HTML5 elements
- Include alt text for images
- Use Django template tags properly

```html
{% extends 'base.html' %}

{% block content %}
  <article class="book-detail">
    <h1>{{ book.title }}</h1>
    
    {% if book.cover %}
      <img src="{{ book.cover.url }}" alt="{{ book.title }} cover">
    {% endif %}
    
    <section class="book-info">
      <p><strong>Publisher:</strong> {{ book.publisher }}</p>
      <p><strong>ISBN:</strong> {{ book.isbn }}</p>
    </section>
  </article>
{% endblock %}
```

**CSS:**
- Use 2 spaces for indentation
- Use meaningful class names
- Group related properties
- Comment complex styles

```css
/* Book card component */
.book-card {
  /* Layout */
  display: flex;
  flex-direction: column;
  
  /* Spacing */
  padding: 2rem;
  margin-bottom: 1rem;
  
  /* Visual */
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  
  /* Animation */
  transition: transform 0.3s ease;
}

.book-card:hover {
  transform: translateY(-5px);
}
```

### JavaScript Style Guide

- Use modern ES6+ syntax
- Use `const` by default, `let` when reassignment needed
- Use template literals for string interpolation
- Add JSDoc comments for functions

```javascript
/**
 * Fetch book data from the API
 * @param {number} bookId - The ID of the book to fetch
 * @returns {Promise<Object>} The book data
 */
const fetchBook = async (bookId) => {
  try {
    const response = await fetch(`/api/books/${bookId}/`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed to fetch book:', error);
    throw error;
  }
};
```

---

## Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Test additions or changes
- `chore`: Build process or auxiliary tool changes

### Examples

**Good commit messages:**
```
feat(reviews): add star rating display to book cards

- Added star rating component
- Updated book card template
- Added CSS for star display

Closes #123
```

```
fix(search): resolve case-sensitivity in book search

Previously, search was case-sensitive causing missed results.
Now uses case-insensitive filtering.

Fixes #456
```

**Bad commit messages:**
```
fixed bug
updated stuff
changes
wip
```

### Guidelines

- Use present tense ("add feature" not "added feature")
- Use imperative mood ("move cursor to..." not "moves cursor to...")
- First line should be 50 characters or less
- Reference issues and pull requests when relevant
- Explain *what* and *why* vs. *how*

---

## Pull Request Process

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] No console errors or warnings

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe tests performed

## Screenshots
If applicable

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed
- [ ] Commented complex code
- [ ] Documentation updated
- [ ] Tests added
- [ ] All tests pass
- [ ] No new warnings

## Related Issues
Closes #issue_number
```

### Review Process

1. At least one maintainer must approve
2. All CI checks must pass
3. All comments must be resolved
4. Branch must be up-to-date with main

### After Approval

Your PR will be merged by a maintainer. You can delete your branch after merging.

---

## Testing Guidelines

### Writing Tests

```python
from django.test import TestCase, Client
from reviews.models import Book, Publisher

class BookModelTest(TestCase):
    """Test the Book model."""
    
    def setUp(self):
        """Set up test data."""
        self.publisher = Publisher.objects.create(
            name='Test Publisher',
            website='https://example.com',
            email='test@example.com'
        )
        self.book = Book.objects.create(
            title='Test Book',
            isbn='1234567890',
            publication_date='2024-01-01',
            publisher=self.publisher
        )
    
    def test_book_str_representation(self):
        """Test book string representation."""
        expected = 'Test Book (1234567890)'
        self.assertEqual(str(self.book), expected)
    
    def test_book_has_publisher(self):
        """Test book has associated publisher."""
        self.assertEqual(self.book.publisher, self.publisher)
```

### Test Coverage

Aim for at least 80% code coverage. Run coverage reports:

```bash
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

---

## Documentation

### Docstring Format

Use Google-style docstrings:

```python
def complex_function(param1, param2, param3=None):
    """
    Brief description of function.
    
    Longer description if needed. Explain what the function does,
    any important behavior, edge cases, etc.
    
    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2
        param3 (bool, optional): Description of param3. Defaults to None.
    
    Returns:
        dict: Description of return value
        
    Raises:
        ValueError: When param1 is empty
        TypeError: When param2 is not an integer
        
    Example:
        >>> result = complex_function('test', 42)
        >>> print(result)
        {'status': 'success'}
    """
    pass
```

### Updating Documentation

- Update README.md for user-facing changes
- Update code comments for implementation changes
- Update API documentation for endpoint changes
- Add examples for new features

---

## Questions?

Feel free to:
- Open an issue with the `question` label
- Reach out to maintainers
- Join our community discussions

---

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Hall of fame (coming soon!)

---

Thank you for contributing to Bookr! 🎉