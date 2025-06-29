# 🧠 CSV AI Agent

This project is a simple AI-powered agent that takes natural language questions (like _"What is the revenue for store A in March?"_) and finds answers from a local CSV file using OpenAI’s GPT models.

It uses:
- OpenAI API for language understanding
- `pandas` for CSV processing
- `python-dotenv` to load environment variables

---

## 📁 Project Structure

```
aiagent/
├── aiagent.py            # Main script
├── sales.csv             # Example CSV file
├── .env                  # Your API key (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔧 Requirements

- Python 3.8+
- OpenAI account & API key

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/eugeneade/csv-ai-agent.git
cd csv-ai-agent
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Create a file called `.env` and add:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 📊 Example CSV (`sales.csv`)

```csv
store,month,revenue
A,January,10000
A,March,15000
B,March,18000
C,February,12000
```

---

## 🚀 Run the Agent

```bash
python aiagent.py
```

**Example Input:**

```
What is the revenue for store A in March?
```

**Output:**

```
The revenue for store A in March is $15000.
```

---

## 📌 Dependencies

See `requirements.txt`:

```
openai>=1.0.0,<2.0.0
pandas>=2.0.0,<3.0.0
python-dotenv>=1.0.0,<2.0.0
```
---

## 📄 License

MIT License – free to use and modify

---

Made with 💡 by Eugene
