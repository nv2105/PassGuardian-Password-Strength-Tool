from passguardian.breaches import check_password_breach
from passguardian.generator import generate_password
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box


import re
import time
import math

console = Console()


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
    import math

    def calculate_entropy(password):
        charset = 0
        if re.search(r'[a-z]', password): charset += 26
        if re.search(r'[A-Z]', password): charset += 26
        if re.search(r'[0-9]', password): charset += 10
        if re.search(r'[@$!%*?&]', password): charset += 10

        if charset == 0:
            return 0.0

        entropy = len(password) * math.log2(charset)
        return round(entropy, 2)


    # CLI loop
    welcome_message()
    while True:
        print("\nType 'exit' to leave the tester anytime.")
        print("Type 'generate' to create a strong suggested password.")

        password = input("\n🔐 Enter a password to test its strength: ")

        if password.lower() == 'exit':
            print("\n👋 Thanks for using PassGuardian! Stay secure! 💻")
            break

        elif password.lower() == 'generate':
            try:
                length = int(input("🔢 Desired length (min 8): "))
                if length < 8:
                    print("❌ Length must be at least 8 characters.")
                    continue

                use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
                use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
                use_digits = input("Include numbers? (y/n): ").lower() == 'y'
                use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

                password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
                print(f"\n🎁 Your generated password is: {password}")
                print("🔁 Testing its strength now...\n")

            except Exception as e:
                print(f"❌ Error: {e}")
                continue

        # --- Common evaluation (runs for both typed & generated password) ---
        entropy = calculate_entropy(password)
        console.print(f"🧠 Estimated Entropy: [bold cyan]{entropy} bits[/bold cyan]")


        breach_count = check_password_breach(password)
        if breach_count == -1:
            console.print("🌐 [bold yellow]Breach check failed[/bold yellow] (offline or API error).")
        elif breach_count == 0:
            console.print("✅ [bold green]No known breaches[/bold green] found for this password.")
        else:
            console.print(f"⚠️ [bold red]WARNING:[/bold red] This password was found in [bold]{breach_count:,}[/bold] breaches! [italic]Avoid using it.[/italic]")

        strength, feedback = check_password_strength(password)
        console.print(Panel.fit(
            f"🔒 Password Strength: {strength}",
            title="Result",
            style="bold green" if "Strong" in strength else "bold yellow" if "Moderate" in strength else "bold red",
            box=box.ROUNDED
        ))


        if feedback:
            tips = "\n".join(f"• {tip}" for tip in feedback)
            console.print(Panel(tips, title="💡 Tips to Improve", style="bold yellow", box=box.SQUARE))
        else:
            console.print("[bold green]🎉 Your password is strong and ready to protect your data! 💪🔐[/bold green]")

        print("\n" + "-"*50 + "\n")


# CLI wrapper for packaging entry point
def main():
    run_password_tester()