#  Blood Donation & Request System

A web-based platform built with **Flask**, **MySQL**, **HTML**, **CSS**, and **JavaScript** that allows users to donate blood, request blood, and explore upcoming donation events. This system helps bridge the gap between blood donors and recipients, while giving admins full control over requests and events.

---

##  Features

###  Users
-  **View Blood Storage:** See real-time blood availability from the blood bank.
-  **Request Blood:** Submit blood request forms for urgent needs.
-  **Donate Blood:** Fill out donation forms to contribute to the blood bank.
-  **View Events:** Explore upcoming blood donation events organized by various centers.

###  Admin Panel
-  **Approve/Reject Requests:** Admin can manage blood donation and request applications.
-  **Manage Events:** Admin has the authority to create, approve, or reject upcoming events.
-  **Control Blood Storage:** Update available blood stock in the blood bank.
-  **Manage Users and Submissions:** View user requests, donor forms, and control the system.

---

##  Tech Stack

| Technology | Purpose               |
|------------|------------------------|
| **Flask**  | Backend Web Framework |
| **MySQL**  | Database Management   |
| **HTML/CSS/JS** | Frontend UI         |
| **Jinja2** | Flask Templating      |

---

##  Website

https://p-tanjim.github.io/Blood-donation/

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/P-Tanjim/Blood-donation.git
cd Blood-donation

```
### 2. Set Up a Virtual Environment

```bash

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up MySQL Database

- Import the provided .sql file into your MySQL server.

- Update your config.py or wherever your DB credentials are stored:

  ```bash
  DB_HOST = 'localhost'
  DB_USER = 'root'
  DB_PASSWORD = 'yourpassword'
  DB_NAME = 'blood_donation'
  ```

### 5. Run the Flask App

```bash
python app.py

```

---

# Usage

- Open your browser and navigate to: http://localhost:5000

- You can:
  - Request or donate blood.
  - Check current blood bank status.
  - View events.
  - Admin login available at /admin to manage system data.

# Admin Credentials(Sample)
```bash
Username: admin
Password: admin
```

# License
This project is licensed under the MIT License.

# Contact
```bash
Developer: Tanjim
GitHub: @P-Tanjim
Email: moksedurtanjim2769@gmail.com
```
