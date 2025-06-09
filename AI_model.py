from groq import Groq
from prompt import rooms_background, destination_background, accomodation_background, activities, activities_for_content, what_to_expect

def room_ai(client, room: str, beds: float, capacity: float, property_: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": rooms_background(room, beds, capacity, property_)
            },
            {
                "role": "user",
                "content": "Generate me a description of a room " + room + " located at " + property_ +  " that contains " + str(beds) + " beds and has a capacity of " + str(capacity)
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion

def destination_ai(client, name: str, country: str, category: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": destination_background(name, country, category)
            },
            {
                "role": "user",
                "content": "Generate me a description of a destination spot " + name + " located at the country " + country + ". The category of the destination is " + category + " if that helps"
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion

def accomodation_ai(client, name: str, category: str, destination: str, area: str):
    
    content = ""

    '''If the area of the destination is unknown, then we don't need to ask'''
    if isinstance(area, float):
        content = "Generate me a description of the accomodations that the " + name + " lodge provides. The lodge is a " + category +  ". The destination of the lodge is at the  " + destination + "."
    else:
        content = "Generate me a description of the accomodations that the " + name + " lodge provides. The lodge is a " + category +  ". The destination of the lodge is at the  " + destination + ". The area it is located at " + area

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": accomodation_background(name, category, destination, area)
            },
            {
                "role": "user",
                "content": content
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion

def itin_ai(client, dest_one: str, dest_two: str, dest_three: str, dest_four: str, country: str):

    content = ""
    if isinstance(dest_three, float) and isinstance(dest_four, float):
        dest_three = ""
        dest_four = ""
        content = "Generate me a description what a tourist may expect when visiting " + dest_one + " and " + dest_two + "  at country: " + country 
    elif isinstance(dest_four, float):
        dest_four = ""
        content = "Generate me a description what a tourist may expect when visiting " + dest_one + ", " + dest_two + ", and " + dest_three + "  at country: " + country 
    else:
        content = "Generate me a description what a tourist may expect when visiting " + dest_one + ", " + dest_two + ", " + dest_three + ", " + dest_four + " located at country: "+ country 

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": what_to_expect(dest_one, dest_two, dest_three, dest_four, country)
        },
        {
            "role": "user",
            "content": content
        }
    ],
    model="llama-3.3-70b-versatile",
    )

    return chat_completion

def activities_ai(client, name: str, destination: str):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": activities(name, destination)
            },
            {
                "role": "user",
                "content": "Generate me a description of an activity called " + name + " located at the property " + destination 
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion

def activities_for_content_ai(client, activity: str, destinations: str, interests: str):
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": activities_for_content(activity, destinations, interests)
            },
            {
                "role": "user",
                "content": "Generate me a description of the content of an activity called " + activity + " located at the properties: " + destinations + ". The core of the activity is focused on: " + interests 
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion
