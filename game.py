################################################################################
# This script will handle starting ROS if it is not started yet,
# pulling the images from the camera in order to run CV
# on it (from the ../cv/ folder), and executing move commands on the UR5
################################################################################

# This constant will be used to convert aruco coords into ur5 coords
GLOBAL_OFFSET = (0,0,0,0)
CAM_LOCATION = (0,0,0,0)
class Block:
    aruco_coords = (0,0,0,0)
    ur5_coords = (0,0,0,0)
    id_number = -1

# Takes in the coordinates for a chosen aruco tag and turns it into UR5 coordinates
def change_coordinate_space(aruco_coords):
    return aruco_coords += GLOBAL_OFFSET

# Returns an image from ROS
def get_image():
    #todo this

def return_to_cam():
    #return the UR5 to the camera sensing location

def get_game_state():
    
def execute_move(block):
    #todo execute move
    return_to_cam()

# Starts ROS server if not started, initializes robot and game state
def main():
    return_to_cam()
    #   todo initial setup
    get_game_state()
    # todo choose block to pick
    picked_block = 0
    execute_move(0)
