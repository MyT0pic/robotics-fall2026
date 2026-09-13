# Mission 1

## Command Path Explanation

The proposed command is traveling from the /student_cmd_vel to /course_cmd_vel_guard to check the published commands before sending the finalized command to the /cmd_vel.


## Graph Explanation

A ROS2 graph shows a live map of the software components and how they interact with each other. For example, node /ros_gz_bridge uses the channel /scan to publish information to node /course_evidence_collector.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found 3.5, which represents the maximum range of the robot.

## Tools Explanation

Gazebo is responsible for simulating the environment and physics of the turtlebot3, including motions, walls, wheels, and sensor readings, while Rviz is responsible for visualizing the data from the turtlebot3 in Gazebo.
