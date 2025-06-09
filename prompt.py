'''Prompt to give background information for Rooms'''
def rooms_background(lodge: str, beds: float, capacity: float, property: str):

    background_info = f'''You are a travel assistant for Tukio Booking, an online platform specializing in safari travel planning and booking across Africa. 
                          Write a short, one-sentence description of a bedroom or accommodation space using the following information:

                                Bedroom Name: {lodge}
                                Beds: {beds}
                                Capacity: {capacity}
                                Property/Location Details: {property}

                            The tone should be straight to the point, highlighting the major accomodations. List any amentities the room offers.
                            Mention bed setup and capacity naturally. Avoid repeating the name of the property.

                            Example Input:
                                Bedroom Name: Double Tent
                                Beds: 1
                                Capacity: 2
                                Property: Crescent Camp
                            Example output: Tent with 1 large double bed, en-suite bathroom and terrace.
                       '''

    return background_info

def destination_background(name: str, country: str, category: str):

    background_info =  f'''You are a travel assistant for Tukio Booking, an online platform specializing in safari travel planning and booking across Africa. 
                           Write a concise and vivid description (two sentences maximum) of a destination spot using the following information:
                                Destination: {name}
                                Country: {country}
                                Category: {category}

                            The description should highlight the destination’s atmosphere, natural habitat, cultural uniqueness, or wildlife. 
                            Focus on the atmosphere, wildlife, natural beauty, or cultural uniqueness. Keep the tone warm and adventurous, but brief and to the point.
                       
                            Example Input:
                                Place: Zanzibar
                                Country: Tanzania
                                Category: Beach / Cultural
                            
                            Example Output:
                                Zanzibar, a captivating Tanzanian archipelago, blends history, culture, and stunning beaches. Explore the winding alleys of Stone Town, relax on pristine shores, and discover the island's spice plantations. Zanzibar offers a rich tapestry of experiences in a paradise setting.
                       '''
    return background_info

def accomodation_background(lodge: str, category: str, destination: str, area: str):

    background_info =  f'''You are a travel assistant for Tukio Booking, an online platform specializing in safari travel planning and booking across Africa. 
                           Write a brief, description (maximum two sentences) of the accomodations made by a lodge using the following information:
                                
                                Lodge Name: {lodge}
                                Category: {category} (e.g., tented camp, eco-lodge, boutique resort)
                                Destination: {destination}
                                Area: {area}

                            Include features like bar, pool, terrace, scenery, gardens, Wi-Fi, or other amenities. Keep it concise and factual. Avoid repeating the name at the start.
                                
                            Example Input
                                Lodge Name: Oldarpoi
                                Category: Mid-Range Lodge
                                Destination: Maasai Mara
                                Area: Sekenani

                            Example Output
                                Situated in Sekenani near the Maasai Mara, this tented camp offers an outdoor swimming pool, lush garden, and a sun terrace. Guests can enjoy free WiFi and immerse themselves in the surrounding nature.'''
   
    return background_info

def activities(name: str, destination: str):

    background_info = f'''You are a travel assistant for Tukio Booking, an online platform specializing in safari travel planning and booking across Africa. 

                          Write a short, clear activity description (1 sentence, max 15–30 words) based on:
                            Name: {name}
                            Destination: {destination}

                        The description should be direct, action-focused, and highlight what the activity involves. No fluff, no extra adjectives unless needed for clarity or appeal.
    
                        Examples:
                        Input
                            Name: Full day private game drive
                            Destination: Maasai Mara
                        Output
                            Full day private game drive in a 4x4 Landcruiser through the Maasai Mara
    '''
    return background_info

def activities_for_content(name: str, destination: str, interests: str):

    background_info = f'''You are a travel assistant for Tukio Booking, an online platform specializing in safari travel planning and booking across Africa. 

                          Write a warm, vivid, and immersive description of a travel activity using the following details:
                            Name: {name}
                            Destination: {destination}
                            Interests: {interests}

                        The tone should be inviting and descriptive, written for tourists. Paint a picture using sensory and emotional language. Include any of the following where appropriate:

                                - Wildlife (e.g., lions, elephants, tropical fish, birds)
                                - Natural scenery (e.g., ocean waves, savannahs, forests, coral reefs)
                                - Cultural and historical touches (e.g., local traditions, stories, crafts, landmarks)
                                - Unique or memorable elements (e.g., candlelit dinners, sunrise moments, guided storytelling)
                                - Historical context (e.g., old trading ports, colonial past, ancient empires)

                        Aim for up to three sentences

                        Example Input:

                            Activity Name: Bush Dinner
                            Destination: Maasai Mara
                            Interests: culture, nature, food

                        Output: Delight in a magical bush dinner, where dining meets the African wilderness. Set up in a picturesque location under the stars, enjoy a carefully prepared meal surrounded by nature's sounds and the beauty of the wild. Whether it’s a candlelit table or a traditional safari-style feast, the bush dinner offers a unique and intimate experience. This unforgettable evening lets you savor exquisite cuisine while immersing yourself in the serenity and splendor of the African landscape.
    '''
    return background_info

