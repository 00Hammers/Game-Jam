label day03:
    scene bg corridoio 1
    
    narrator "3° giorno fratm"
    
    show connor at right

    connor "Mi vuoi bene?"

    menu:
        "Sì":
            $ score += 1
        
        "No":
            $ score -= 1

    jump end_day03