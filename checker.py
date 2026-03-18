import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include at least one numeric digit.")

    # special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add one special character (!@#$ etc).")

    # strength levels
    strength_levels = {
        5: "Very Strong 💪",
        4: "Strong ✔",
        3: "Moderate 🙂",
        2: "Weak ⚠",
        1: "Very Weak ❌",
        0: "Extremely Weak ❌"
    }

    return strength_levels[score], score, suggestions
