import random
import datetime
import json

# Study content database
study_content = {
    "math": {
        "tips": ["Practice daily", "Break down complex problems", "Check your work", "Visualize with diagrams"],
        "questions": [
            {"q": "Solve: 2x + 5 = 15", "a": "5", "points": 10},
            {"q": "What is 7 x 8?", "a": "56", "points": 5},
            {"q": "What is 144 ÷ 12?", "a": "12", "points": 5},
            {"q": "Solve: 3(x - 4) = 18", "a": "10", "points": 15},
            {"q": "What is 15² (squared)?", "a": "225", "points": 20}
        ]
    },
    "science": {
        "tips": ["Create flashcards", "Watch educational videos", "Do experiments", "Connect to real life"],
        "questions": [
            {"q": "What planet is closest to the Sun?", "a": "mercury", "points": 5},
            {"q": "What is H2O?", "a": "water", "points": 5},
            {"q": "What is the powerhouse of the cell?", "a": "mitochondria", "points": 10},
            {"q": "What gas do plants absorb?", "a": "carbon dioxide", "points": 10},
            {"q": "What is the atomic number of carbon?", "a": "6", "points": 20}
        ]
    },
    "english": {
        "tips": ["Read daily", "Keep vocabulary journal", "Practice writing", "Look for themes"],
        "questions": [
            {"q": "What describes a noun?", "a": "adjective", "points": 5},
            {"q": "What is past tense of 'run'?", "a": "ran", "points": 5},
            {"q": "What compares using 'like' or 'as'?", "a": "simile", "points": 10},
            {"q": "What is the main character called?", "a": "protagonist", "points": 15},
            {"q": "What is a 14-line poem?", "a": "sonnet", "points": 20}
        ]
    },
    "history": {
        "tips": ["Create timelines", "Connect past to present", "Use mnemonics", "Study cause and effect"],
        "questions": [
            {"q": "First US President?", "a": "george washington", "points": 5},
            {"q": "Year WWII ended?", "a": "1945", "points": 5},
            {"q": "Who built the pyramids?", "a": "egyptians", "points": 10},
            {"q": "Year of US independence?", "a": "1776", "points": 10},
            {"q": "What empire did Julius Caesar rule?", "a": "roman empire", "points": 20}
        ]
    }
}

