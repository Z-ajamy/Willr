# Willr

> *"That which does not kill us makes us stronger."* — Friedrich Nietzsche

A lightweight, open-source blogging platform built with Flask. Willr is inspired by Nietzsche's concept of the **Will to Power** — the fundamental drive to create, shape, and overcome.

This isn't just another blog engine. It's a statement of intent. A platform for those who write not to record, but to **assert**. To turn thought into creation through the clarity of code and will.

---

## Philosophy

Willr embodies the spirit of creative assertion. Every post is an act of will — a manifestation of the power to shape reality through words. Like Nietzsche's *Übermensch*, Willr users don't just consume content; they create it, own it, and forge their own path.

The platform strips away the noise, leaving only what matters: your thoughts, your voice, your creation.

---

## Features

### Core Functionality
- ✍️ **User Authentication** - Register, log in, and manage your profile securely
- 📝 **Post Management** - Create, edit, and delete posts with ease
- 📰 **Clean Feed** - View all posts in a minimal, distraction-free interface
- 🔒 **Secure Data Storage** - SQLite database with proper security practices
- 🎨 **Simple Design** - Bootstrap-styled templates that get out of your way

### Technical Highlights
- **Modular Architecture** - Blueprint-based design for scalability
- **Session-Based Auth** - Secure, straightforward authentication
- **Jinja2 Templating** - Dynamic, powerful template rendering
- **Database Agnostic** - SQLite by default, configurable for other databases
- **Lightweight** - Minimal dependencies, maximum control

---

## Technical Overview

| Component | Technology |
|-----------|-----------|
| **Framework** | Flask (Python) |
| **Database** | SQLite (configurable) |
| **Authentication** | Session-based login |
| **Architecture** | Blueprint modular design |
| **Templating** | Jinja2 |
| **Styling** | Bootstrap 5 |

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Quick Start

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/willr.git
cd willr
```

#### 2. Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Initialize the Database
```bash
flask --app willr init-db
```

#### 5. Run the Application
```bash
# Development mode
flask --app willr run --debug

# Production mode
flask --app willr run
```

The application will be available at `http://127.0.0.1:5000`

---

## Project Structure

```
willr/
├── willr/
│   ├── __init__.py          # Application factory
│   ├── db.py                # Database initialization and connection
│   ├── schema.sql           # Database schema
│   ├── auth.py              # Authentication blueprint
│   ├── blog.py              # Blog blueprint
│   ├── templates/
│   │   ├── base.html        # Base template
│   │   ├── auth/
│   │   │   ├── login.html   # Login page
│   │   │   └── register.html # Registration page
│   │   └── blog/
│   │       ├── index.html   # Post feed
│   │       ├── create.html  # Create/edit post
│   │       └── update.html  # Update post
│   └── static/
│       └── style.css        # Custom styles
├── tests/
│   ├── conftest.py          # Test configuration
│   ├── test_auth.py         # Authentication tests
│   ├── test_blog.py         # Blog functionality tests
│   ├── test_db.py           # Database tests
│   └── test_factory.py      # Application factory tests
├── venv/                    # Virtual environment (not in repo)
├── instance/                # Instance folder (created on init)
│   └── willr.sqlite         # SQLite database (created on init)
├── requirements.txt         # Python dependencies
├── setup.py                 # Package setup configuration
├── MANIFEST.in             # Package manifest
├── README.md               # This file
└── .gitignore              # Git ignore rules
```

---

## Usage

### Creating Your First Post

1. **Register an Account**
   - Navigate to `/auth/register`
   - Create your username and password
   - Your will begins here

2. **Log In**
   - Go to `/auth/login`
   - Enter your credentials
   - Assert your presence

3. **Create a Post**
   - Click "New Post"
   - Write your title and body
   - Click "Save" to manifest your creation

4. **Manage Your Posts**
   - Edit: Refine your assertions
   - Delete: Remove what no longer serves your will

---

## Configuration

### Environment Variables

Create a `.env` file or set environment variables:

```bash
# Secret key for session management
export SECRET_KEY='your-secret-key-here'

# Database URI (optional, defaults to SQLite)
export DATABASE_URL='sqlite:///instance/willr.sqlite'

# Flask environment
export FLASK_ENV='development'  # or 'production'
```

### Custom Configuration

Edit `willr/__init__.py` to customize:

```python
app.config.from_mapping(
    SECRET_KEY='dev',  # Change in production!
    DATABASE=os.path.join(app.instance_path, 'willr.sqlite'),
)
```

---

## Database Schema

### Users Table
```sql
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);
```

### Posts Table
```sql
CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```

---

## Development

### Running Tests

```bash
# Install development dependencies
pip install -e .

# Run all tests
pytest

# Run with coverage
pytest --cov=willr

# Run specific test file
pytest tests/test_auth.py
```

### Code Style

Willr follows PEP 8 guidelines. Format your code using:

```bash
# Install black (optional)
pip install black

# Format code
black willr/
```

---

## Deployment

### Production Checklist

- [ ] Set a strong `SECRET_KEY`
- [ ] Use a production-ready database (PostgreSQL recommended)
- [ ] Set `FLASK_ENV='production'`
- [ ] Use a WSGI server (Gunicorn, uWSGI)
- [ ] Set up a reverse proxy (Nginx, Apache)
- [ ] Enable HTTPS
- [ ] Configure proper logging
- [ ] Set up database backups

### Example Production Setup

#### Using Gunicorn

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 'willr:create_app()'
```

#### Nginx Configuration

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        alias /path/to/willr/willr/static;
    }
}
```

