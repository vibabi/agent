from langchain_core.tools import tool
from datetime import datetime

# Інструмент 1: Час (щоб агент знав "сьогодні")
@tool
def get_current_time(dummy: str = "") -> str:
    """Повертає поточну дату та час у форматі ISO. Використовуй, коли питають про 'зараз' або 'сьогодні'."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Інструмент 2: Довідник (щоб показати, що агент вміє не тільки рахувати)
@tool
def explain_business_term(term: str) -> str:
    """Пояснює бізнес-терміни (ROI, Margin, CAC, LTV)."""
    glossary = {
        "ROI": "Return on Investment - коефіцієнт окупності інвестицій.",
        "Margin": "Різниця між собівартістю та ціною продажу.",
        "LTV": "Life Time Value - скільки грошей клієнт приносить за весь час.",
    }
    # Простий пошук по словнику
    for key, value in glossary.items():
        if key.lower() in term.lower():
            return value
    return "Вибач, я не знаю такого терміну в моїй базі."