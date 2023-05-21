label day01:
    scene bg corridoio 1
    
    narrator "Primo giorno fratm"
    
    show connor

    connor "Mi vuoi bene?"

    menu:
        "Sì":
            $ score += 1
        
        "No":
            $ score -= 1

    jump end_day01