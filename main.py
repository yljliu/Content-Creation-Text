import os
from groq import Groq, RateLimitError
from readCSV import destination, accomodation, activities_for_content, room_type, activities, preset_itineraries
from AI_model import room_ai, destination_ai, accomodation_ai, itin_ai, activities_for_content_ai, activities_ai
from writeCSV import Write

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

'''Generate descriptions for room types'''
def main_room():

    room_array = room_type()
    results = []
    names = []
    for dictionary in room_array:
        values = list(dictionary.values())
        try:
            chat = room_ai(client, values[0], values[1], values[2], values[3])
            names.append(values[0])
            results.append(chat.choices[0].message.content)
        except RateLimitError as e:
            print("error")
            break
    return {"result": results, "names": names, "type": "room"}

'''Generate descriptions for destinations'''
def main_destination():

    destination_array = destination()
    results = []
    names = []
    for dictionary in destination_array:
        values = list(dictionary.values())
        try:
            chat = destination_ai(client, values[0], values[1], values[2])
            names.append(values[0])
            results.append(chat.choices[0].message.content)
        except RateLimitError as e:
            print("error")
            break
    return {"result": results, "names": names, "type": "destination"}

'''Generate descriptions for accomodations'''
def main_accomodation():
    
    accomodation_array = accomodation()
    results = []
    names = []
    for dictionary in accomodation_array:
        values = list(dictionary.values())
        try:
            chat = accomodation_ai(client, values[0], values[1], values[2], values[3])
            results.append(chat.choices[0].message.content)
            names.append(values[0])
        except RateLimitError as e:
            print("error")
            break
    return {"result": results, "names": names, "type": "accomodation"}

'''Generate descriptions for itineraries'''
def main_itinerary():
    
    itineraries_array = preset_itineraries()
    results = []
    names = []
    for dictionary in itineraries_array:
        values = list(dictionary.values())
        try:
            chat = itin_ai(client, values[0], values[1], values[2], values[3], values[4])
            results.append(chat.choices[0].message.content)
            names.append(values[0])
        except RateLimitError as e:
            print("error")
            break
    return {"result": results, "names": names, "type": "itinerary"}

'''Generate descriptions for activities'''
def main_activities():
    
    activities_array = activities()
    results = []
    names = []
    for dictionary in activities_array:
        values = list(dictionary.values())
        try:
            chat = activities_ai(client, values[0], values[1])
            results.append(chat.choices[0].message.content)
            names.append(values[0])
        except RateLimitError as e:
            print("error")
            break
    return {"result": results, "names": names, "type": "activity"}

'''Generate descriptions for activities for content'''
def main_activities_for_content():
    
    activities_for_content_array = activities_for_content()
    results = []
    names = []
    for dictionary in activities_for_content_array:
        values = list(dictionary.values())
        try:
            chat = activities_for_content_ai(client, values[0], values[1], values[2])
            results.append(chat.choices[0].message.content)
            names.append(values[0])
        except RateLimitError as e:
            print("error")
            break
    return {"result": results, "names": names, "type": "activities for content"}


if __name__ == '__main__':

    '''Create a Write class to write our results into a CSV file'''
    write = Write()
    #write.getFile(main_room())
    #write.getFile(main_destination())
    #write.getFile(main_accomodation())
    write.getFile(main_itinerary())
    write.getFile(main_activities())
    #write.getFile(main_activities_for_content())
