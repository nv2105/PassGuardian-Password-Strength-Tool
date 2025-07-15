import re
import time

def run_password_tester():
    def welcome_message():
        print("\n" + "="*50)
        print("🚀 Welcome to PassGuardian: Smart Password Evaluator! 🔐")
        print("Let’s test your password’s strength with smart feedback!")
        print("="*50 + "\n")

    def check_password_strength(password):
        strength_score = 0
        feedback = []

        print("\n🔍 Checking password strength...\n")
        time.sleep(1)

        if len(password) >= 8:
            strength_score += 1
        else:
            feedback.append("🚩 Your password is too short! (Minimum 8 characters needed)")

        if re.search(r'[A-Z]', password):
            strength_score += 1
        else:
            feedback.append("🔑 Add at least one UPPERCASE letter to strengthen your password.")

        if re.search(r'[a-z]', password):
            strength_score += 1
        else:
            feedback.append("🔑 Add at least one lowercase letter to balance your password.")

        if re.search(r'[0-9]', password):
            strength_score += 1
        else:
            feedback.append("🔢 Include at least one number to make it more secure.")

        if re.search(r'[@$!%*?&]', password):
            strength_score += 1
        else:
            feedback.append("💥 Use special characters like @, $, !, %, &, etc. to make it harder to guess.")

        common_passwords = ['password', '123456', '123456789', 'qwerty', 'abc123']
        if password.lower() in common_passwords:
            feedback.append("⚠️ Your password is too common! Choose something more unique.")

        if strength_score <= 2:
            return "Weak password", feedback
        elif strength_score in [3, 4]:
            return "Moderate password", feedback
        else:
            return "🎉 Strong password!", feedback

    # CLI loop
    welcome_message()
    while True:
        print("\nType 'exit' to leave the tester anytime.")
        password = input("\n🔐 Enter a password to test its strength: ")
        if password.lower() == 'exit':
            print("\n👋 Thanks for using PassGuardian! Stay secure! 💻")
            break

        strength, feedback = check_password_strength(password)
        print("\n" + "="*50)
        print(f"🔒 Password Strength: {strength}")
        print("="*50)

        if feedback:
            print("\n💡 Tips to improve your password:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("\n🎉 Your password is strong and ready to protect your data! 💪🔐")

        print("\n" + "-"*50 + "\n")
