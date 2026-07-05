"""Module for determining Bob's responses."""

def response(hey_bob):
    """Return Bob's response to what someone says to him."""
    stripped = hey_bob.strip()
    is_yelling = stripped.upper() == stripped and stripped.lower() != stripped
    is_question = stripped.endswith("?")
    is_silence = len(stripped) == 0

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    if is_silence:
        return "Fine. Be that way!"
    return "Whatever."