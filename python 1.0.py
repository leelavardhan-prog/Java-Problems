import random
import time
import json
import os

# ================= DATABASE =================
DB_FILE = "quiz_db.json"

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({"users": []}, f)

def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ================= REAL GK QUESTIONS =================
real_questions = [
    {"q": "Capital of India?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "ans": "Delhi"},
    {"q": "Largest planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "ans": "Jupiter"},
    {"q": "Father of Computer?", "options": ["Newton", "Einstein", "Babbage", "Tesla"], "ans": "Babbage"},
    {"q": "Fastest land animal?", "options": ["Lion", "Tiger", "Cheetah", "Horse"], "ans": "Cheetah"},
    {"q": "National bird of India?", "options": ["Parrot", "Peacock", "Crow", "Eagle"], "ans": "Peacock"}
]

# ================= AUTO GENERATE 3000 QUESTIONS =================
generated_questions = []

for i in range(1, 3001):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    correct = a + b

    options = [correct, correct+1, correct-1, correct+2]
    random.shuffle(options)

    generated_questions.append({
        "q": f"What is {a} + {b} ?",
        "options": options,
        "ans": correct
    })

# Combine all questions
quiz = real_questions + generated_questions

# ================= LOGIN =================
username = input("Enter your name: ")

db = read_db()
user = next((u for u in db["users"] if u["username"] == username), None)

if not user:
    user = {"username": username, "scores": []}
    db["users"].append(user)
    write_db(db)

print(f"\nWelcome {username} 🎉")
print("Quiz starting...\n")

# ================= QUIZ =================
score = 0
num_questions = 10   # random 10 questions each run

questions = random.sample(quiz, num_questions)

for i, q in enumerate(questions, 1):
    print(f"\nQ{i}: {q['q']}")

    for idx, opt in enumerate(q["options"], 1):
        print(f"{idx}. {opt}")

    start = time.time()
    answer = input("Enter option (1-4): ")
    end = time.time()

    # ⏰ Timer check (30 sec)
    if end - start > 30:
        print("⏰ Time Up!")
        print("Correct Answer:", q["ans"])
        continue

    try:
        answer = int(answer)
        selected = q["options"][answer-1]

        if selected == q["ans"]:
            print("✅ Correct")
            score += 1
        else:
            print("❌ Incorrect")
            print("Correct Answer:", q["ans"])

    except:
        print("Invalid input")
        print("Correct Answer:", q["ans"])

# ================= SAVE SCORE =================
for u in db["users"]:
    if u["username"] == username:
        u["scores"].append(score)

write_db(db)

print("\n🎉 Quiz Finished!")
print(f"Score: {score}/{num_questions}")