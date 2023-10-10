# Showroom 
# Python Program 
# List comprehension practice 

# As a lion trainer, you are taking part in an international lion exhibition
# During the event lions from different teams enter and exit the showroom where lion experts can inspect and score them 
# Lions do not enter the showroom all at once, as that would cause too much commotion
# The organizers of the event are letting them in and out based on a predefined schedule 
# Before the show starts you get access to the schedule for your lions - but not for the others
# Nevertheless, during the show, you can observe all lions getting in and out of the room 
# Based on your experience, you believe that the judges tend to award the biggest lios in the room with the highest scores
# Before the final results are out, you want to estimate your chances of winning this competition 

# Requirements
# Complete the following functions 

# The LionCompetition class constructor that accepts lion descriptions and the private schedule of when the lions enter and exit the showroom 

# The lionEntered and lionLeft functions that are called whenever a new lion enters of leaves the room 

# The GetBiggestLions function that, for the current time, returns a list of our lions in the room that are at least as big as the biggest lion from competing teams in the room 
# The presented list has to be sorted alphabetically 

# Function definitions 
# LionCompetition class constructor parameters 
# lions is the list or elements describing your lions 
# name - string representing a name of the lion 
# height - height of the lion 

# schedule is a private schedule of when your lions enter and leave the show room 
# name - string representing a name of a lion 
# enterTime - number of minutes since the start of the show when the lion will enter the room 
# exitTime - number of minutes since the start of the show when the lion will exit the room 

# lionEntered function parameters 
# currentTime is the number of minutes since the start of the show 
# height is the height of the lion that entered the room 

# lionLeft function parameters 
# currentTime is the number of minutes since the start of the show 
# height is the height of the lion that left the room 

# Constraints 
# Subsequent invocations of lionLeft and lionEntered functions are always called in order, according to the currentTime parameter 

# The schedule is strictly followed - your lions enter and exit the room exactly as specified times 

# The lions inspection (invocation of the getBiggestLions functions) takes place wither before or after all lions scheduled to enter or leave the room at a given minute did that - never in between 

# Lion names are unique 

# Times 
# (currentTime, enterTime and exitTime) are always whole numbers (and multiple events can occur at the same time) 

# A single lion enters the room only once during the show 

# Sample case
# definition marry 300
# definition rob 250
# schedule marry 10 15
# schedule rob 13 20
# start 
# 8 enter 200 
# 10 enter 310
# 10 enter 300
# 11 inspect 
# 13 enter 250
# 13 exit 310
# 13 inspect
# 15 exit 300
# 16 inspect 
# 16 exit 200
# 20 exit 250
# 21 end 

# Sample output 
# 0
# 2 marry rob
# 1 rob

# Explanation 
# We have two lions 
# marry with a height of 300cm that enters the show 10 minutes after its start and exits it 15 minutes after its start 
# rob with a height of 250cm that enters the show 13 minutes after its start and exits it 20 minutes afters its start 
 
# The show goes as follows 
# 8 minutes after the start of the show a lion with a height of 200cm enters the room - based on the schedule it is not one of ours 

# 10 minutesafter the start of the show two lions enter the room: a 310cm one and a 300cm one. The second one is marry 

# We do an inspection. Both marry and rob are higher than the 200cm height lion that entered the room at the 8th minutes of the show, so we return both names 

# 16 minutes after the start of the show marry leaves the room 

# We do an inspection, rob is still the biggest lion in the room 

# 16 and 20 minutes after the start of the show both remaining lions exit the room 

from dataclasses import dataclass

# LionDescription class that has the name and height of a lion
@dataclass
class LionDescription:
    
    # String variable to store a lion's name
    name: str

    # Integer variable to store a lion's height
    height: int

# LionSchedule class that has the name, entry time and exit time onto a stage for a lion
@dataclass
class LionSchedule:

    # String variable to store a lion's name
    name: str

    # Integer variable to store the time a lion enters the stage after the competition starts
    enter_time: int

    # Integer variable to store the time a lion exits the stage after the competition starts 
    exit_time: int

