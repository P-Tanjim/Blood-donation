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

##  Image

### User

## Blood Availability
> Users can view the currently available blood groups.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/a6cd2240-3009-4d89-b7d2-d7f3a88230ab" />

## Blood Donation Request
> Users can request to donate blood.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/73062049-05e7-4839-9316-3673ec60ef7d" />

## Blood Request
> Users can request blood if needed.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/a5d33247-3b89-48e2-bb05-e21ed9b13356" />

## Events
> Everyone can view and add blood donation events.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/fbc0f35a-e68d-4a88-b07f-be2b350cadbf" />

## Donation Form
> Form to register a blood donation.
<img width="1920" height="1288" alt="screencapture-localhost-5000-donate-blood-2025-07-20-07_16_44" src="https://github.com/user-attachments/assets/21d8b197-36ea-4a81-874c-b5d8ac2ef826" />

## Blood Request Form
> Form to request blood in emergencies.
<img width="1920" height="1239" alt="screencapture-localhost-5000-request-blood-2025-07-20-07_15_16" src="https://github.com/user-attachments/assets/24db0127-bb6b-4f3c-afe8-6681d39a273f" />

### Admin Features

## Admin Dashboard
> Full admin access to blood data and requests.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/96b6ee6c-b743-464a-81c4-dd22e3477c00" />

## Manage Donation Requests
> Admin can view and approve or reject donation requests.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/298891fd-6671-4228-8abe-767e7a258536" />

## Manage Blood Requests
> Admin can monitor and manage blood requests.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/d8b44e0f-cb8e-47b2-8db2-bfdda0d17bdc" />

## Manage Event Requests
> Admin can add and manage event requests.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/7d6f5708-b9cc-4d10-9128-d9e9c99f0377" />


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
