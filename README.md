<img src="https://github.com/ECC-BFMC/Simulator/blob/main/Picture1.png" width=30% height=30%>

# BFMC Simulator Project

The project contains the entire Gazebo simulator. 
- It can also be used to get a better overview of how the competition is environment looks like
- It can be used in to develop the vehicle state machine
- It can be used to simulate the path planning
- It can be used to set-up a configuration procedure for the real track
- Not suggested for image processing
- Try not to fall in the "continuous simulator developing" trap

Tips on how to install and work on it, can be found in the 


## The documentation is available in details here:
[Documentation](https://bosch-future-mobility-challenge-documentation.readthedocs-hosted.com/data/simulator.html)


## Camera settings 
the launch script is ```roslaunch sim_pkg map_with_car_REC.launch ``` but only from the Simulator folder after sourcing devel/setup.bash 

to start the posting of camera images outside the sim  ```rosrun example camera.py```
to start the reciving of actions inside the sim  ```rosrun example control.py``` 

file for camera settings is located in the following path:<br>
[camera on the car](/catkin_ws/Simulator/src/models_pkg/camera_follow/model.sdf)

[cam above](catkin_ws/Simulator/src/models_pkg/cam_birdeye_REC/model.sdf) <br>
[position of the car in the sim](catkin_ws/Simulator/src/sim_pkg/launch/sublaunchers/car_REC.launch) <br>

