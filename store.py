patients = []
consultations = []

def create(name, birthday, cpf, gender, street, city, state):
    
    user = {
        "id": len(patients) + 1,
        "name": name,
        "birthday": birthday,
        "cpf": cpf,
        "gender": gender,
        "address": {
            "street": street,
            "city": city,
            "state": state
        }
    }
    
    patients.append(user)
    
    return True

def update(cpf, name=None, birthday=None, gender=None, street=None, city=None, state=None):
    for patient in patients:
        if patient["cpf"] == cpf:
            if name:
                patient["name"] = name
            if birthday:
                patient["birthday"] = birthday
            if gender:
                patient["gender"] = gender
            if street:
                patient["address"]["street"] = street
            if city:
                patient["address"]["city"] = city
            if state:
                patient["address"]["state"] = state
            return True
    return False