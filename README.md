# 🔐 PassGuardian: Smart Password Evaluator

PassGuardian is a smart, terminal-based password strength evaluator that helps you create and test strong, secure passwords in real time. It combines entropy analysis, breach detection, actionable feedback, and an optional password generator — all with a colorful, polished CLI experience.

---

![PassGuardian Demo](assets/terminal-demo.png) <!-- Replace or remove if needed -->

## 🚀 Features

- 🧠 **Entropy-based Strength Scoring**
- 🔥 **Real-time Breach Check** via HaveIBeenPwned API
- 💡 **Smart Feedback** with improvement tips
- 🔁 **Interactive Password Generator**
- 🎨 **Colorful CLI UI** powered by `rich`
- 🔐 Built with **Security Best Practices**

---

## 🛠 Tech Stack

- Python 3
- `rich` (for colorful CLI output)
- `requests` (for HIBP breach API)
- Regex & logic-based password scoring
- Optional: HIBP Pwned Passwords API

---

## ⚙️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/nv2105/PassGuardian.git
cd PassGuardian
```
### 2. Set Up Virtual Environment
```bash
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# Or: source .venv/bin/activate  # On Mac/Linux
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the CLI App
```bash
python main.py
```
### 📸 Sample Output
```sql
🧠 Estimated Entropy: 83.36 bits
✅ No known breaches found for this password.

╭──────────── Result ────────────╮
│ 🔒 Password Strength: Strong!  │
╰───────────────────────────────╯

💡 Tips to Improve:
- Add at least one special character
- Avoid common patterns like '123', 'password'
```

### 📂 Project Structure
```css
PassGuardian/
├── passguardian/
│   ├── evaluator.py
│   ├── breaches.py
│   ├── entropy.py
│   ├── generator.py
│   └── __init__.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```
# 📌 Author
## Naman Vora
### Final Year CSE | Aspiring Data Analyst
### [Github ](https://github.com/nv2105) | [LinkedIn](www.linkedin.com/in/namanvora21)

### 📄 License
[MIT License](https://mit-license.org)


