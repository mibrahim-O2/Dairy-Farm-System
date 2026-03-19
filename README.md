# 🐃 Bin Khalid Dairy Farm – Dairy Management System

[![Python](https://img.shields.io/badge/Python-3.x-blue)]()
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)]()
[![Status](https://img.shields.io/badge/Status-Live-success)]()
[![License](https://img.shields.io/badge/License-Personal%20Use-orange)]()

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Now-brightgreen)](https://mibrahim02.pythonanywhere.com/)
---

## Project Overview

**Bin Khalid Dairy Farm – Dairy Management System** is a **Flask-based web application** designed to help small dairy farms efficiently manage milk vouchers, billing, and customer records.  

This system provides a simple **login system**, a professional **billing interface** with bilingual support (English + Urdu), and monthly reports for milk collection and income.  

The project is deployed live on PythonAnywhere and can be accessed at: [https://mibrahim02.pythonanywhere.com/](https://mibrahim02.pythonanywhere.com/)

---
## Custom Logo  

The system includes a **custom-designed logo** created specifically for **Bin Khalid Dairy Farm**.  
The logo reflects the farm’s identity and is prominently displayed in the dashboard, bills, and other interfaces to give a professional and personalized touch:

![Custom Logo](https://github.com/mibrahim-O2/Dairy-Farm-System/blob/main/static/buffalo.png)
---

## Features

- **Secure Login System** – only authorized users can access the dashboard.  
- **Customer Management** – add, edit, and delete customer milk vouchers.  
- **Professional Bills** – bills are generated in **English & Urdu**, ready to print.  
- **Monthly Reports** – automatically calculates total milk collected and income per month.  
- **Online Payment Info** – includes Easypaisa and JazzCash details for easy payment.  
- **Search Functionality** – search for customer records quickly.  

---

## Technologies Used

- **Backend:** Python 3.x, Flask  
- **Database:** SQLite  
- **Frontend:** HTML5, CSS3 (with professional design for bilingual bills)  
- **Deployment:** PythonAnywhere  
- **Version Control:** Git + GitHub  

---
## Usage

1. **Login**:

   * Default credentials for demo purposes:

     ```
     Username: admin
     Password: 1234
     ```
---

![Login Screen](https://github.com/mibrahim-O2/Dairy-Farm-System/blob/main/login.png)
---
2. **Dashboard**:

   * View latest vouchers for all customers.
   * Search customers by name.
   * Add, edit, or delete vouchers.
---
**Main Dashboard**

![Dashboard](https://github.com/mibrahim-O2/Dairy-Farm-System/blob/main/Screenshot%202026-03-19%20030314.png)

---
3. **Generate Bill**:

   * Click **Print** to open professional bill in a new tab.
   * Bills include English and Urdu details, payment info, and totals.
---
**Add Voucher Screen**

![Add Voucher](https://github.com/mibrahim-O2/Dairy-Farm-System/blob/main/Screenshot%202026-03-19%20030421.png)
---
4. **Sample Bill**

![Bill Preview](https://github.com/mibrahim-O2/Dairy-Farm-System/blob/main/bill.png)
---
[📄 Download Full Bill (PDF)](https://raw.githubusercontent.com/mibrahim-O2/Dairy-Farm-System/main/Bill.pdf)

---
5. **Monthly Report**:

   * Shows total milk collected and total income for the current month.
---

## Installation

To run this project locally:

1. Clone the repository:

```bash
git clone https://github.com/mibrahim-O2/Dairy-Farm-System.git
cd Dairy-Farm-System
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Initialize the database:

```bash
python init_db.py
```

5. Run the app:

```bash
python app.py
```

6. Open your browser and visit:

```
http://127.0.0.1:5000
```

---
## Database Structure

**SQLite Database:** `database.db`

**Table: vouchers**

| Column     | Type    | Description               |
| ---------- | ------- | ------------------------- |
| id         | INTEGER | Primary key               |
| name       | TEXT    | Customer name             |
| date       | TEXT    | Voucher date (YYYY-MM-DD) |
| days       | INTEGER | Total days milk delivered |
| rate       | REAL    | Rate per KG               |
| daily      | REAL    | Daily milk collected      |
| extra      | REAL    | Extra milk                |
| used       | REAL    | Milk used by customer     |
| due        | REAL    | Previous due amount       |
| total_milk | REAL    | Calculated total milk     |
| amount     | REAL    | Calculated amount         |
| final_bill | REAL    | Total bill including dues |

---

##  Future Improvements

This project can be enhanced further with:

- 👥 Multi-user authentication system  
- 📱 Mobile responsive UI design  
- ☁️ Cloud database (PostgreSQL / MySQL)  
- 📊 Advanced analytics & charts  
- 🧾 PDF download instead of print-only bills  
- 🔔 SMS/WhatsApp payment reminders  
---

## 👨‍💻 About the Developer

This project was developed by a **Computer Science student** as a practical implementation of web development concepts.  

It is designed specifically for **real-world dairy farm management**, focusing on simplicity, efficiency, and usability.  
From backend logic to UI design, deployment, and even logo customization — everything was built as a complete end-to-end solution.

---

## 🤝 Contributing

This is a personal project, but contributions are welcome!

1. Fork the repository  
2. Create a branch: `git checkout -b feature-name`  
3. Make your changes  
4. Commit: `git commit -m "Add feature"`  
5. Push: `git push origin feature-name`  
6. Open a Pull Request  

---

## 💡 Final Note

This system reflects how **technology can simplify small business operations**.  
It’s a real example of turning a daily manual process into a **digital, efficient system**.

---

## 📜 License

This project is available for **personal and educational use**.  
You are free to use and modify it according to your needs.

---

⭐ If you like this project, don’t forget to **star the repository**!
 
