# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Oscar Pan
- Email: oscar.pan04@login.cuny.edu

## final.architecture_evidence

My node is reactive because when there's no valid frontal distance being calculated at all, the decide_velocity() function will propose the command of stopping the motion of the robot. Additionally, in the case of the frontal distance being <= stop_distance also issuing the command to stop the motion of the robot, making the node reactive. A remapping and configuration of path systems after encountering a obstacle is needed to be included for the node to be a hybrid system.

## final.course_reflection

I think this activity shows me that maybe perhaps I'm into more of the robotic design and engineering type of work. These sorts of works are physical, and I can physically see and feel proud of the creation of whatever I have developed. Though I probably need to endure more on the repeated struggles of trials and errors which further my love-hate relationship with debugging. However, that doesn't mean that I'll undermine digital works and products that I will probably create. Regardless of what I am creating, I should always understand the practical need of the robots or anything in general that I am creating as the philosophy of the Human Center Design will probably be the most fundamental ideology that I need to take away from this experience as these are tools designed and developed for human. Hopefully in the future I will always have the human ethics in mind. 

## final.hardware_next

I would probably like to test how correctional command should function to hopefully develop like a hybrid system that'll react and replan its motions before using the behaviors on actual hardware. 

## final.middleware_debugging

The ROS graph could help me diagnose a command that never reaches the robot by allowing me to visually see the movement and action of the robot through the Gazebo Sim, and checking on the communication between the nodes to see the relationship of which nodes being the publishers or the subscribers to identify potential command issuing problem.

## final.system_synthesis

Robotics software is difficult because there's various different software components that have their individual role that they need to perform while communicating with other components to ensure that they'll work in harmonious tuning that will perform based on the designer's desired outcome. Currently, by using ROS 2 as a middleware, it allows the nodes, the computational units, to communicate with each other via topic which serves as a data transferring channel. For example, the /student_cmd_vel node serves as a computational unit that proposes driving commands to the robot, but needs to publish the proposal commands to the /course_cmd_vel_guard node first to be double checked before finalizing the proposed commands. Then, the /course_cmd_vel_guard published the commands to the /cmd_vel node where the driving commands are finalized which is when the robot will act upon the commands. There's also the /ros_gz_bridge node, whose publisher is the /cmd_vel node, that sends the driving commands inside the Gazebo Sim and the data collected by the robot's LiBAR sensors within Gazebo Sim is then sent out to the topics /scan and /odom outside the Gazebo Sim which then can be publish to /student_cmd_vel. Thus, creating a cycle of collecting data, decision-making, decision-making correction, and actions. Occasionally, some of the data being collected by the LiBAR sensors will be deemed invalid. In this case, /student_cmd_vel needs to propose a command to halt the movement of the robot because without valid information, it's problematic to allow the robot to continue motion as it could collide with the environment, or even in the case of threatening the surrounding people out of safety concerns when the robot is closing in their distance towards them. Even then, a proposal command correction is needed, like the /course_cmd_vel_guard, to check the proposed command to ensure the restriction of the robot's movement to ensure safety for itself and the people around it.  

## final.timing_evidence

The possibility of sensor-failure most affected my understanding of robot safety because it leads to additional consideration of the robot's decision-making system design in the case of failing to observe the environment or system failure in general. It's better to stop the robot's movement or a more careful and slow maneuver rather than taking the risk with unknown information especially when it concerns not only the safety of the robot but the people around it too. 

## mission_1.command_path_explanation

The proposed command is traveling from the /student_cmd_vel to /course_cmd_vel_guard to check the published commands before sending the finalized command to the /cmd_vel.


## mission_1.graph_explanation

A ROS2 graph shows a live map of the software components and how they interact with each other. For example, node /ros_gz_bridge uses the channel /scan to publish information to node /course_evidence_collector.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

I found 3.5, which represents the maximum range of the robot.

## mission_1.tools_explanation

Gazebo is responsible for simulating the environment and physics of the turtlebot3, including motions, walls, wheels, and sensor readings, while Rviz is responsible for visualizing the data from the turtlebot3 in Gazebo.

## mission_2.measurement_explanation

The estimated traveled path distance measurement differs from the start-to-end distance measurements because the odometry can't perfectly measure and adjust to curved motions.

## mission_2.modified_settings

{'linear_x': 0.15, 'angular_z': 0.8, 'duration': 4.0}

## mission_2.motion_comparison

In the rotation live simulation, the live motion result is almost as I initially predicted because  the start-to-end distance is 0m matching with my prediction of the robot remaining in the same position, and the 20 degrees change matched my expectation of the robot turning left.

## mission_2.prediction_locks

{'curve': '2026-09-12T00:28:28.817907+00:00', 'curve_modified': '2026-09-12T00:33:32.506748+00:00', 'rotation': '2026-09-12T00:15:22.988419+00:00', 'straight': '2026-09-11T23:30:21.408170+00:00'}

## mission_2.predictions

{'curve': 'I predict that the robot will move in a forward-right direction in an arc.', 'curve_modified': 'This path differs from the first curved trial because the robot will turn to the left due to the positive radian/s velocity, and a tighter curve due to the higher |turning speed|.', 'rotation': "The robot's position will remain in place, while its direction will shift 1.5 radians to the left.", 'straight': 'I predict that the robot will move forward 0.45m from its initial position.'}

## mission_2.safety_explanation

The command guard checks every proposed instruction to make sure that it's reasonable within the current context before finalizing the instruction to the robot. The final zero command stops both the robot's velocity and angular turning to flag the completion of the task. The stale-command timeout sends out a stop command to stop the robot after 0.5s if the robot is in motion with no new instructions being received due to either no communication or program crashes. 

## mission_3.data_to_command

The front_distance() function is responsible for finding the shortest valid frontal distance collected by the LiDAR by making sure that the angle of each of the collected distance is within the boundaries of the half width radians and is a positive finite number. Then, the decide_velocity() function will determine to stop the velocity completely if there's invalid distance or a valid distance is <= the stop_distance. Else, the forward speed will continue onward under the constraints of it being between 0.0m/s and 18.0m/s.  

## mission_3.missing_data_safety

The robot will stop when there's no valid front measurement because it's a safety measure for not only the robot itself, but also prevent the robot from potentially causing problems, collisions, and other issues due to lack of information that'll cause people to feel unsafe in the environment.

## mission_3.system_layers

The distance information collected by LiDAR is sent to the /student_cmd_vel through the /scan topic. /student_cmd_vel will utilize the collected distance to calculate the front distance and make the proposed command to the robot's velocity. The proposed command is sent from /student_cmd_vel to /course_ cmd_vel_guard to check the proposed command before sending the finalized velocity command decision to /cmd_vel.

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
