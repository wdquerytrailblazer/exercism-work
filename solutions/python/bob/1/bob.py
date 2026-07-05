def response(hey_bob):
    stripped = hey_bob.strip()
    is_silence = len(stripped) == 0
    is_question = stripped.endswith("?")
    is_yelling = stripped.upper() == stripped and stripped.lower() != stripped

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    elif is_silence:
        return "Fine. Be that way!"
    else:
        return "Whatever."