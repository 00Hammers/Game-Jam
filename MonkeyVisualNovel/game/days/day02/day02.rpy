label day02:
    scene bg corridoio 1
    
    narrator "2° giorno fratm"
    
    show connor at left

    connor "Mi vuoi bene?"

    menu:
        "Sì":
            $ score += 1
        
        "No":
            $ score -= 1

    jump end_day02