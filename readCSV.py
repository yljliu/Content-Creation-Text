# import pandas as pd
# from googleAPI import Sheet

# def destination(id: str):
#     sheet = Sheet(range = "Destination!B1:V", id=id)
#     df_destination = sheet.read_sheet()
#     df_destination = df_destination.loc[:, ['name', 'country_name', 'Destination Category']]
#     df_destination = df_destination.to_dict(orient = 'records')
#     return df_destination

# def accomodation(id: str):
#     sheet = Sheet(range = "Accommodation!B1:N", id=id)
#     df_accomodation = sheet.read_sheet()
#     df_accomodation = df_accomodation.loc[:, ['Lodge Name', 'Category', 'Destination', 'Area']]
#     df_accomodation = df_accomodation.to_dict(orient = 'records')
#     return df_accomodation

# def activities_for_content(id: str):
#     sheet = Sheet(range = "Activities For Content!A1:Q", id=id)
#     df_activities_content = sheet.read_sheet()
#     df_activities_content = df_activities_content.loc[:, ['name', 'destinations', 'interests']]
#     df_activities_content = df_activities_content.to_dict(orient = 'records')
#     return df_activities_content

# def room_type(id: str):
#     sheet = Sheet(range = "Room Type!B2:W", id=id)
#     df_room_type = sheet.read_sheet()
#     df_room_type = df_room_type.loc[:, ['Name', 'Beds', 'Capacity', 'Property']]
#     df_room_type = df_room_type.to_dict(orient = 'records')
#     return df_room_type

# def activities(id: str):
#     sheet = Sheet(range = "Activities!A1:M", id=id)
#     df_activities = sheet.read_sheet()
#     df_activities = df_activities.loc[:, ['name', 'destination']]
#     df_activities = df_activities.to_dict(orient = 'records')
#     return df_activities

# def preset_itineraries(id: str):
#     sheet = Sheet(range = "Pre-set Itineraries", id=id)
#     df_iten = sheet.read_sheet()
#     df_iten = df_iten.loc[:, ['Destination 1', 'Destination 2', 'Destination 3', 'Destination 4', 'Country']]
#     df_iten = df_iten.to_dict(orient = 'records')
#     return df_iten

"""
Old Code
"""
import pandas as pd
def destination():
    df_destination = pd.read_excel("New Database.xlsx", sheet_name = "Destination", usecols = "B,C,V")
    df_destination = df_destination.to_dict(orient = 'records')
    return df_destination

def accomodation():
   df_accomodation = pd.read_excel("New Database.xlsx", sheet_name = "Accommodation", usecols = "B,C,H,N")
   df_accomodation = df_accomodation.to_dict(orient = 'records')
   return df_accomodation

def activities_for_content():
    df_activities_content = pd.read_excel("New Database.xlsx", sheet_name = "Activities for Content", usecols = "A,J,L")
    print(df_activities_content.head(5))
    df_activities_content = df_activities_content.to_dict(orient = 'records')
    return df_activities_content

def room_type():
    df_room_type = pd.read_excel("New Database.xlsx", sheet_name = "Room Type", usecols = "B,D,E,J", skiprows = 1)
    print(df_room_type.head(5))
    df_room_type = df_room_type.to_dict(orient = 'records')
    return df_room_type

def activities():
    df_activities = pd.read_excel("New Database.xlsx", sheet_name = "Activities", usecols = "A,J")
    print(df_activities.head(5))
    df_activities = df_activities.to_dict(orient = 'records')
    return df_activities

def preset_itineraries():
    df_iten = pd.read_excel("New Database.xlsx", sheet_name = "Pre-set Itineraries", usecols = "F,H,J,M,R")
    print(df_iten.head(5))
    df_iten = df_iten.to_dict(orient = 'records')
    return df_iten
