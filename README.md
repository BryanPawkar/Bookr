# Bookr - Luxury Book Review Platform

<div align="center">

![Bookr](https://img.shields.io/badge/Django-5.2-success?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**A sophisticated, Bugatti-inspired book review platform built with Django**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation)

</div>

---

## 📖 Overview

**Bookr** is an elegant, minimalist book review platform that brings together literature enthusiasts in a sophisticated digital space. Inspired by the timeless design philosophy of luxury brands like Bugatti, Bookr features a pure black and white aesthetic with premium typography and intuitive user experience.

### Design Philosophy

> "Beauty through simplicity, elegance through restraint"

Bookr embodies:
- **Minimalist Design** - Pure black and white color scheme
- **Premium Typography** - Playfair Display & Inter fonts
- **Sophisticated UX** - Clean navigation and intuitive interactions
- **Responsive Layout** - Beautiful on all devices
- **Performance First** - Fast, efficient, and accessible

---

## ✨ Features

### 📚 Core Functionality

- **Book Catalog Management**
  - Comprehensive book database with ISBN tracking
  - Publisher and contributor management
  - Publication date tracking
  - Book cover image support
  - Sample file downloads

- **Review System**
  - User-generated reviews with 5-star ratings
  - Edit and delete capabilities for review authors
  - Average rating calculations
  - Review timestamps and edit history

- **Search & Discovery**
  - Full-text search across book titles
  - Contributor name search
  - Advanced filtering options
  - Recently viewed books tracking (session-based)

- **User Authentication**
  - Secure login/logout system
  - User profiles with activity tracking
  - Permission-based access control
  - Staff vs. regular user distinctions

### 🎨 Design Features

- **Bugatti-Inspired Aesthetics**
  - Pure black (#000000) background
  - White (#FFFFFF) typography and elements
  - Playfair Display serif headings
  - Inter sans-serif body text
  - Generous whitespace and minimal borders

- **Interactive Elements**
  - Smooth hover animations
  - Card elevation effects
  - Subtle opacity transitions
  - Clean form styling

- **Book Cover Display**
  - Elegant image rendering
  - Graceful fallback for missing covers
  - Responsive image sizing
  - Optimized loading

### 🛠️ Technical Features

- **RESTful API** (Django REST Framework)
  - Book listings endpoint
  - Contributor data access
  - JSON serialization
  - API documentation ready

- **Custom Management Commands**
  - CSV data import (`loadcsv`)
  - Database population utilities
  - Automated data migration

- **Custom Template Tags & Filters**
  - Reusable UI components
  - Data formatting helpers
  - Template logic abstraction

- **Media Management**
  - Book cover uploads
  - Sample file handling
  - Optimized image processing with Pillow

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- SQLite (included with Python)
- Virtual environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/CapBraco/Bookr.git
cd Bookr
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- Django >= 3.0
- djangorestframework
- Pillow (for image processing)

### Step 4: Database Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 5: Load Sample Data (Optional)

```bash
# Load sample books, publishers, and reviews
python manage.py loadcsv --csv reviews/management/commands/WebDevWithDjangoData.csv
```

This will populate your database with:
- 21 books
- 10 publishers
- 20 contributors
- 18 reviews
- 3 test user accounts

### Step 6: Run Development Server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

---

## 📂 Project Structure

```
bookr/
├── bookr/                          # Project configuration
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # Main URL routing
│   ├── views.py                    # Profile views
│   └── wsgi.py                     # WSGI configuration
│
├── reviews/                        # Main application
│   ├── models.py                   # Data models
│   ├── views.py                    # View functions
│   ├── urls.py                     # App URL routing
│   ├── forms.py                    # Form definitions
│   ├── admin.py                    # Admin configuration
│   ├── serializers.py              # API serializers
│   ├── api_views.py                # API endpoints
│   ├── templates/                  # HTML templates
│   │   └── reviews/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── book_list.html
│   │       ├── book_detail.html
│   │       ├── search-results.html
│   │       └── instance-form.html
│   ├── templatetags/               # Custom template tags
│   │   └── profile_tags.py
│   ├── management/                 # Custom commands
│   │   └── commands/
│   │       ├── loadcsv.py
│   │       └── WebDevWithDjangoData.csv
│   └── migrations/                 # Database migrations
│
├── book_management/                # Book CRUD app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│
├── filter_demo/                    # Template filter examples
│   ├── templatetags/
│   └── templates/
│
├── bookr_admin/                    # Custom admin site
│   └── admin.py
│
├── static/                         # Static files
│   ├── main.css                    # Main stylesheet
│   └── logo.png                    # Site logo
│
├── media/                          # User uploads
│   ├── book_covers/                # Book cover images
│   └── book_samples/               # Sample files
│
├── templates/                      # Global templates
│   ├── base.html                   # Base template
│   ├── profile.html                # User profile
│   └── registration/
│       └── login.html              # Login page
│
├── db.sqlite3                      # SQLite database
├── manage.py                       # Django CLI
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 💻 Usage

### Accessing the Application

#### Main Pages

| URL | Description |
|-----|-------------|
| `/` | Homepage with recently viewed books |
| `/books/` | Complete book collection |
| `/books/<id>/` | Individual book details |
| `/book-search/` | Search books by title or contributor |
| `/accounts/login/` | User login |
| `/accounts/profile/` | User profile page |
| `/admin/` | Django admin interface |

#### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/all_books/` | GET | List all books (JSON) |
| `/api/contributors/` | GET | List all contributors (JSON) |

### User Workflows

#### Browse Books
1. Navigate to homepage or `/books/`
2. View book cards with covers and ratings
3. Click on any book to see full details

#### Search for Books
1. Use search bar in navigation
2. Enter search term (minimum 3 characters)
3. Select search field (Title or Contributor)
4. View filtered results

#### Write a Review
1. Log in to your account
2. Navigate to a book detail page
3. Click "Add Review"
4. Enter rating (0-5) and review text
5. Submit review

#### Upload Book Covers
1. Log in with staff privileges
2. Go to book detail page
3. Click "Update Media"
4. Upload cover image and/or sample file
5. Images are automatically resized to 300x300px

### Admin Panel

Access the admin panel at `/admin/` with superuser credentials.

**Admin capabilities:**
- Manage books, publishers, contributors
- Moderate reviews
- Manage user accounts
- View all database records
- Bulk operations

---

## 🗄️ Database Schema

### Models

#### Publisher
```python
- name (CharField, max 50)
- website (URLField)
- email (EmailField)
```

#### Book
```python
- title (CharField, max 70)
- publication_date (DateField)
- isbn (CharField, max 20, unique)
- publisher (ForeignKey → Publisher)
- contributors (ManyToMany → Contributor)
- cover (ImageField, optional)
- sample (FileField, optional)
```

#### Contributor
```python
- first_names (CharField, max 50)
- last_names (CharField, max 50)
- email (EmailField)
```

#### BookContributor (Through Model)
```python
- book (ForeignKey → Book)
- contributor (ForeignKey → Contributor)
- role (CharField: AUTHOR, CO_AUTHOR, EDITOR)
```

#### Review
```python
- content (TextField)
- rating (IntegerField, 0-5)
- date_created (DateTimeField, auto)
- date_edited (DateTimeField, nullable)
- creator (ForeignKey → User)
- book (ForeignKey → Book)
```

### Relationships

```
Publisher ──< Book ──< Review
                │
                ├──< BookContributor >── Contributor
                │
                └── User (creator of reviews)
```

---

## 🎨 Customization

### Changing the Color Scheme

Edit `static/main.css`:

```css
:root {
    --pure-black: #000000;    /* Background */
    --pure-white: #FFFFFF;    /* Text/borders */
    --light-gray: #999999;    /* Secondary text */
    /* Modify these values */
}
```

### Changing Typography

In `templates/base.html` and `static/main.css`:

```css
/* Headings */
font-family: 'Playfair Display', serif;

/* Body text */
font-family: 'Inter', sans-serif;

/* Change to your preferred fonts */
```

### Adjusting Layout

Grid columns in `static/main.css`:

```css
.book-grid {
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    /* Change 300px to adjust card width */
    gap: 3rem; /* Adjust spacing */
}
```

### Adding Custom Template Tags

Create in `reviews/templatetags/`:

```python
from django import template

register = template.Library()

@register.filter
def your_custom_filter(value):
    return modified_value
```

---

## 🔧 Configuration

### Settings Overview

Key settings in `bookr/settings.py`:

```python
# Debug mode (set to False in production)
DEBUG = True

# Allowed hosts
ALLOWED_HOSTS = []  # Add your domain in production

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### Environment Variables

For production, use environment variables:

```bash
# .env file (create this)
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url
```

Install `python-decouple`:
```bash
pip install python-decouple
```

Update settings:
```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test reviews

# Run with verbosity
python manage.py test --verbosity=2

# Run specific test case
python manage.py test reviews.tests.Activity1Test
```

### Test Coverage

The project includes tests for:
- Form validation (`SearchForm`)
- View rendering (`book_search`)
- Template content verification
- Data retrieval and filtering

### Writing New Tests

Create tests in `reviews/tests.py`:

```python
from django.test import TestCase, Client

class YourTestCase(TestCase):
    def setUp(self):
        # Set up test data
        pass
    
    def test_your_feature(self):
        # Test your feature
        self.assertEqual(expected, actual)
```

---

## 📊 API Documentation

### Books API

**Endpoint:** `/api/all_books/`  
**Method:** GET  
**Authentication:** Not required

**Response:**
```json
[
  {
    "title": "Advanced Deep Learning with Keras",
    "publication_date": "2018-10-31",
    "isbn": "9781788629416",
    "publisher": {
      "name": "Packt Publishing",
      "website": "https://www.packtpub.com",
      "email": "info@packtpub.com"
    }
  }
]
```

### Contributors API

**Endpoint:** `/api/contributors/`  
**Method:** GET  
**Authentication:** Not required

**Response:**
```json
[
  {
    "first_names": "Rowel",
    "last_names": "Atienza",
    "email": "rowel.atienza@example.com",
    "bookcontributor_set": [
      {
        "book": {
          "title": "Advanced Deep Learning with Keras",
          "publication_date": "2018-10-31",
          "isbn": "9781788629416",
          "publisher": {...}
        },
        "role": "AUTHOR"
      }
    ],
    "number_contributions": 1
  }
]
```

---

## 🚢 Deployment

### Production Checklist

- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use environment variables for secrets
- [ ] Set up production database (PostgreSQL recommended)
- [ ] Configure static file serving
- [ ] Set up media file storage (S3, etc.)
- [ ] Enable HTTPS
- [ ] Configure email backend
- [ ] Set up logging
- [ ] Run `collectstatic`
- [ ] Create superuser account

### Deploying to Heroku

```bash
# Install Heroku CLI and login
heroku login

# Create Heroku app
heroku create your-app-name

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Open app
heroku open
```

### Deploying to Railway

1. Connect GitHub repository
2. Configure build settings
3. Add environment variables
4. Deploy automatically on push

### Deploying to DigitalOcean/AWS

Use gunicorn + nginx:

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn bookr.wsgi:application --bind 0.0.0.0:8000
```

Configure nginx as reverse proxy.

---

## 🛡️ Security

### Best Practices Implemented

- **CSRF Protection** - Enabled by default
- **XSS Prevention** - Template auto-escaping
- **SQL Injection Protection** - Django ORM
- **Password Hashing** - PBKDF2 algorithm
- **Session Security** - Secure cookies in production

### Additional Recommendations

```python
# In production settings.py:

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HSTS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Run tests (`python manage.py test`)
5. Commit changes (`git commit -m 'Add AmazingFeature'`)
6. Push to branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed
- Keep pull requests focused on single features

### Code Style

```python
# Good
def calculate_average_rating(reviews):
    """Calculate the average rating from a list of reviews."""
    if not reviews:
        return 0
    return sum(r.rating for r in reviews) / len(reviews)

# Use type hints when helpful
from typing import List

def get_top_books(limit: int = 10) -> List[Book]:
    return Book.objects.all()[:limit]
```

---

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2026 Bookr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Support

### Documentation

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Bootstrap 4 Docs](https://getbootstrap.com/docs/4.4/)

### Getting Help

- **Issues:** [GitHub Issues](https://github.com/CapBraco/Bookr/issues)
- **Discussions:** [GitHub Discussions](https://github.com/CapBraco/bookr/discussions)
- **Email:** dev@capbraco.com

### FAQ

**Q: How do I reset my database?**
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

**Q: Book covers aren't showing?**  
A: Ensure `MEDIA_URL` is configured and media files are being served in development.

**Q: How do I add more sample data?**  
A: Edit `WebDevWithDjangoData.csv` and run the `loadcsv` command again.

**Q: Can I use a different database?**  
A: Yes! Update `DATABASES` in settings.py. PostgreSQL is recommended for production.

---

## 🗺️ Roadmap

### Version 1.0 (Current)
- ✅ Core book catalog
- ✅ Review system
- ✅ User authentication
- ✅ Search functionality
- ✅ Elegant UI design
- ✅ RESTful API

### Version 1.1 (Planned)
- [ ] User wishlists
- [ ] Book recommendations
- [ ] Social sharing features
- [ ] Email notifications
- [ ] Advanced filtering

### Version 2.0 (Future)
- [ ] Reading lists/collections
- [ ] Book clubs feature
- [ ] Mobile app (React Native)
- [ ] GraphQL API
- [ ] Full-text search (Elasticsearch)
- [ ] Multi-language support

---

## 👥 Authors & Acknowledgments

### Core Team
- **CapBraco** - *Initial work* - [YourGitHub](https://github.com/Capbraco)

### Contributors
See the list of [contributors](https://github.com/CapBraco/Bookr/contributors) who participated in this project.

### Acknowledgments
- **Packt Publications** - For educational resources
- **Django Community** - For the excellent framework
- **Bugatti** - For design inspiration
- **Bootstrap** - For responsive framework
- **Font Awesome** - For icons
- **Google Fonts** - For typography

### Special Thanks
- Coffee ☕ - For keeping the development going
- The open-source community - For making this possible

---

## 📸 Screenshots

### Homepage
![Homepage](screenshots/homepage.png)
*Elegant landing page with recently viewed books*

### Book Collection
![Book Collection](screenshots/collection.png)
*Complete catalog with cover images and ratings*

### Book Details
![Book Details](screenshots/book-detail.png)
*Detailed book view with reviews*

### Search
![Search](screenshots/search.png)
*Powerful search functionality*

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=CapBraco/Bookr&type=Date)](https://star-history.com/#CapBraco/Bookr&Date)

---

<div align="center">

**Built with ❤️ using Django**

[⬆ Back to Top](#bookr---luxury-book-review-platform)

</div>
