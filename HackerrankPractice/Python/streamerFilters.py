# Streamers 
# Python Program 

# As a Twitch user, you want to be able to filter the available streams by category to find content that is more fitting for you
# Create a system that will filter streamers by two given categories
# There is no preferred coding languange for submission 

# Input: ["Streamer1-StreamLanguage1-StreamContent1","Streamer2-StreamLanguage2-StreamContent2","Streamer3-StreamLanguage1-StreamContent2"]

# If prompted to filterBy(SteamLanguage1,StreamContent1) -> return [Streamer1] 
# If prompted to filterBy(StreamLanguage1, null) -> return [Streamer1, Streamer3] 

# The input to filterBy() is of the following types:
# input ->list[string] with each index being of the form: "streamer1-language-category"
# language -> string
# category -> string

# If no streamers are available based on the filter, return the a list with the "null" string as: ["null"] 

# Sample case 
# Arguments
# pokimane-English-Valorant,Dream-English-Minecraft,k4sen-Japanese-League of Legends,tommyinnit-English-Minecraft,QTCinderella-English-Just Chatting, English, Minecraft

# Expected output 
# Dream, tommyinnit

# Code in python 

def filterBy(input, language, category): 

    # Test printing the contents of input 
    # print("The contents of input are ", input)

    # Test printing the contents of language
    # print("The contents of language are ", language)

    # Test printing the contents of category 
    # print("The contents of category are ", category)

    # Need an empty list to store the results of the filter
    filtered = []

    # Cycling through the elements in the list received as parameter
    for streamer in input: 

        # Separating the input string into 3 components - streamername (s), language (lang) and category (cat)
        # Using the - as the marker for separation 
        s, lang, cat = streamer.split('-')

        # If the language is None or the language received matches the contents of lang 
        # AND 
        # If the category is None of the category received matches the contents of cat 
        if (language is None or lang == language) and (category is None or cat == category): 

            # We add the current streamer's name to our list 
            filtered.append(s)

            # Test print the contents of filtered 
            # print("The contents of filtered are ", filtered)

    # Return the filtered list of streamers 
    return filtered

if __name__ == '__main__':

    input_streamers = ["pokimane-English-Valorant", "Dream-English-Minecraft", "k4sen-Japanese-League of Legends", "tommyinnit-English-Minecraft", "QTCinderella-English-Just Chatting"]

    print(filterBy(input_streamers, "English", "Minecraft")) 

    print(filterBy(input_streamers, "Japanese", "League of Legends")) 
