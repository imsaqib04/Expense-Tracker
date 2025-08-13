# 💰 Expense Tracker

A simple and intuitive **Django-based web application** to record, categorize, and analyze your expenses.  
Track your spending habits, view category-wise summaries, and get visual insights with charts.

---

## 🚀 Features

- ➕ **Add Expenses** – Record new expenses with name, amount, category, and date.  
- 🗂 **Categorization** – Organize expenses into categories (Food, Tech, Shopping, etc.).  
- 📋 **Expense List** – View all transactions in a neat table.  
- 📊 **Categorical Summary** – See total spending for each category.  
- 📈 **Interactive Charts** – Visualize expenses with a pie chart & summary cards.  
- ✏ **Edit & Delete** – Update or remove expenses easily:  
  - **Edit:** `/edit/<id>`  
  - **Delete:** `/delete/<id>`  

---

## 🛠 Technologies

- **Backend:** Django  
- **Database:** SQLite3  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 4, Chart.js  

---

## 📂 Project Structure

```plaintext
expense-tracker/
│
├── expense_tracker/         # Main project settings
│   ├── settings.py
│   ├── urls.py
│
├── expense_app/             # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/expense_app/
│
├── manage.py
└── requirements.txt
````

---

## 🖥 Getting Started

1️⃣ **Clone the repository**

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

4️⃣ **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

5️⃣ **Run development server**

```bash
python manage.py runserver
```

📌 Open `http://127.0.0.1:8000/` in your browser.
📌 Admin panel: `http://127.0.0.1:8000/admin/`

---

## 📸 Screenshots
<img width="1919" height="942" alt="image" src="https://github.com/user-attachments/assets/0d13092c-319a-4276-9ad8-0e0237956e53" />


### 🏠 Expense List

<img width="1913" height="701" alt="image" src="https://github.com/user-attachments/assets/f1375934-089d-467c-99a1-d3f7948ac844" />

---

### 📊 Expense Summary

* Total expenses for last **365 / 30 / 7 days**
* **Past 30 days** date-wise breakdown
* Category-wise spending summary
<img width="1880" height="956" alt="image" src="https://github.com/user-attachments/assets/fe85f58b-aec9-4c3d-b840-f49956e3350c" />

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify it.

---
