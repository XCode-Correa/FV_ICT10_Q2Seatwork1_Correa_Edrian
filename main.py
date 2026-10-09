# Q2 Seatwork 1 PYSCRIPT
from pyscript import document, display

def check_club(event):
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

    messages = [
        f"Sorry {name}, your name is not on the list.",
        f"Congratulations {name}! You are now part of the ICT club."
    ]

    # Select message using boolean as list index (False=0, True=1)
    result_message = messages[check_candidate]

    display(result_message, target="announce_result")