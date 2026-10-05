# mission_3 Submission

- Name: Oscar Pan
- Section: (not provided)

## Explanations

### technical_analysis

I predicted that less forward velocity and higher Kd control is needed to navigate around the pedestrian safely, otherwise the robot will endanger the pedestrian which matches up with the simulation testing. The next route point becomes a heading command by providing a series of sequential checkpoints to travel through which lead to a complete route from WP1 to WP2 and forth until the last WP4. PID control how the robot steers with Kp being how aggressive the route that the robot should follow through by, Kd being how the robot should slow down before making a sharper turn, and Ki being the last adjustment needed to correct prolong traversal error to be close to the drawn route as much as possible. Although the orange/odometry estimated path isn't displayed at all, I could predict that the inaccurate wheel radius, even with well-tuned PID controller, will follow the wrong physical path because the robot odometry estimates will be either underestimated or overestimated the position itself is in in regard to the routed path that it should follow.

### human_centered_analysis

The consequential failure for a pedestrian is most likely injuries or death. There's the safety and well regards to the pedestrians that needs consideration which requires the robot to slow down and proceed with caution, but at the cost of time to finish the assigned task. On the other hand, increasing speed will allow the task to finish faster but at the expense of safety to the pedestrians. Such difficult balancing decision is ultimately up to the responsibility of the robot's creator to make those decisions on the robot's behalf.