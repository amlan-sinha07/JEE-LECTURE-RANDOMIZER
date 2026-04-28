# 🎯 JEE Smart Lecture Randomizer

A Python-based CLI tool designed to **optimize daily study decisions** for JEE/WBJEE aspirants using **weighted randomness and progress tracking**.

---

## 🚀 Problem It Solves

Students often face:

* Decision fatigue (“What should I study next?”)
* Bias toward easy or favorite topics
* Poor tracking of completed lectures

This tool solves that by generating **smart, unbiased study targets** every day.

---

## 🧠 Key Features

* 🎲 **Weighted Random Selection**

  * Prioritizes weak or incomplete chapters
  * Reduces repetition of recently studied topics

* 📊 **Progress Tracking**

  * Tracks completed lectures per chapter
  * Displays subject-wise and overall progress

* 💾 **Persistent Storage**

  * Saves progress using JSON
  * Resume anytime without losing data

* 🧾 **Roll History**

  * Stores recent study targets
  * Helps track consistency

* ⚡ **CLI-Based Interface**

  * Fast, lightweight, and distraction-free

---

## 🛠️ Tech Stack

* Python
* JSON (for storage)
* CLI (Command Line Interface)

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🎮 Commands

| Command | Action               |
| ------- | -------------------- |
| `r`     | Roll new lectures    |
| `d`     | Mark lecture as done |
| `s`     | Show progress stats  |
| `h`     | Show history         |
| `reset` | Reset progress       |
| `q`     | Quit                 |

---

## 📌 Example Output

```
PHYSICS        CHEMISTRY        MATH
Lec 3/10       Lec 5/12         Lec 2/8
Rotational     Organic          Functions
```

---

## 🔥 Future Improvements

* GUI version (Tkinter / Web App)
* Adaptive difficulty system
* Streak tracking
* Smart scheduling (avoid recent repeats)

---

## 💡 Inspiration

Built to improve personal study efficiency and eliminate decision fatigue during JEE preparation.

---

## 👤 Author

Amlan Sinha