# AI Student Profile with Advanced Tracking
class StudentProfile:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.total_points = 0
        self.streak_days = 0
        self.last_study_date = None
        self.badges = []
        self.weak_subjects = {}
        self.strong_subjects = {}
        self.study_history = []
        self.achievements = {
            "first_quiz": False,
            "perfect_score": False,
            "week_streak": False,
            "master_learner": False,
            "subject_expert": False
        }
    
    def add_xp(self, points):
        """Add experience points and level up"""
        self.xp += points
        self.total_points += points
        old_level = self.level
        self.level = (self.xp // 100) + 1
        if self.level > old_level:
            return True  # Level up!
        return False
    
    def update_streak(self):
        """Update study streak"""
        today = datetime.date.today()
        if self.last_study_date:
            days_diff = (today - self.last_study_date).days
            if days_diff == 1:
                self.streak_days += 1
            elif days_diff > 1:
                self.streak_days = 1
        else:
            self.streak_days = 1
        self.last_study_date = today
        
        if self.streak_days >= 7 and not self.achievements["week_streak"]:
            self.achievements["week_streak"] = True
            self.badges.append("🔥 Week Warrior")
    
    def analyze_performance(self, subject, score):
        """Analyze and track subject performance"""
        if subject not in self.weak_subjects:
            self.weak_subjects[subject] = []
            self.strong_subjects[subject] = []
        
        if score < 60:
            self.weak_subjects[subject].append(score)
        elif score >= 80:
            self.strong_subjects[subject].append(score)
        
        # Check for subject mastery
        if len(self.strong_subjects.get(subject, [])) >= 5:
            if not self.achievements["subject_expert"]:
                self.achievements["subject_expert"] = True
                self.badges.append(f"🏆 {subject.capitalize()} Expert")

# Global student profile
student = None

def create_or_load_profile():
    """Create new profile or load existing one"""
    global student
    print("=" * 60)
    print("🎓 AI STUDY BUDDY - ADVANCED LEARNING SYSTEM 🎓")
    print("=" * 60)
    
    choice = input("\n1. Create New Profile\n2. Load Existing Profile\nChoice: ")
    
    if choice == "2":
        try:
            with open("profile.json", "r") as f:
                data = json.load(f)
                student = StudentProfile(data["name"])
                student.__dict__.update(data)
                print(f"\n✅ Welcome back, {student.name}!")
                print(f"Level: {student.level} | XP: {student.xp} | Streak: {student.streak_days} days 🔥")
                return
        except:
            print("⚠️ No profile found. Creating new one...")
    
    name = input("\nEnter your name: ")
    student = StudentProfile(name)
    print(f"\n🎉 Welcome, {name}! Let's start your learning journey!")

def save_profile():
    """Save student profile to file"""
    try:
        with open("profile.json", "w") as f:
            json.dump(student.__dict__, f, default=str)
        print("💾 Profile saved!")
    except:
        print("⚠️ Could not save profile (file operations may be limited)")

def display_dashboard():
    """Show student dashboard with stats"""
    print("\n" + "=" * 60)
    print(f"📊 {student.name.upper()}'S DASHBOARD")
    print("=" * 60)
    print(f"Level: {student.level} ⭐ | XP: {student.xp}/{(student.level) * 100}")
    print(f"Total Points: {student.total_points} 💰")
    print(f"Study Streak: {student.streak_days} days 🔥")
    print(f"Badges Earned: {len(student.badges)} 🏅")
    
    # XP Progress Bar
    xp_progress = (student.xp % 100) / 100
    bar_length = 30
    filled = int(bar_length * xp_progress)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\nXP Progress: [{bar}] {int(xp_progress * 100)}%")
    
    if student.badges:
        print(f"\n🏅 Badges: {', '.join(student.badges)}")
    
    print("=" * 60)

def ai_recommendations():
    """AI suggests what to study based on performance"""
    print("\n🤖 AI RECOMMENDATIONS:")
    print("-" * 60)
    
    if not student.weak_subjects:
        print("Take more quizzes so I can analyze your performance!")
        return
    
    # Find weakest subject
    weak_avg = {}
    for subject, scores in student.weak_subjects.items():
        if scores:
            weak_avg[subject] = sum(scores) / len(scores)
    
    if weak_avg:
        weakest = min(weak_avg, key=weak_avg.get)
        print(f"📌 Focus on: {weakest.upper()}")
        print(f"   Your average: {weak_avg[weakest]:.1f}%")
        print(f"   Recommendation: Review basics and practice more")
    
    # Find strongest subject
    strong_avg = {}
    for subject, scores in student.strong_subjects.items():
        if scores:
            strong_avg[subject] = sum(scores) / len(scores)
    
    if strong_avg:
        strongest = max(strong_avg, key=strong_avg.get)
        print(f"\n⭐ You're excelling at: {strongest.upper()}")
        print(f"   Your average: {strong_avg[strongest]:.1f}%")
        print(f"   Keep up the great work!")

def adaptive_quiz(subject):
    """Adaptive quiz that adjusts difficulty"""
    print(f"\n🎯 ADAPTIVE QUIZ: {subject.upper()}")
    print("-" * 60)
    
    questions = study_content[subject]["questions"].copy()
    random.shuffle(questions)
    
    score = 0
    total_points = 0
    correct_streak = 0
    answers_log = []
    
    # Start with 3 questions, can earn bonus questions
    num_questions = 3
    
    for i, item in enumerate(questions[:num_questions], 1):
        print(f"\nQuestion {i} ({item['points']} points):")
        print(item['q'])
        
        # Hint system
        if correct_streak == 0 and i > 1:
            hint = input("Need a hint? (yes/no): ").lower()
            if hint == "yes" or hint == "y":
                print("💡 Hint: Check the study tips for this subject!")
        
        answer = input("Your answer: ").strip().lower()
        correct_answer = item['a'].lower()
        
        # Flexible answer checking
        is_correct = answer == correct_answer or answer in correct_answer
        
        if is_correct:
            points_earned = item['points']
            # Bonus for streak
            if correct_streak >= 2:
                bonus = 5
                points_earned += bonus
                print(f"✅ Correct! +{item['points']} points + {bonus} streak bonus!")
            else:
                print(f"✅ Correct! +{item['points']} points")
            
            score += points_earned
            correct_streak += 1
            answers_log.append({"q": item['q'], "correct": True, "points": points_earned})
            
            # Unlock bonus question on 3-streak
            if correct_streak == 3 and num_questions < len(questions):
                print("🎁 3-STREAK BONUS! You've unlocked a challenge question!")
                num_questions += 1
        else:
            print(f"❌ Not quite. The answer is: {item['a']}")
            correct_streak = 0
            answers_log.append({"q": item['q'], "correct": False, "points": 0})
        
        total_points += item['points']
    
    # Calculate percentage
    percentage = (score / total_points) * 100 if total_points > 0 else 0
    
    # Update student profile
    student.update_streak()
    leveled_up = student.add_xp(score)
    student.analyze_performance(subject, percentage)
    
    # Check for achievements
    if not student.achievements["first_quiz"]:
        student.achievements["first_quiz"] = True
        student.badges.append("🎓 First Steps")
    
    if percentage == 100 and not student.achievements["perfect_score"]:
        student.achievements["perfect_score"] = True
        student.badges.append("💯 Perfectionist")
    
    if student.total_points >= 500 and not student.achievements["master_learner"]:
        student.achievements["master_learner"] = True
        student.badges.append("🌟 Master Learner")
    
    # Save to history
    student.study_history.append({
        "date": str(datetime.datetime.now()),
        "subject": subject,
        "score": score,
        "percentage": percentage,
        "questions": len(answers_log)
    })
    
    # Display results
    print("\n" + "=" * 60)
    print("📊 QUIZ RESULTS")
    print("=" * 60)
    print(f"Points Earned: {score}/{total_points}")
    print(f"Percentage: {percentage:.1f}%")
    print(f"XP Gained: +{score}")
    
    if leveled_up:
        print(f"\n🎉 LEVEL UP! You're now Level {student.level}!")
    
    # Detailed feedback
    print("\n📈 Performance Analysis:")
    correct_count = sum(1 for a in answers_log if a["correct"])
    print(f"Correct Answers: {correct_count}/{len(answers_log)}")
    
    if percentage >= 90:
        print("🌟 Outstanding! You're mastering this subject!")
    elif percentage >= 70:
        print("👍 Great job! Keep practicing to reach mastery!")
    elif percentage >= 50:
        print("💪 Good effort! Review the material and try again!")
    else:
        print("🎯 Keep going! Focus on the basics and you'll improve!")
    
    return percentage

def study_timer():
    """Pomodoro-style study timer"""
    print("\n⏰ STUDY TIMER (Pomodoro Technique)")
    print("-" * 60)
    print("The Pomodoro Technique: Study for 25 min, break for 5 min")
    
    choice = input("\nStart a study session? (yes/no): ").lower()
    if choice != "yes" and choice != "y":
        return
    
    print("\n⏱️ 25-minute study session starting...")
    print("💡 Focus on one subject. No distractions!")
    print("\n(In a real app, this would count down 25 minutes)")
    print("For demo: Press Enter when you've finished studying")
    
    input()
    
    print("\n🎉 Great job! You completed a study session!")
    print("💪 Take a 5-minute break. You earned it!")
    
    student.add_xp(25)  # Bonus XP for completing study session
    print("+25 XP for focused studying!")

def flashcard_mode(subject):
    """Interactive flashcard study mode"""
    print(f"\n📇 FLASHCARD MODE: {subject.upper()}")
    print("-" * 60)
    print("Study tips for this subject:\n")
    
    tips = study_content[subject]["tips"]
    
    for i, tip in enumerate(tips, 1):
        print(f"Card {i}/{len(tips)}")
        print(f"💡 {tip}")
        input("\nPress Enter for next card...")
        print()
    
    print("✅ You've reviewed all flashcards!")
    student.add_xp(10)
    print("+10 XP for reviewing flashcards!")

def compare_with_peers():
    """Simulate peer comparison (gamification)"""
    print("\n👥 PEER COMPARISON")
    print("-" * 60)
    
    # Simulated peer data
    peers = [
        {"name": "Alex", "level": random.randint(1, 10), "points": random.randint(100, 800)},
        {"name": "Maria", "level": random.randint(1, 10), "points": random.randint(100, 800)},
        {"name": "James", "level": random.randint(1, 10), "points": random.randint(100, 800)},
        {"name": "Sophie", "level": random.randint(1, 10), "points": random.randint(100, 800)}
    ]
    
    # Add current student
    all_students = peers + [{"name": f"{student.name} (You)", "level": student.level, "points": student.total_points}]
    all_students.sort(key=lambda x: x["points"], reverse=True)
    
    print("🏆 LEADERBOARD:")
    for i, s in enumerate(all_students, 1):
        indicator = " ⭐" if "(You)" in s["name"] else ""
        print(f"{i}. {s['name']}{indicator} - Level {s['level']} - {s['points']} pts")
    
    your_rank = next(i for i, s in enumerate(all_students, 1) if "(You)" in s["name"])
    print(f"\n📍 You're ranked #{your_rank} out of {len(all_students)}!")

def study_goal_tracker():
    """Set and track study goals"""
    print("\n🎯 STUDY GOALS")
    print("-" * 60)
    
    print("Set a goal for this week:")
    print("1. Reach Level", student.level + 2)
    print("2. Study 5 different subjects")
    print("3. Maintain a 7-day streak")
    print("4. Earn 200 more points")
    
    goal = input("\nChoose a goal (1-4): ")
    
    goals = {
        "1": f"Reach Level {student.level + 2}",
        "2": "Study 5 different subjects",
        "3": "Maintain a 7-day streak",
        "4": "Earn 200 more points"
    }
    
    if goal in goals:
        print(f"\n✅ Goal set: {goals[goal]}")
        print("🔔 I'll remind you of your progress each session!")
        student.add_xp(5)
        print("+5 XP for setting a goal!")

def main_menu():
    """Enhanced main menu"""
    while True:
        print("\n" + "=" * 60)
        print("📚 MAIN MENU")
        print("=" * 60)
        print("1. 📊 View Dashboard")
        print("2. 🎯 Take Adaptive Quiz")
        print("3. 📇 Flashcard Mode")
        print("4. ⏰ Study Timer")
        print("5. 🤖 AI Recommendations")
        print("6. 👥 Compare with Peers")
        print("7. 🎯 Set Study Goals")
        print("8. 💾 Save & Exit")
        
        choice = input("\nEnter choice (1-8): ")
        
        if choice == "1":
            display_dashboard()
        
        elif choice == "2":
            print("\nChoose subject:")
            print("1. Math  2. Science  3. English  4. History")
            sub_choice = input("Choice (1-4): ")
            subjects = {"1": "math", "2": "science", "3": "english", "4": "history"}
            if sub_choice in subjects:
                adaptive_quiz(subjects[sub_choice])
            else:
                print("❌ Invalid choice")
        
        elif choice == "3":
            print("\nChoose subject:")
            print("1. Math  2. Science  3. English  4. History")
            sub_choice = input("Choice (1-4): ")
            subjects = {"1": "math", "2": "science", "3": "english", "4": "history"}
            if sub_choice in subjects:
                flashcard_mode(subjects[sub_choice])
            else:
                print("❌ Invalid choice")
        
        elif choice == "4":
            study_timer()
        
        elif choice == "5":
            ai_recommendations()
        
        elif choice == "6":
            compare_with_peers()
        
        elif choice == "7":
            study_goal_tracker()
        
        elif choice == "8":
            save_profile()
            print(f"\n👋 Great work today, {student.name}!")
            print(f"Final Stats: Level {student.level} | {student.total_points} Total Points")
            print("Keep up the amazing effort! See you next time! 🌟")
            break
        
        else:
            print("❌ Invalid choice. Try again!")

# Run the program
if __name__ == "__main__":
    create_or_load_profile()
    main_menu()