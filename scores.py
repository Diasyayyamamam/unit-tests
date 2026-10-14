# Студент: Друженко Діана (Група: 3_41, Журнал: 13, Варіант: 3)

def score_to_ects(score: int) -> str:
    """Переводить бал від 0 до 100 у шкалу ECTS (A-F)."""
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        raise ValueError("Бал має бути в межах від 0 до 100")
    
    score = int(score)
    
    if 90 <= score <= 100:
        return "A"
    elif 82 <= score <= 89:
        return "B"
    elif 74 <= score <= 81:
        return "C"
    elif 64 <= score <= 73:
        return "D"
    elif 60 <= score <= 63:
        return "E"
    else:
        return "F"