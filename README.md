# Django Multi-Step Session Form 🚀

A clean, responsive, and industry-standard Django application that demonstrates how to capture user data across multiple pages using **Django Sessions**.

## ✨ Features
* **Multi-Step Workflow:** Segregates Name, Age, and Profession into logical steps.
* **Session Persistence:** Uses Django's built-in session framework to store data temporarily without immediate database hits.
* **Clean Logic:** Organized view functions for better readability and maintenance.
* **Responsive UI:** (Assuming you used Bootstrap) Optimized for both Desktop and Mobile devices.

## 🛠️ Tech Stack
* **Backend:** Python, Django
* **Frontend:** HTML5, Bootstrap 5
* **State Management:** Django Sessions

## 📂 Project Structure
```text
testapp/
├── views.py       # Core logic for handling session data
├── templates/
│   └── testapp/
│       ├── name.html    # Step 1: Name Input
│       ├── age.html     # Step 2: Age Input
│       ├── prof.html    # Step 3: Profession Input
│       └── result.html  # Step 4: Final Summary

---

## If you find these logic-building challenges helpful, feel free to ⭐ this repository!

---

## 🚀 How to Run Locally
1. Clone the repo:
git clone [https://github.com/your-username/repo-name.git](https://github.com/your-username/repo-name.git)

2. Install Django:
pip install django

3. Run Migrations (for sessions):
python manage.py migrate

4. Start the server:
python manage.py runserver

---
