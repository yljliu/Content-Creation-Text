import pandas as pd
from googleAPI import Sheet

def destination():
    sheet = Sheet(range = "Destination!B1:V")
    df_destination = sheet.read_sheet()
    df_destination = df_destination.loc[:, ['name', 'country_name', 'Destination Category']]
    df_destination = df_destination.to_dict(orient = 'records')
    return df_destination

def accomodation():
    sheet = Sheet(range = "Accommodation!B1:N")
    df_accomodation = sheet.read_sheet()
    df_accomodation = df_accomodation.loc[:, ['Lodge Name', 'Category', 'Destination', 'Area']]
    df_accomodation = df_accomodation.to_dict(orient = 'records')
    return df_accomodation

def activities_for_content():
    sheet = Sheet(range = "Activities For Content!A1:Q")
    df_activities_content = sheet.read_sheet()
    df_activities_content = df_activities_content.loc[:, ['name', 'destinations', 'interests']]
    df_activities_content = df_activities_content.to_dict(orient = 'records')
    return df_activities_content

def room_type():
    sheet = Sheet(range = "Room Type!B2:W")
    df_room_type = sheet.read_sheet()
    df_room_type = df_room_type.loc[:, ['Name', 'Beds', 'Capacity', 'Property']]
    df_room_type = df_room_type.to_dict(orient = 'records')
    return df_room_type

def activities():
    sheet = Sheet(range = "Activities!A1:M")
    df_activities = sheet.read_sheet()
    df_activities = df_activities.loc[:, ['name', 'destination']]
    df_activities = df_activities.to_dict(orient = 'records')
    return df_activities

def preset_itineraries():
    sheet = Sheet(range = "Pre-set Itineraries")
    df_iten = sheet.read_sheet()
    df_iten = df_iten.loc[:, ['Destination 1', 'Destination 2', 'Destination 3', 'Destination 4', 'Country']]
    df_iten = df_iten.to_dict(orient = 'records')
    return df_iten

"""
Old Code
"""
# def destination():
#     df_destination = pd.read_excel("C:\\Users\\Chubb\\Downloads\\New Database.xlsx", sheet_name = "Destination", usecols = "B,C,V")
#     df_destination = df_destination.to_dict(orient = 'records')
#     return df_destination

# def accomodation_():
#    df_accomodation = pd.read_excel("C:\\Users\\Chubb\\Downloads\\New Database.xlsx", sheet_name = "Accommodation", usecols = "B,C,H,N")
#    print(df_accomodation.head(5))
#    df_accomodation = df_accomodation.to_dict(orient = 'records')
#    return df_accomodation

# def activities_for_content_():
#     df_activities_content = pd.read_excel("C:\\Users\\Chubb\\Downloads\\New Database.xlsx", sheet_name = "Activities for Content", usecols = "A,J,L")
#     print(df_activities_content.head(5))
#     df_activities_content = df_activities_content.to_dict(orient = 'records')
#     return df_activities_content

# def room_type_():
#     df_room_type = pd.read_excel("C:\\Users\\Chubb\\Downloads\\New Database.xlsx", sheet_name = "Room Type", usecols = "B,D,E,J", skiprows = 1)
#     print(df_room_type.head(5))
#     df_room_type = df_room_type.to_dict(orient = 'records')
#     return df_room_type

# def activities_():
#     df_activities = pd.read_excel("C:\\Users\\Chubb\\Downloads\\New Database.xlsx", sheet_name = "Activities", usecols = "A,J")
#     print(df_activities.head(5))
#     df_activities = df_activities.to_dict(orient = 'records')
#     return df_activities

# def preset_itineraries_():
#     df_iten = pd.read_excel("C:\\Users\\Chubb\\Downloads\\New Database.xlsx", sheet_name = "Pre-set Itineraries", usecols = "F,H,J,M,R")
#     print(df_iten.head(5))
#     df_iten = df_iten.to_dict(orient = 'records')
#     return df_iten
