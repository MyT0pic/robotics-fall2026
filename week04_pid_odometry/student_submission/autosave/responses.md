# Autosaved responses

- Name: Oscar Pan
- Student ID: 24344304 & oscar.pan04@login.cuny.edu
- Section: (not provided)

## Check-in answers

### background_compare

The human engineers are responsible for tuning and setting the Kp, Kd, and Ki to find the acceptable intensity of any of those 3 variables in a PID controller depending of the task that the robot is supposed to be performing. This makes a PID a feedback controller because the human engineers can test the state of the PID controller through actual physical experimentation to adjust any of the Kp, Kd, and Ki to balance between accuracy, reliability and trust in regard to the robot's design.

### background_social

For example, a heater, if the tuning of the controller is too aggressive then it's possible that the heat generated will be way too much which might potentially waste unnecessary fuel source, degrading/melting the heater itself, and causing heatstroke to anyone in the environment. On the other hand, if the controller is way too cautiously, the heat generation might be too slow causing the surrounding temperature to remain the same which can cause people who need heat on demand to suffer hypothermia in a cold environment.

### odom_background_wheels

None

### m1_prediction

With too little Kp, I predict that the arm will slowly or maybe not even able to raise the arm at all to a certain position. Additionally, if the Kd is too low, then the arm will not be able to slowly come to a rest or hold onto a specific position with the elbow oscillating around a position.

### m1_arm_tuning

For both the shoulder and elbow controllers, the Kp is decreased to 1.1 and Kd is decreased to 0.5. Based on the visual, the shoulder joint constantly overshoots and undershoots in its oscillations which matches with my initial prediction of oscillation movement of the arm. As for the elbow joint, it also exhibits the same behavior as predicted. The gravity compensation seems to make the Kp and Kd component of the PID controller a lot more aggressive.

### final_reflection

This lab makes me reflect upon the ethical responsibility that I have as a robotic designer and creator. Every single decision that the robots made are also decision that I made too, since it's purposefully designed in a way that I would've act upon but it's on the hand of a robot. I'm not too sure about myself, but the ethical responsibility and decision-making that robots do will put immense pressure on me. Not too sure if the possible guilt that I'll develop will dissuade upon me or motivate me more to be more ethically thorough when designing and tuning the PID controller for example. The mathematical aspect of the PID controller really sticks to me probably because of how mathematically sense each of the p, i & d component of the equation is and how it works. I just love seeing how more math is applied to robotics in the future or other creation of things in the computer science field.

## Mission explanations

### mission_1

**prediction**: With too little Kp, I predict that the arm will slowly or maybe not even able to raise the arm at all to a certain position. Additionally, if the Kd is too low, then the arm will not be able to slowly come to a rest or hold onto a specific position with the elbow oscillating around a position.

**tuning_analysis**: For both the shoulder and elbow controllers, the Kp is decreased to 1.1 and Kd is decreased to 0.5. Based on the visual, the shoulder joint constantly overshoots and undershoots in its oscillations which matches with my initial prediction of oscillation movement of the arm. As for the elbow joint, it also exhibits the same behavior as predicted. The gravity compensation seems to make the Kp and Kd component of the PID controller a lot more aggressive.
