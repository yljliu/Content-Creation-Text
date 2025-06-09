import pandas as pd

class Write:

    def __init__(self):
       pass
    
    '''Write results into CSV File'''
    def getFile(self, results: dict[str, any]):

        dataframe = pd.DataFrame({"Name": results["names"], "Description": results["result"]})

        '''Each type specifies the name of the CSV file'''
        if results["type"] == "destination":
            dataframe.to_csv("destination.csv", index=False)

        elif results["type"] == "accomodation":
            dataframe.to_csv("accomodation.csv", index=False)

        elif results["type"] == "activities for content":
            dataframe.to_csv("activities_for_content.csv", index=False)
        
        elif results["type"] == "activity":
            dataframe.to_csv("activity.csv", index=False)
        
        elif results["type"] == "itinerary":
            dataframe.to_csv("itinerary.csv", index=False)

        elif results["type"] == "room":
            dataframe.to_csv("room.csv", index=False)
