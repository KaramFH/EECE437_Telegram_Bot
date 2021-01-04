from enum import Enum

class VolunteerState(Enum):
    FREE = 1                    # volunteer is not assigned any task
    PENDING_ACK = 2 
    PENDING_PICKUP = 3            # volunteer has been assignedd a task
    PENDING_DELV = 4            # pending confirmation that deliviry has been made
    RESTING = 5                # volunteer has been assigned too many tasks and needs to rest