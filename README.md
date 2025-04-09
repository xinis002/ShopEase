# 🛍️ ShopEase
ShopEase is a Django-based admin dashboard for managing product catalogs and store content.
It provides functionality for adding, editing, and organizing products, categories, users, and images.
The project is ideal for building the backend of an e-commerce or inventory system.

## 🚀 Features
> - 🗂️ Manage product listings with detailed fields
>   
> - 🧭 Organize products by categories
>   
> - 🖼️ Upload and manage product images
>   
> - 👤 Admin interface for user management
>   
> - 🔒 Built-in Django authentication system


## 📁 Project Structure
```bash
ShopEase/
├── manage.py                  # Django project manager
├── db.sqlite3                 # Default SQLite database
├── media/                     # Uploaded media files
├── static/                    # Static files 
├── products/                  # Main app for products and categories
│   ├── models.py              # Product, Category, and Image models
│   ├── admin.py               # Admin panel customizations
│   └── ...
├── users/                     # Custom user model and admin integration
├── shopproject/               # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── README.md                  # Project documentation
```

## ⚙️ Installation
### 💻 Local Development

#### 1. Clone the Repository:
```bash
git clone https://github.com/xinis002/ShopEase.git
```

#### 2. Navigate to the Project Directory:
```bash
cd ShopEase
```

#### 3. Create and Activate a Virtual Environment:
##### Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
##### Windows
```bash
python3 -m venv venv
venv\Scripts\activate
```

#### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 5. Apply Migrations and Create Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

#### 6. Run the Development Server
```bash
python manage.py runserver
```

## 🧪 Testing
```bash
python manage.py test
```

## 🤝 Contributing
> Contributions are welcome! 
> Please fork the repository and submit a pull request with your changes.
> 1. Fork the repository
> 2. Create a new branch ```git checkout -b feature-name```
> 3. Commit your changes
> 4. Push to your fork
> 5. Open a pull request


## 📝 License
This project is open-source and available under the MIT License.
















