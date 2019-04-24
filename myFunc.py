def caught_speeding(speed, is_birthday):
    if ((speed <= 60) and is_birthday):
        return "No Ticket"
    elif ((speed >= 61) and (speed <= 80) and is_birthday):
        return "Small Ticket"
    elif (speed >= 61) and (speed <= 80):
        return "Big Ticket"
    elif speed >= 81:
        return "Very Big Ticket"