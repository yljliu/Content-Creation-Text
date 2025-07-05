from google import genai
from google.genai.errors import ClientError
import time
import os
from readCSV import destination, accomodation, activities_for_content, room_type, activities, preset_itineraries
from AI_model import room_ai, destination_ai, accomodation_ai, itin_ai, activities_for_content_ai, activities_ai
from writeCSV import Write

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

'''Generate descriptions for room types'''
def main_room(id: str):

    room_array = room_type(id)
    results = []
    names = []
    for dictionary in room_array:
        values = list(dictionary.values())
        sleep_time = 0
        time_slept = 2
        exhaust = ""
        while True:
            try:
                chat = room_ai(client, values[0], values[1], values[2], values[3])
                names.append(values[0])
                results.append(chat)
                break
            except ClientError as e:
                sleep_time += 1
                if sleep_time > 6:
                    exhaust = "Exhausted"
                    return "Exhausted"
                time.sleep(time_slept)
                time_slept = time_slept * 2
            except Exception as e:
                results.append("")
                names.append(values[0])
                break
        if exhaust == "Exhausted":
            print("Error, Resource Exhausted")
            break
        break
    return {"result": results, "names": names, "type": "room"}

'''Generate descriptions for destinations'''
def main_destination(id: str):

    destination_array = destination(id)
    results = []
    names = []
    for dictionary in destination_array:
        values = list(dictionary.values())
        sleep_time = 0
        time_slept = 2
        exhaust = ""
        while True:
            try:
                chat = destination_ai(client, values[0], values[1], values[2])
                names.append(values[0])
                results.append(chat)
                break
            except ClientError as e:
                sleep_time += 1
                if sleep_time > 6:
                    exhaust = "Exhausted"
                    return "Exhausted"
                time.sleep(time_slept)
                time_slept = time_slept * 2
            except Exception as e:
                results.append("")
                names.append(values[0])
                break
        if exhaust == "Exhausted":
            print("Error, Resource Exhausted")
            break
        break
    return {"result": results, "names": names, "type": "destination"}

'''Generate descriptions for accomodations'''
def main_accomodation(id: str):
    
    accomodation_array = accomodation(id)
    results = []
    names = []
    for dictionary in accomodation_array:
        values = list(dictionary.values())
        sleep_time = 0
        time_slept = 2
        exhaust = ""
        while True:
            try:
                chat = accomodation_ai(client, values[0], values[1], values[2], values[3])
                results.append(chat)
                names.append(values[0])
                break
            except ClientError as e:
                sleep_time += 1
                if sleep_time > 6:
                    exhaust = "Exhausted"
                    return "Exhausted"
                time.sleep(time_slept)
                time_slept = time_slept * 2
            except Exception as e:
                results.append("")
                names.append(values[0])
                break
        if exhaust == "Exhausted":
            print("Error, Resource Exhausted")
            break
        break
    return {"result": results, "names": names, "type": "accomodation"}

'''Generate descriptions for itineraries'''
def main_itinerary(id: str):
    
    itineraries_array = preset_itineraries(id)
    results = []
    names = []
    for dictionary in itineraries_array:
        values = list(dictionary.values())
        sleep_time = 0
        time_slept = 2
        exhaust = ""
        while True:
            try:
                chat = itin_ai(client, values[0], values[1], values[2], values[3], values[4])
                results.append(chat)
                names.append(values[0])
                break
            except ClientError as e:
                sleep_time += 1
                if sleep_time > 6:
                    exhaust = "Exhausted"
                    return "Exhausted"
                time.sleep(time_slept)
                time_slept = time_slept * 2
            except Exception as e:
                results.append("")
                names.append(values[0])
                break
        if exhaust == "Exhausted":
            print("Error, Resource Exhausted")
            break
        break
    return {"result": results, "names": names, "type": "itinerary"}

'''Generate descriptions for activities'''
def main_activities(id: str):
    
    activities_array = activities(id)
    results = []
    names = []
    for dictionary in activities_array:
        values = list(dictionary.values())
        sleep_time = 0
        time_slept = 2
        exhaust = ""
        while True:
            try:
                chat = activities_ai(client, values[0], values[1])
                results.append(chat)
                names.append(values[0])
                break
            except ClientError as e:
                sleep_time += 1
                if sleep_time > 6:
                    exhaust = "Exhausted"
                    return "Exhausted"
                time.sleep(time_slept)
                time_slept = time_slept * 2
            except Exception as e:
                results.append("")
                names.append(values[0])
                break
        if exhaust == "Exhausted":
            print("Error, Resource Exhausted")
            break
    return {"result": results, "names": names, "type": "activity"}

'''Generate descriptions for activities for content'''
def main_activities_for_content(id: str):
    
    activities_for_content_array = activities_for_content(id)
    results = []
    names = []
    for dictionary in activities_for_content_array:
        values = list(dictionary.values())
        sleep_time = 0
        time_slept = 2
        exhaust = ""
        while True:
            try:
                chat = activities_for_content_ai(client, values[0], values[1], values[2])
                results.append(chat)
                names.append(values[0])
                break
            except ClientError as e:
                sleep_time += 1
                if sleep_time > 6:
                    exhaust = "Exhausted"
                    return "Exhausted"
                time.sleep(time_slept)
                time_slept = time_slept * 2.01
            except Exception as e:
                results.append("")
                names.append(values[0])
                break
        if exhaust == "Exhausted":
            print("Error, Resource Exhausted")
            break
    return {"result": results, "names": names, "type": "activities for content"}


if __name__ == '__main__':

    '''Create a Write class to write our results into a CSV file'''
    print("What would you like to generate me a description of?\n1. Room Type\n2. Destination\n3. Accomodations\n4. Itineraries\n5. Activities for Content\n6. Activities\n")
    
    write = Write()
    while True:
        num = int(input("Enter a number 1 to 6, each corresponding its respective category: "))
        if num == 1:
            spreadsheet_id = input("Enter the ID of your spreadsheet: ")
            write.getFile(main_room(spreadsheet_id))
            break
        elif num == 2:
            spreadsheet_id = input("Enter the ID of your spreadsheet: ")
            write.getFile(main_destination(spreadsheet_id))
            break
        elif num == 3:
            spreadsheet_id = input("Enter the ID of your spreadsheet: ")
            write.getFile(main_accomodation(spreadsheet_id))
            break
        elif num == 4:
            spreadsheet_id = input("Enter the ID of your spreadsheet: ")
            write.getFile(main_itinerary(spreadsheet_id))
            break
        elif num == 5:
            spreadsheet_id = input("Enter the ID of your spreadsheet: ")
            write.getFile(main_activities(spreadsheet_id))
            break
        elif num == 6:
            spreadsheet_id = input("Enter the ID of your spreadsheet: ")
            write.getFile(main_activities_for_content(spreadsheet_id))
            break
        else:
            print("Invalid Number, try again")