---

## API Reference

While Willr is primarily a web application, understanding the route structure helps with customization:

### Authentication Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/auth/register` | GET, POST | User registration |
| `/auth/login` | GET, POST | User login |
| `/auth/logout` | POST | User logout |

### Blog Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | View all posts (index) |
| `/create` | GET, POST | Create new post |
| `/post/<id>/update` | GET, POST | Update existing post |
| `/post/<id>/delete` | POST | Delete post |

---

## Security Considerations

### Password Security
- Passwords are hashed using Werkzeug's security utilities
- Uses `pbkdf2:sha256` by default
- Never stores plain-text passwords

### Session Security
- Sessions are signed with `SECRET_KEY`
- Use a strong, random secret key in production
- Sessions expire on browser close by default

### Input Validation
- Form inputs are validated server-side
- SQL injection protection via parameterized queries
- XSS protection via Jinja2 auto-escaping

### Best Practices
- Always use HTTPS in production
- Regularly update dependencies
- Enable CSRF protection for production use
- Implement rate limiting for authentication endpoints

---

## Customization

### Adding New Features

#### 1. Create a New Blueprint
```python
# willr/feature.py
from flask import Blueprint

bp = Blueprint('feature', __name__, url_prefix='/feature')

@bp.route('/')
def index():
    return 'New feature'
```

#### 2. Register in Application Factory
```python
# willr/__init__.py
from . import feature
app.register_blueprint(feature.bp)
```

### Styling Customization

Edit `willr/static/style.css` to customize the appearance:

```css
/* Your custom styles */
:root {
    --primary-color: #2c3e50;
    --secondary-color: #34495e;
}

body {
    font-family: 'Your-Font', sans-serif;
}
```

---

## Troubleshooting

### Common Issues

#### Database Not Initialized
```
Error: sqlite3.OperationalError: no such table: user
```
**Solution:**
```bash
flask --app willr init-db
```

#### Secret Key Warning
```
Warning: Do not use the development server in a production environment.
```
**Solution:** Set a proper `SECRET_KEY` in production:
```bash
export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex())')
```

#### Import Errors
```
ModuleNotFoundError: No module named 'flask'
```
**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

#### Permission Denied on Instance Folder
**Solution:**
```bash
mkdir -p instance
chmod 755 instance
```

---

## Contributing

Contributions are welcome! Willr grows through the collective will of its users.

### How to Contribute

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make Your Changes**
   - Write clean, documented code
   - Add tests for new features
   - Follow existing code style
4. **Test Your Changes**
   ```bash
   pytest
   ```
5. **Commit Your Changes**
   ```bash
   git commit -m "Add: Brief description of your feature"
   ```
6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request**

### Contribution Guidelines

- Write clear commit messages
- Add tests for new functionality
- Update documentation as needed
- Follow PEP 8 style guidelines
- Be respectful and constructive

---

## Philosophy & Design Principles

### Minimalism
Willr embraces simplicity. No bloat, no unnecessary features. Only what matters: the ability to create and share your thoughts.

### Ownership
Your content belongs to you. Willr provides the platform, but your words, your ideas, your will — that's yours alone.

### Transparency
Open source means open knowledge. See how it works, modify it, make it yours. Assert your will over the tools you use.

### Power Through Creation
Every post is an act of creation. Every user is an author. Willr doesn't just host content — it empowers creators.

---

## Roadmap

### Planned Features
- [ ] Markdown support for posts
- [ ] User profiles with bio
- [ ] Post categories and tags
- [ ] Search functionality
- [ ] Comment system
- [ ] RSS feed generation
- [ ] Dark mode
- [ ] Post drafts
- [ ] Image uploads
- [ ] API endpoints for headless use

### Long-term Vision
- Plugin system for extensibility
- Multi-user blog support
- Advanced text editor
- Social sharing features
- Export/import functionality

---

## FAQ

### Why Willr?
Because creating should be simple, powerful, and intentional. Willr strips away complexity and gives you the tools to assert your voice.

### Is Willr suitable for production?
Yes, with proper configuration. Follow the production checklist and security best practices.

### Can I use a different database?
Yes! Willr works with any SQLAlchemy-supported database. Update the `DATABASE` configuration.

### How do I migrate my data?
Export your SQLite database, configure your new database in `config.py`, and import your data using SQLAlchemy migrations.

### Is Willr mobile-friendly?
Yes! The Bootstrap-based templates are responsive and work on all devices.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

---

## Acknowledgments

Willr stands on the shoulders of giants:
- **Flask** - The microframework that makes it all possible
- **Friedrich Nietzsche** - For the philosophy and inspiration
- **The Open Source Community** - For building tools that empower creators

---

## Contact & Support

### Get Help
- 📚 [Documentation](https://github.com/yourusername/willr/wiki)
- 🐛 [Issue Tracker](https://github.com/yourusername/willr/issues)
- 💬 [Discussions](https://github.com/yourusername/willr/discussions)

### Stay Connected
- ⭐ Star this repo if Willr helps manifest your will
- 🔄 Watch for updates and new features
- 🤝 Contribute and join the community

---

## Final Words

*"The individual has always had to struggle to keep from being overwhelmed by the tribe. If you try it, you will be lonely often, and sometimes frightened. But no price is too high to pay for the privilege of owning yourself."* — Friedrich Nietzsche

Willr is your tool. Your platform. Your assertion.

**Now go create.**

---

**Built with Will. Powered by Python. Inspired by Nietzsche.**
