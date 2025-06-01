
---

````markdown
# 🧠 SQL QnA App with LangChain, Groq & Streamlit

This project is an intelligent **SQL Question Answering App** built using:

- [LangChain](https://www.langchain.com/)
- [Groq API](https://console.groq.com/)
- [LLama3-8B](https://groq.com/)
- [Streamlit](https://streamlit.io/)
- [MySQL](https://www.mysql.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [dotenv](https://pypi.org/project/python-dotenv/)

It allows users to input natural language questions and receive accurate answers based on data from a **MySQL database**. The app uses an LLM to generate SQL queries and interprets the results using prompt engineering.

---

## 📦 Features

- 🔐 Uses `dotenv` for secure API key handling
- 🧠 Translates natural questions into SQL queries
- 📊 Executes the query against a MySQL database
- 🗣️ Converts SQL results into human-readable answers
- 🌐 Easy to use with a Streamlit UI

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sql-qna-app.git
cd sql-qna-app
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up `.env` file

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🧪 Running the App

Make sure MySQL is running and the database `x` with table `employees` is accessible.

Then start the Streamlit app:

```bash
streamlit run app.py
```

---

## 🧱 Database Setup Example

If you don’t have a database yet, create one:

```sql
CREATE DATABASE x;

USE x;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(50),
    salary INT
);

INSERT INTO employees VALUES
(1, 'Alice', 'Data Scientist', 120000),
(2, 'Bob', 'Software Engineer', 110000),
(3, 'Charlie', 'Product Manager', 105000);
```

---

## 🧾 Example Questions

* "How many employees are there?"
* "What is the average salary of employees?"
* "List all employees with their roles."

---

## 📁 Project Structure

```
.
├── app.py              # Main application
├── .env                # API keys (not tracked)
├── .gitignore          # Ignores venv and .env
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ✅ Requirements

* Python 3.8+
* MySQL Server
* [Groq API Key](https://console.groq.com/)

---

## 🔒 .gitignore

Make sure you have a `.gitignore` like this:

```gitignore
venv/
.env
__pycache__/
*.pyc
```

---

## 📜 License

MIT License. Feel free to use, modify, and distribute.

---

## 🙋‍♂️ Support

If you run into issues, feel free to open an issue or reach out.

---

```

---

