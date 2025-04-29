import time
import random
import sys
from typing import List, Dict

class DebugQuest:
    def __init__(self):
        self.player_name = ""
        self.skills = {
            "Leadership": 0,
            "Problem Solving": 0,
            "Python": 0,
            "JavaScript": 0,
            "Debugging": 0,
            "Patience": 0
        }
        self.level = 1
        self.score = 0
        self.bugs_fixed = 0
        self.easter_eggs_found = 0
        
    def display_header(self):
        print(r"""
   ___      _       ____               _   
  / _ \  __| | ___ / ___|_ __ __ _ ___| |_ 
 | | | |/ _` |/ _ \ |  _| '__/ _` / __| __|
 | |_| | (_| |  __/ |_| | | | (_| \__ \ |_ 
  \___/ \__,_|\___|\____|_|  \__,_|___/\__|
   ___            _       _   _             
  / _ \___   ___ | |_ ___| |_(_) ___  ___   
 / /_)/ _ \ / _ \| __/ __| __| |/ _ \/ __|  
/ ___/ (_) | (_) | |_\__ \ |_| |  __/\__ \  
\/    \___/ \___/ \__|___/\__|_|\___||___/  
        """)
        print("="*55)
        print(" Welcome to Debug Quest: Terminal Adventure!")
        print(" Fix bugs, gain skills, and defeat CSS gremlins!")
        print("="*55 + "\n")

    def typewriter_effect(self, text: str, delay: float = 0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def animate_loading(self, seconds: int = 2):
        for i in range(seconds * 10):
            sys.stdout.write("\rLoading" + "." * (i % 4) + " " * 3)
            sys.stdout.flush()
            time.sleep(0.1)
        print("\r" + " " * 20 + "\r", end="")

    def get_player_name(self):
        self.typewriter_effect("\n(Wait... does that say 'OdeGrast Pootsties'?! Damn CSS gremlins messed up the title!)")
        self.typewriter_effect("\nBefore we begin, brave debugger...")
        self.player_name = input("What shall we call you? > ").strip()
        if not self.player_name:
            self.player_name = "Anonymous Coder"
        self.typewriter_effect(f"\nWelcome, {self.player_name}! Prepare for debugging adventures!")
        
    def show_status(self):
        print("\n" + "="*55)
        print(f" Debugger: {self.player_name}")
        print(f" Level: {self.level} | Score: {self.score} | Bugs Fixed: {self.bugs_fixed}")
        print("-"*55)
        print(" Skills:")
        for skill, level in self.skills.items():
            print(f"  {skill}: {'★' * level}{'☆' * (5 - level)}")
        print("="*55 + "\n")
        
    def level_up(self, skill: str):
        if self.skills[skill] < 5:
            self.skills[skill] += 1
            self.typewriter_effect(f"\n✨ Skill improved! {skill} is now level {self.skills[skill]}!")
            
        if sum(self.skills.values()) >= self.level * 8:
            self.level += 1
            self.typewriter_effect(f"\n🎉 LEVEL UP! You are now Level {self.level}!")
            self.typewriter_effect(" New debugging challenges await!")
            
    def random_easter_egg(self):
        eggs = [
            "You notice a tiny CSS gremlin hiding in the comments! +5 points!",
            "Wait... is that your CV in this code? You used Leadership skill!",
            "A wild Rubber Duck appears! It helps you debug! +10 points!",
            "You found the secret 'Hire Me' function! Recruiters love this!",
            "The code comments reveal a dad joke: Why do programmers confuse Halloween and Christmas? Because Oct 31 == Dec 25!",
            "You discover a hidden tribute to Stack Overflow! All hail the knowledge base!"
        ]
        if random.random() < 0.3:  # 30% chance of easter egg
            egg = random.choice(eggs)
            self.typewriter_effect("\n🐣 EASTER EGG: " + egg)
            self.score += random.randint(5, 15)
            self.easter_eggs_found += 1
            return True
        return False
        
    def present_python_challenge(self) -> bool:
        challenges = [
            {
                "buggy_code": "def add_numbers(a, b):\n    return a - b",
                "description": "The function doesn't add numbers correctly. The CSS gremlin must have messed with the operator!",
                "solution": "+",
                "hint": "Check the arithmetic operator",
                "skills": ["Python", "Debugging"]
            },
            {
                "buggy_code": "for i in range(5):\nprint(i)",
                "description": "This loop should print numbers 0-4, but it's throwing an IndentationError!",
                "solution": "    print(i)",
                "hint": "Python cares about whitespace",
                "skills": ["Python", "Problem Solving"]
            },
            {
                "buggy_code": "numbers = [1, 2, 3]\nnumbers.append(4)\nprint(numbers)",
                "description": "There's a SyntaxError in this code. Those pesky brackets!",
                "solution": "numbers.append(4",
                "hint": "Count the parentheses",
                "skills": ["Python", "Debugging"]
            },
            {
                "buggy_code": "def greet(name):\n    print('Hello, ' + name)\n\ngreet()",
                "description": "This greeting function isn't very welcoming - it's missing something!",
                "solution": "greet('your_name')",
                "hint": "The function needs an argument",
                "skills": ["Python", "Problem Solving"]
            },
            {
                "buggy_code": "x = 5\ny = '10'\nprint(x + y)",
                "description": "This code tries to add a number and a string - we need to fix the type mismatch!",
                "solution": "print(x + int(y))",
                "hint": "Type conversion might help",
                "skills": ["Python", "Debugging"]
            }
        ]
        
        challenge = random.choice(challenges)
        self.typewriter_effect(f"\n🚨 PYTHON BUG ALERT (Level {self.level}) 🚨")
        self.typewriter_effect(challenge["description"])
        print("\n" + challenge["buggy_code"] + "\n")
        
        attempts = 3
        while attempts > 0:
            answer = input("How would you fix this code? > ").strip()
            
            if answer.lower() == "hint":
                self.typewriter_effect(f"💡 Hint: {challenge['hint']}")
                continue
            elif answer.lower() == "exit":
                return False
            
            if answer in challenge["solution"] or challenge["solution"] in answer:
                self.typewriter_effect("\n✅ Success! Bug fixed!")
                self.score += self.level * 10
                self.bugs_fixed += 1
                
                for skill in challenge["skills"]:
                    self.level_up(skill)
                
                if self.random_easter_egg():
                    time.sleep(1)
                
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    self.typewriter_effect(f"\n❌ Not quite! {attempts} attempt(s) left. Try again or type 'hint' for help.")
                else:
                    self.typewriter_effect("\n😵 Out of attempts! The correct fix was: " + challenge["solution"])
                    self.skills["Patience"] = max(1, self.skills["Patience"])
                    return False
                
    def present_javascript_challenge(self) -> bool:
        challenges = [
            {
                "buggy_code": "function multiply(a, b) {\n  return a + b;\n}",
                "description": "This multiplication function isn't multiplying! The CSS gremlin strikes again!",
                "solution": "*",
                "hint": "Check the arithmetic operator",
                "skills": ["JavaScript", "Debugging"]
            },
            {
                "buggy_code": "let x = 5;\nconst y = 10;\nx = 20;\ny = 15;",
                "description": "This code throws an error when run. Something about constant variables...",
                "solution": "const y = 10;",
                "hint": "Can you change a const after declaring it?",
                "skills": ["JavaScript", "Problem Solving"]
            },
            {
                "buggy_code": "console.log('Hello, world!');",
                "description": "Wait... this code actually works! The CSS gremlin is playing tricks on you!",
                "solution": "none",
                "hint": "There's no actual bug here!",
                "skills": ["JavaScript", "Patience"]
            },
            {
                "buggy_code": "for (let i = 0; i < 5; i++)\nconsole.log(i);",
                "description": "This loop should log numbers 0-4, but it's missing something important!",
                "solution": "{}",
                "hint": "JavaScript needs these for loops",
                "skills": ["JavaScript", "Debugging"]
            },
            {
                "buggy_code": "let numbers = [1, 2, 3];\nnumbers.push(4);\nconsole.log(numbers);",
                "description": "There's a SyntaxError in this code. Those pesky brackets!",
                "solution": "numbers.push(4",
                "hint": "Count the parentheses",
                "skills": ["JavaScript", "Debugging"]
            }
        ]
        
        challenge = random.choice(challenges)
        self.typewriter_effect(f"\n🚨 JAVASCRIPT BUG ALERT (Level {self.level}) 🚨")
        self.typewriter_effect(challenge["description"])
        print("\n" + challenge["buggy_code"] + "\n")
        
        attempts = 3
        while attempts > 0:
            answer = input("How would you fix this code? > ").strip()
            
            if answer.lower() == "hint":
                self.typewriter_effect(f"💡 Hint: {challenge['hint']}")
                continue
            elif answer.lower() == "exit":
                return False
            
            if challenge["solution"] == "none" and answer.lower() in ["nothing", "no bug", "it's fine"]:
                self.typewriter_effect("\n✅ Correct! There was no bug! The CSS gremlin fooled you!")
                self.score += self.level * 15
                self.bugs_fixed += 1
                
                for skill in challenge["skills"]:
                    self.level_up(skill)
                
                if self.random_easter_egg():
                    time.sleep(1)
                
                return True
            elif answer in challenge["solution"] or challenge["solution"] in answer:
                self.typewriter_effect("\n✅ Success! Bug fixed!")
                self.score += self.level * 10
                self.bugs_fixed += 1
                
                for skill in challenge["skills"]:
                    self.level_up(skill)
                
                if self.random_easter_egg():
                    time.sleep(1)
                
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    self.typewriter_effect(f"\n❌ Not quite! {attempts} attempt(s) left. Try again or type 'hint' for help.")
                else:
                    self.typewriter_effect("\n😵 Out of attempts! The correct fix was: " + challenge["solution"])
                    self.skills["Patience"] = max(1, self.skills["Patience"])
                    return False
    
    def play(self):
        self.display_header()
        self.animate_loading()
        self.get_player_name()
        
        while True:
            self.show_status()
            
            lang_choice = input("Choose your challenge: [1] Python [2] JavaScript [3] Quit > ").strip()
            
            if lang_choice == "1":
                self.animate_loading(1)
                if not self.present_python_challenge():
                    break
            elif lang_choice == "2":
                self.animate_loading(1)
                if not self.present_javascript_challenge():
                    break
            elif lang_choice == "3":
                break
            else:
                self.typewriter_effect("Invalid choice! Try again.")
            
            time.sleep(1)
        
        self.typewriter_effect("\n\n=== GAME OVER ===")
        self.typewriter_effect(f"\nFinal Score: {self.score}")
        self.typewriter_effect(f"Bugs Fixed: {self.bugs_fixed}")
        self.typewriter_effect(f"Easter Eggs Found: {self.easter_eggs_found}")
        self.typewriter_effect("\nThanks for playing Debug Quest!")
        self.typewriter_effect("Keep debugging, brave coder!\n")

if __name__ == "__main__":
    game = DebugQuest()
    game.play()