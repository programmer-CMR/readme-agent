import random
from datetime import datetime

# Local pool of quotes — you can expand this list anytime.
LOCAL_QUOTES = [
    (
        "Technology does not move things forward by itself. "
        "People do, through consistent effort and practical decisions. "
        "Progress happens when tools are used with intention. "
        "Innovation is not magic; it's discipline. "
        "Real growth begins when action replaces theory. - Alan Richards"
    ),
    (
        "Improvement in technology is rarely instant. "
        "It comes from repeated trials and adjustments. "
        "Systems become better when someone maintains them. "
        "Progress requires clarity, not perfection. "
        "Consistency is more valuable than inspiration. - Maria Thompson"
    ),
    (
        "Tools do not solve problems without direction. "
        "Every reliable system is built through small fixes over time. "
        "Progress is the result of structure, not luck. "
        "Technology amplifies habits, good or bad. "
        "The real upgrade is the mindset using the tool. - David Grant"
    ),
    (
        "Success in technology comes from understanding limits. "
        "A stable system matters more than a flashy one. "
        "Progress is steady, not dramatic. "
        "Focus on reliability before anything else. "
        "Every improvement starts with one practical change. - Karen Mitchell"
    ),
]

def generate_local_quote() -> str:
    """Return a structured, 5-line, non-poetic tech-related quote."""
    return random.choice(LOCAL_QUOTES)

def improve_readme_content(old_content: str) -> str:
    quote = generate_local_quote()

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    # Replace or insert the daily quote section
    if "## 📅 Daily Quote" in old_content:
        before, _ = old_content.split("## 📅 Daily Quote", 1)
        new_section = (
            f"## 📅 Daily Quote\n\n"
            f"> \"{quote}\"\n\n"
            f"*🕒 Updated on {timestamp}*"
        )
        return before + new_section
    else:
        return (
            old_content
            + f"\n\n## 📅 Daily Quote\n\n> \"{quote}\"\n\n*🕒 Updated on {timestamp}*"
        )