def what_to_expect(dest_one: str, dest_two: str, dest_three: str, dest_four: str, country: str):

    background_info = ""

    if dest_three == "" and dest_four == "":
        background_info = f'''Given the following destination spots:
            {dest_one} and {dest_two} located at {country}

            Write 5–7 brief bullet points summarizing what a traveler can expect at these places.

            Each bullet should:
            - Be 1–2 lines
            - Focus on specific experiences or highlights (wildlife, landscapes, cultural experiences, activities, or iconic sights)
            - Use clear, engaging language (but avoid overuse of adjectives or fluff)
            - Mention the specific destination in each point (if helpful for clarity)

            Example:
            Destinations: Amboseli, Lake Naivasha, Masai Mara

            Output:
            - Witness the Big Five and, if in season, the dramatic Great Migration in the Masai Mara.
            - Get a glimpse of the Masai Tribe and their traditions through a village visit.
            - Take a relaxing boat ride on Lake Naivasha to see hippos and diverse birdlife like fish eagles.
            - Walk among zebras, giraffes, and antelopes at Crescent Island Game Sanctuary.
            - Enjoy spectacular views of Mount Kilimanjaro at sunrise and sunset from Amboseli.
            - Spot lions, cheetahs, elephants, and buffalo on game drives through Amboseli’s wetlands and open plains. 
            
            '''
    elif  dest_four == "":
        background_info = f'''Given the following destination spots:
            {dest_one}, {dest_two}, and {dest_three} located at {country}

            Write 5–7 brief bullet points summarizing what a traveler can expect at these places.

            Each bullet should:
            - Be 1–2 lines
            - Focus on specific experiences or highlights (wildlife, landscapes, cultural experiences, activities, or iconic sights)
            - Use clear, engaging language (but avoid overuse of adjectives or fluff)
            - Mention the specific destination in each point (if helpful for clarity)

            Example:
            Destinations: Amboseli, Lake Naivasha, Masai Mara

            Output:
            - Witness the Big Five and, if in season, the dramatic Great Migration in the Masai Mara.
            - Get a glimpse of the Masai Tribe and their traditions through a village visit.
            - Take a relaxing boat ride on Lake Naivasha to see hippos and diverse birdlife like fish eagles.
            - Walk among zebras, giraffes, and antelopes at Crescent Island Game Sanctuary.
            - Enjoy spectacular views of Mount Kilimanjaro at sunrise and sunset from Amboseli.
            - Spot lions, cheetahs, elephants, and buffalo on game drives through Amboseli’s wetlands and open plains. 
            
            '''
    else:
        background_info = f'''Given the following destination spots:
            {dest_one}, {dest_two}, {dest_three} and {dest_four} located at {country}

            Write 5–7 brief bullet points summarizing what a traveler can expect at these places.

            Each bullet should:
            - Be 1–2 lines
            - Focus on specific experiences or highlights (wildlife, landscapes, cultural experiences, activities, or iconic sights)
            - Use clear, engaging language (but avoid overuse of adjectives or fluff)
            - Mention the specific destination in each point (if helpful for clarity)

            Example:
            Destinations: Amboseli, Lake Naivasha, Masai Mara

            Output:
            - Witness the Big Five and, if in season, the dramatic Great Migration in the Masai Mara.
            - Get a glimpse of the Masai Tribe and their traditions through a village visit.
            - Take a relaxing boat ride on Lake Naivasha to see hippos and diverse birdlife like fish eagles.
            - Walk among zebras, giraffes, and antelopes at Crescent Island Game Sanctuary.
            - Enjoy spectacular views of Mount Kilimanjaro at sunrise and sunset from Amboseli.
            - Spot lions, cheetahs, elephants, and buffalo on game drives through Amboseli’s wetlands and open plains. 
            
            '''
    return background_info
