def grade_scale(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 50 <= score < 60:
        return 'E'
    elif 30 <= score < 50:
        return 'FX'
    elif 0 <= score < 30:
        return 'F'
    else:
        return 'Invalid score'

# try:
#     score = float(input("Write a score (0-100): "))
#     print(f"Your Uni Score: {grade_scale(score)}")
# except ValueError:
#     print("Write a score.")