# LionCompetition class 
class LionCompetition:

    # Constructor function 
    # Takes in as parameters the list of the LionDescription as lions and the list of LionSchedule as schedule
    # It allows us to create instances of lions that have two attributes name and height
    # It allows us to create 
    def __init__(self, lions: list[LionDescription], schedule: list[LionSchedule]):

        # The self.our_lions will have the values of name from lion and height from lion for each lion in the lions list 
        # Creating a dictionary with our lion's name as keys and heights as their values
        self.our_lions = {lion.name: lion.height for lion in lions}

        # Creating a dictionary to keep track of our lions that are in the showroom 
        self.lions_in_showroom = {}

        # Creating a list of the heights of other lions in the showroom
        self.other_lions_heights = []

        # Creating a dictionary with the schedules of our lions
        self.schedule = {s.name: (s.enter_time, s.exit_time) for s in schedule}

    # Instance method lion_entered 
    # Takes self, current_time and height as parameters
    def lion_entered(self, current_time: int, height: int):

        # Check if the height of the lion that entered the showroom is if it matches then we know it's one of our lions
        # If it's one of our lions
        if height in self.our_lions.values():

            # Cycle through our lions to identify which of our lions was the one that entered the showroom
            for name, h in self.our_lions.items():

                # If the value of h matches the height of a lion, we found our lion who entered the showroom 
                if h == height:

                    # Now we add the lion to our dictionary lions_in_showroom 
                    # We use the lion's height as the key and its name as the value 

                    self.lions_in_showroom[height] = name

        # Otherwise, we know that the lion that entered wasn't ours    
        else:

            # We sore that lion's height in our list other_lions_heights
            self.other_lions_heights.append(height)

    # Instance method lion_left
    # Takes self, current_time and height as parameters
    def lion_left(self, current_time: int, height: int):
        
        # Check if a lion with the given height that is currently in the showroom is one of ours
        if height in self.lions_in_showroom:
            
            # Removing the lion so it's not considered as in the showroom
            del self.lions_in_showroom[height]
        
        # Otherwise, if the lion isn't one of ours 
        else:
            
            # We remove the height from the other_lions_heights so that it's not considered to be in the showroom
            self.other_lions_heights.remove(height)

    # Instance method get_biggest_lions
    # Will check which of the lions in the showroom is the biggest 
    def get_biggest_lions(self) -> list[str]:

        # Calculating which of the lions from the other teams is the biggest in the showroom 
        # If there's no other lions in the showroom, it's going to default to 0 as a fallback 
        biggest_other_lion_height = max(self.other_lions_heights, default=0)

        # No we need to check which of our lions is taller than or equal to the talles lion from the other team
        # # List comprehension 
        # For each height (h) and name (name) pair in our lions_in_showroom dictionary we check if our lion's height (h) 
        # is greater than or equal to the biggest_other_lion_height 
        eligible_lions = [name for h, name in self.lions_in_showroom.items() if h >= biggest_other_lion_height]

        # Now we return the names of our eligible_lions sorted alphabetically 
        return sorted(eligible_lions)

#
if __name__ == "__main__":

    # 
    lions = [LionDescription("marry", 300), LionDescription("rob", 250)]

    #
    schedules = [LionSchedule("marry", 10, 15), LionSchedule("rob", 13, 20)]

    #
    competition = LionCompetition(lions, schedules)

    # Events
    events = [
        (8, "enter", 200),
        (10, "enter", 310),
        (10, "enter", 300),
        (11, "inspect"),
        (13, "enter", 250),
        (13, "exit", 310),
        (13, "inspect"),
        (15, "exit", 300),
        (16, "inspect"),
        (16, "exit", 200),
        (20, "exit", 250),
        (21, "end")
    ]

    # Processing the events
    for event in events:

        time, action, *args = event

        if action == "enter":

            competition.lion_entered(time, args[0])

        elif action == "exit":

            competition.lion_left(time, args[0])

        elif action == "inspect":

            lions = competition.get_biggest_lions()
            
            # print(len(lions), *lions)
            print(len(lions), ' '.join(lions))

    # import sys

    # read_line = lambda: sys.stdin.readline().split()

    # descriptions: list[LionDescription] = []
    # lion_schedule: list[LionSchedule] = []

    # parse = True
    # while parse:
    #     line = read_line()
    #     if line[0] == 'definition':
    #         name = line[1]
    #         size = int(line[2])
    #         description = LionDescription(name, size)
    #         descriptions.append(description)
    #     elif line[0] == 'schedule':
    #         name = line[1]
    #         enter_time = int(line[2])
    #         exit_time = int(line[3])
    #         schedule_entry = LionSchedule(name, enter_time, exit_time)
    #         lion_schedule.append(schedule_entry)
    #     elif line[0] == 'start':
    #         parse = False
    #     else:
    #         raise Exception('invalid input')

    # lion_competition = LionCompetition(descriptions, lion_schedule)
    # parse = True
    # while parse:
    #     line = read_line()
    #     time = int(line[0])
    #     if line[1] == 'enter':
    #         size = int(line[2])
    #         lion_competition.lion_entered(time, size)
    #     elif line[1] == 'exit':
    #         size = int(line[2])
    #         lion_competition.lion_left(time, size)
    #     elif line[1] == 'inspect':
    #         biggest_lions = lion_competition.get_biggest_lions()
    #         print(len(biggest_lions), end='')
    #         for lion in biggest_lions:
    #             print(" " + lion, end='')
    #         print()
    #     elif line[1] == 'end':
    #         parse = False
    #     else:
    #         raise Exception('invalid input')

 