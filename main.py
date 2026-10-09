# Q2 Seatwork 1 PYSCRIPT
from pyscript import document, display

def check_club(e):
    # Clear previous result
    document.getElementById("announce_result").innerHTML = ""
    
    # Get user input values
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    
    # Combine first and last name into full name
    name = f"{first_name} {last_name}"

    # List of official candidates
    candidates = [
        'Francis Fernandez', 
        'Gavin Ruiz', 
        'Edrian Correa', 
        'Philip Ponce', 
        'Julian Anaque', 
        'Andrik David', 
        'Annika De Vera', 
        'Eliana Daet',
        'Lance Catu'
    ]

    # Check if candidate exists in list (True or False)
    check_candidate = name in candidates
    # Turns check_candidate to integer (0 or 1)
    check_candidate = int(check_candidate)

    # Tuple that contains messages with index (0 for Sorry... and 1 for Congratulations...)
    messages = ((f"Sorry {name}, your name is not on the list."), (f"Congratulations {name}! You are now part of the ICT Club."))

    # Select messages based on index of message based on the check_candidate number
    result_message = messages[check_candidate]

    display(result_message, target="announce_result")