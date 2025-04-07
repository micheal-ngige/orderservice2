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
- SMS notifications sent using Africa's Talking API.Use counrty code when placing an order like +2547...

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
DB_NAME='your db name'
DB_USER='your db username'
DB_PASSWORD='your db password'
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY= 'django _secret'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

AFRICASTALKING_API_KEY=your-africas-talking-api-key

AFRICASTALKING_USERNAME=sandbox

GOOGLE_CLIENT_ID='google client ID'
GOOGLE_CLIENT_SECRET='google client secret'




```

### **5. Apply Database Migrations**
```bash
python3 manage.py migrate
```

### **6. Create a Superuser**
```bash
python3 manage.py createsuperuser
```
CI/CD Setup with GitHub Actions
This project uses GitHub Actions for Continuous Integration and Deployment (CI/CD).

📂 Workflow File
Located at: .github/workflows/deploy.yml

✅ What It Does
Runs on: Pushes to the master branch.

🔧 Jobs:
Test Job

🧾 Checks out code.

🐍 Sets up Python 3.10.

📦 Installs dependencies from backend/requirements.txt.

🔄 Runs Django migrations.

✅ Executes Django unit tests.

📊 Measures code coverage.

❌ Fails the workflow if test coverage is below 80%.

Deploy Job

🔗 Depends on successful completion of the test job.

🚀 Triggers deployment via a Render deploy hook.




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

