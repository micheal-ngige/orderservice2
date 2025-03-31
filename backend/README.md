# Order Service API

This is a Django REST Framework-based API for managing customers and orders.

## 🌍 Live URLs
1. **Login:** [Order Service Login](https://orderservice2.onrender.com)
2. **Create Customer:** [Customers API](https://orderservice2.onrender.com/customers/)
3. **Create Order:** [Orders API](https://orderservice2.onrender.com/orders/)

---

## 🚀 Features
- User authentication using Google Auth0.
- Secure API endpoints using JWT authentication.
- Customers can be created and orders placed.
- SMS notifications sent using Africa's Talking API.

---

## 🛠 Setup Instructions

### **1. Clone the Repository**
```bash
git clone <your-github-repo-url>
cd <your-project-folder>
```

### **2. Create and Activate a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Create a .env File**
Create a `.env` file in your project's root directory and add the following:
```env
SECRET_KEY='your-django-secret-key'
DEBUG=True

AUTH0_DOMAIN='your-auth0-domain'
AUTH0_CLIENT_ID='your-auth0-client-id'
AUTH0_CLIENT_SECRET='your-auth0-client-secret'
AUTH0_ALGORITHM='RS256'

AFRICASTALKING_API_KEY='your-africas-talking-api-key'
AFRICASTALKING_USERNAME='sandbox'
```

### **5. Apply Database Migrations**
```bash
python3 manage.py migrate
```

### **6. Create a Superuser**
```bash
python3 manage.py createsuperuser
```

### **7. Run the Development Server**
```bash
python3 manage.py runserver
```
The API will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 📜 API Endpoints

 1 `/accounts/login/` | POST| User login                 |
 2 `/customers/` | GET, POST | Create and view customers  
 3 `/orders/`  | GET, POST | Create and view orders     |





## 🤝 Contributing
Feel free to fork the repository, make changes, and submit a pull request.

