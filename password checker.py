import re

def check_password_strength(password):
    """Check the complexity of a password and return a strength score."""
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))  # Convert to boolean
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[@$!%*?&]', password))

    # Calculate strength score
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Strength levels based on criteria met
    if strength_score == 5:
        return "🔒 Strong Password ✅"
    elif strength_score >= 3:
        return "🟡 Medium Strength ⚠️"
    else:
        return "❌ Weak Password 🚫 (Try adding more complexity)"

# ===== Example Usage =====
password = input("Enter a password: ")
print(check_password_strength(password))
