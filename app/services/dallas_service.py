from app.models import PoliceCall

def create_police_call(street_number, street_name, description, created):
    return PoliceCall.objects.create(
    	street_number = street_number,
    	street_name = street_name,
    	description = description,
    	created = created)