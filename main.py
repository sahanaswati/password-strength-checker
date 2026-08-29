import math
import re


def evaluate_password(password):
    # 1. Policy Criteria Checks
    length = len(password)
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # 2. Calculate Pool Size and Entropy
    pool_size = 0

    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_special:
        pool_size += 32

    entropy = (
        length * math.log2(pool_size)
        if pool_size > 0 and length > 0
        else 0
    )

    # 3. Classify Strength
    if entropy < 28:
        strength = "Weak"
    elif entropy < 50:
        strength = "Moderate"
    elif entropy < 70:
        strength = "Strong"
    else:
        strength = "Exceptional"

    # 4. Feedback Generation
    feedback = []

    if length < 12:
        feedback.append("Increase length to at least 12 characters.")

    if not (has_lower and has_upper):
        feedback.append("Mix uppercase and lowercase letters.")

    if not has_digit:
        feedback.append("Include numbers.")

    if not has_special:
        feedback.append("Include special characters.")

    return {
        "Entropy": round(entropy, 2),
        "Strength": strength,
        "Feedback": (
            feedback
            if feedback
            else ["Great! Strong password pattern."]
        )
    }


if __name__ == "__main__":
    password = input("Enter password: ")
    result = evaluate_password(password)

    print("\nPassword Strength Report")
    print("Entropy:", result["Entropy"])
    print("Strength:", result["Strength"])
    print("Feedback:", result["Feedback"])
    
  
