# My Portfolio

A professional, responsive portfolio website built with **Django** and **Bootstrap 5**. This project serves as a central hub to showcase my skills, software development projects, and blog, while providing a way for visitors to get in touch.

## 🚀 Features

*   **Project Showcase**: Detailed project pages with galleries, technology tags, and links to live demos/GitHub.
*   **Blog System**: A fully functional blog to share thoughts and tutorials.
*   **Dynamic Resume**: Sections for Skills, Experience, and Education manageable via the Django Admin.
*   **Contact System**: Integrated contact form that handles user inquiries.
*   **Responsive Design**: Built with Bootstrap 5 to look great on mobile, tablet, and desktop.
*   **SEO Friendly**: structured HTML5 and semantic tags.

## 🛠️ Tech Stack

*   **Backend**: Python, Django
*   **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
*   **Database**: SQLite (Development), PostgreSQL (Production ready)
*   **Utilities**: Pillow (Image processing)

## 📦 Installation

Follow these steps to set up the project locally:

1.  **Clone the repository**
    ```bash
    git clone https://github.com/BinYusuf078/My-Portfolio.git
    cd My-Portfolio
    ```

2.  **Create a virtual environment**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations**
    Navigate to the project directory (where `manage.py` is located):
    ```bash
    cd projects/Portfolio
    python manage.py migrate
    ```

5.  **Create a superuser (for Admin access)**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server**
    ```bash
    python manage.py runserver
    ```

    Open your browser and visit `http://127.0.0.1:8000`.

## 📂 Project Structure

```
My-Portfolio/
├── projects/
│   └── Portfolio/
│       ├── blog/           # Blog application
│       ├── contacts/       # Contact form functionality
│       ├── in_portfolio/   # Core portfolio management (projects, skills)
│       ├── pages/          # Static pages (Home, About)
│       ├── templates/      # Base HTML templates
│       ├── static/         # CSS, JS, and Images
│       └── manage.py       # Django entry point
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
