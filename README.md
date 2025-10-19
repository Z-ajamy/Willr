# Willr

## *"A Blog for the Free Will"*

---

## 🔥 About the Project

**Willr** is a full-stack blog web application built with the Flask framework. This project was developed as an advanced, practical application of the official Flask tutorial, focusing on building an app from scratch using the "Application Factory" pattern.

The application allows users to register, log in, create their own blog posts, and edit or delete them.

Willr goes beyond being a simple tutorial project by featuring a completely custom-built frontend. The unique UI is inspired by Nietzschean philosophy, using a strong and bold color palette based on **blood red** (`#990000`) to reflect the project's spirit of "will" and "power". This is not a standard, calm design—it is bold and sharp, embodying the philosophy of the *Will to Power*.

---

## ✨ Key Features

### Authentication & Security
- **Full Authentication System**: Complete user registration, login, and logout functionality
- **Secure Password Storage**: All passwords are hashed using industry-standard algorithms
- **SQL Injection Protection**: Parameterized queries protect against malicious attacks
- **Cryptographically-Signed Sessions**: Session data is securely signed to prevent tampering

### Post Management (CRUD Operations)
- **Create**: Compose new blog posts (requires authentication)
- **Read**: Browse all published posts on the public index page
- **Update**: Edit your existing posts (author-only access)
- **Delete**: Remove your posts permanently (author-only access)

### Design Philosophy
- **Custom UI**: Unique interface built from scratch with custom CSS
- **Bold Aesthetic**: Blood red primary color (`#990000`) reflecting Nietzschean themes
- **Project Logo**: Custom branding that embodies the spirit of free will

### Architecture
- **Secure Association**: Every post is cryptographically tied to its creator
- **Application Factory Pattern**: Scalable and maintainable code structure
- **Blueprint-Based Organization**: Modular routing and view management

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Flask |
| **Database** | SQLite (file-based, serverless) |
| **Frontend** | Jinja2 (templating), HTML5, CSS3 |
| **Environment** | Python Virtual Environment (venv) |

---

## 📦 Installation & Setup

Follow these steps to run Willr locally on your development machine:

### 1. Clone the Repository

```bash
git clone [Your-Repo-URL-Here]
cd Willr
```

### 2. Create and Activate Virtual Environment

```bash
# Create the environment
python -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows
# .\venv\Scripts\activate
```

### 3. Install Dependencies

This command reads `requirements.txt` and installs Flask, Jinja2, and all other dependencies:

```bash
pip install -r requirements.txt
```

### 4. Install the Project in Editable Mode

This installs Willr as an editable package in your environment:

```bash
pip install -e .
```

---

## 🚀 Usage

After installation, follow these steps to launch the application:

### Initialize the Database (First-time only)

This command creates the `willr.sqlite` file and sets up all necessary tables:

```bash
flask --app willr init-db
```

You should see a confirmation message: `Initialized the database.`

### Run the Development Server

Start the Flask development server with debug mode enabled:

```bash
flask --app willr run --debug
```

### Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

You can now register a new account, log in, and start creating posts!

---

## 📂 Project Structure

```
Willr/
├── willr/              # Main application package
│   ├── __init__.py     # Application factory
│   ├── auth.py         # Authentication blueprint
│   ├── blog.py         # Blog blueprint
│   ├── db.py           # Database initialization
│   ├── schema.sql      # Database schema
│   ├── static/         # Static files (CSS, images, logo)
│   └── templates/      # Jinja2 templates
├── instance/           # Instance-specific files (database)
├── venv/               # Virtual environment (not in repo)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🎨 Design Philosophy

Willr's design is a deliberate departure from conventional blog aesthetics. Inspired by Friedrich Nietzsche's concept of the *Will to Power*, the interface uses:

- **Blood Red (`#990000`)** as the primary accent color, symbolizing passion, power, and vitality
- **Bold typography** that commands attention
- **Sharp contrasts** that reflect the philosophical tensions between conformity and individual will
- **Minimalist brutalism** that prioritizes function and statement over decoration

This is not a blog for passive consumption—it's a platform for powerful self-expression.

---

## 🔒 Security Features

- **Password Hashing**: Uses Werkzeug's security utilities for secure password storage
- **CSRF Protection**: Forms are protected against Cross-Site Request Forgery
- **SQL Injection Prevention**: All database queries use parameterized statements
- **Session Security**: Flask's cryptographically-signed session cookies
- **Authorization Checks**: Users can only modify their own content

---

## 🤝 Contributing

Contributions are welcome! Whether you want to:
- Report a bug
- Suggest a feature
- Improve documentation
- Submit a pull request

Feel free to open an issue or submit a PR on the repository.

---

## 📄 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software as long as you include the original copyright notice.

---

## 🙏 Acknowledgments

- Built upon the foundation of the [official Flask tutorial](https://flask.palletsprojects.com/tutorial/)
- Inspired by Friedrich Nietzsche's philosophical works
- Created as a demonstration of full-stack web development principles

---

## 💪 Final Words

> *"He who has a why to live can bear almost any how."* — Friedrich Nietzsche

Willr is more than code—it's a statement. A digital space where will meets expression, where philosophy meets functionality. 

**Build. Express. Empower.**

---

*Made with 🔥 and philosophical intent*
