#  🐃 Bin Khalid Dairy Farm – Dairy Management System

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

## Usage

1. **Login**:

   * Default credentials for demo purposes:

     ```
     Username: admin
     Password: 1234
     ```

2. **Dashboard**:

   * View latest vouchers for all customers.
   * Search customers by name.
   * Add, edit, or delete vouchers.

3. **Generate Bill**:

   * Click **Print** to open professional bill in a new tab.
   * Bills include English and Urdu details, payment info, and totals.

4. **Monthly Report**:

   * Shows total milk collected and total income for the current month.

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

## Screenshots

**Main Dashboard**
![Dashboard](https://github.com/mibrahim-O2/Dairy-Farm-System/blob/main/Screenshot%202026-03-19%20030314.png)

**Add Voucher Screen**
![Add Voucher](https://github.com/mibrahim-O2/Dairy-Farm-System/blob/main/Screenshot%202026-03-19%20030421.png)

**Sample Bill (PDF)**
[Download Bill](https://github.com/mibrahim-O2/Dairy-Farm-System/blob/main/Bill.pdf)

---

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make changes and commit: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature-name`
5. Create a pull request

---

## License

This project is **open source** and free to use for personal/business purposes.

```

---

This README will:

- Show your **logo** at the top  
- Embed **all your screenshots** so they render directly on GitHub  
- Include a **link to the live site** and the **PDF bill**  

---

If you want, I can also **enhance it with badges** like Python version, Flask, license, and last update to make it **look more professional** on GitHub.  

Do you want me to do that?
```
