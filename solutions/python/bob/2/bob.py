def response(hey_bob):
    stripped = hey_bob.strip()
    is_silence = len(stripped) == 0
    is_question = stripped.endswith("?")
    
    # Honestly I do not understand much about code below
    
    is_yelling = stripped.upper() == stripped and stripped.lower() != stripped

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    if is_silence:
        return "Fine. Be that way!"
    else:
        return "Whatever."