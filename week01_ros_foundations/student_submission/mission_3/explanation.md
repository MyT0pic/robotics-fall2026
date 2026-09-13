# Mission 3

## Data To Command

The front_distance() function is responsible for finding the shortest valid frontal distance collected by the LiDAR by making sure that the angle of each of the collected distance is within the boundaries of the half width radians and is a positive finite number. Then, the decide_velocity() function will determine to stop the velocity completely if there's invalid distance or a valid distance is <= the stop_distance. Else, the forward speed will continue onward under the constraints of it being between 0.0m/s and 18.0m/s.  

## Missing Data Safety

The robot will stop when there's no valid front measurement because it's a safety measure for not only the robot itself, but also prevent the robot from potentially causing problems, collisions, and other issues due to lack of information that'll cause people to feel unsafe in the environment.

## System Layers

The distance information collected by LiDAR is sent to the /student_cmd_vel through the /scan topic. /student_cmd_vel will utilize the collected distance to calculate the front distance and make the proposed command to the robot's velocity. The proposed command is sent from /student_cmd_vel to /course_ cmd_vel_guard to check the proposed command before sending the finalized velocity command decision to /cmd_vel.
