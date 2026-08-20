"""
TASK 2: Phishing Awareness Training
--------------------------------------
An interactive console-based training module about phishing attacks.
Walks the user through lessons on recognizing phishing emails and
social engineering tactics, then tests them with a quiz.

Key concepts used: functions, while loop, if-elif, lists, dictionaries,
string formatting, input/output
"""

import time

LESSONS = [
    {
        "title": "What is Phishing?",
        "content": """
Phishing is a social engineering attack where an attacker pretends to
be a trustworthy source (a bank, employer, or delivery company) to
trick you into giving up passwords, card numbers, or clicking a
malicious link.

Common types:
  - Email phishing   : fake emails that look official
  - Smishing         : phishing over SMS/text messages
  - Spear phishing    : a targeted attack using details about you specifically
"""
    },
    {
        "title": "Real-World Example — Spot the Red Flags",
        "content": """
Example phishing email:

    From:    support@secure-bank-alerts.info
    Subject: WARNING: Your account will be suspended in 24 hours!
    Body:    Dear Customer, we detected unusual activity.
             Click here to verify your identity immediately
             or your account will be locked.

Red flags in this example:
  1. The sender domain ("secure-bank-alerts.info") is NOT the bank's
     real domain — a classic imitation trick.
  2. The subject line creates urgency and fear to stop you thinking
     clearly before you act.
  3. It uses a generic greeting ("Dear Customer") instead of your
     real name, showing it wasn't sent by an institution that
     actually has your account details.
"""
    },
    {
        "title": "Social Engineering Tactics",
        "content": """
Phishing rarely relies on technical tricks alone — it relies on
manipulating human behavior:

  - Urgency   : "act now or lose access"
  - Authority : pretending to be IT, HR, or a manager
  - Fear      : threats of account suspension or legal action
  - Curiosity : "you have a package waiting" / "someone tagged you"

Recognizing the emotional trigger is often faster than checking
every technical detail.
"""
    },
    {
        "title": "Best Practices to Protect Yourself",
        "content": """
  1. Check the sender's actual email address, not just the display name.
  2. Hover over links (don't click) to preview the real URL first.
  3. Never enter your password from a link in an email — go to the
     site directly by typing the URL yourself.
  4. Enable two-factor authentication (2FA) wherever possible.
  5. Report suspicious emails to your IT/security team instead of
     ignoring them.

When in doubt, verify through a separate channel — call the company
using a number you already trust, not one provided in the email.
"""
    },
]

QUIZ = [
    {
        "question": "An email creates panic, saying your account will be deleted in 1 hour unless you click a link. This is most likely:",
        "options": ["A routine account update", "A phishing urgency tactic", "A software bug"],
        "correct": 2,
        "explanation": "Creating panic and time pressure is a classic phishing tactic to stop you from thinking clearly.",
    },
    {
        "question": "The safest way to check a suspicious link is to:",
        "options": ["Click it to see where it goes", "Hover over it to preview the real URL first", "Forward it to a friend"],
        "correct": 2,
        "explanation": "Hovering reveals the real destination URL without the risk of actually clicking a malicious link.",
    },
    {
        "question": "Which sender address below is most suspicious?",
        "options": ["billing@yourbank.com", "support@yourbank-secure-alerts.info", "help@yourbank.com"],
        "correct": 2,
        "explanation": "The extra words appended to the domain are a common trick used to imitate a real, trusted brand.",
    },
]


def print_header(title):
    print("\n" + "=" * 55)
    print(f"  {title}")
    print("=" * 55)


def run_lessons():
    """Walk the user through each lesson, one at a time."""
    for i, lesson in enumerate(LESSONS, start=1):
        print_header(f"Lesson {i} of {len(LESSONS)}: {lesson['title']}")
        print(lesson["content"])
        input("Press Enter to continue to the next section... ")


def run_quiz():
    """Ask each quiz question and track the user's score."""
    print_header("Final Quiz")
    print("Answer each question by typing 1, 2, or 3.\n")

    score = 0

    for i, q in enumerate(QUIZ, start=1):
        print(f"Q{i}. {q['question']}")
        for idx, option in enumerate(q["options"], start=1):
            print(f"   {idx}. {option}")

        while True:
            answer = input("Your answer: ").strip()
            if answer in ["1", "2", "3"]:
                answer = int(answer)
                break
            print("Please enter 1, 2, or 3.")

        if answer == q["correct"]:
            print("✅ Correct!", q["explanation"], "\n")
            score += 1
        else:
            correct_text = q["options"][q["correct"] - 1]
            print(f"❌ Not quite. The correct answer was: '{correct_text}'.")
            print(q["explanation"], "\n")

        time.sleep(0.3)

    return score


def show_results(score):
    total = len(QUIZ)
    pct = round((score / total) * 100)

    print_header("Training Complete")
    print(f"You scored {score}/{total} ({pct}%)\n")

    if pct >= 70:
        print("Great job — you're spotting the right red flags!")
    else:
        print("Good start — consider reviewing the lessons above and trying again.")


def main():
    print_header("PHISHING AWARENESS TRAINING")
    print("This short module will teach you how to recognize phishing")
    print("emails and fake websites, then test your understanding.\n")
    input("Press Enter to begin... ")

    run_lessons()
    score = run_quiz()
    show_results(score)

    print("\nThanks for completing the Phishing Awareness Training module!")


if __name__ == "__main__":
    main()
