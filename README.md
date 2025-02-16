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

## Docker setup 
```docker build -t ros_noetic_simulator .```  This build the image with every needed dependency <br>
```docker run --name simulator_container --env="DISPLAY=$DISPLAY" --env="QT_X11_NO_MITSHM=1" --env="XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR" --env="WAYLAND_DISPLAY=$WAYLAND_DISPLAY" --volume="$PWD/Simulator:/Simulator" --volume="$PWD/shared:/shared" --volume="/tmp/.X11-unix:/tmp/.X11-unix" --net=host --privileged -it ros_noetic_simulator bash``` <br>

THIS MONSTER OF A COMMAND WILL RUN THE CONTAINER WITH THE SIMULATOR INSIDE IT.<br>

## run script
the launch script is ```roslaunch sim_pkg map_with_car_REC.launch ``` but only from the Simulator folder after sourcing devel/setup.bash<br>

to start the posting of camera images outside the sim  ```rosrun example camera.py``` <br>
to start the reciving of actions inside the sim  ```rosrun example control.py``` 
## Camera settings
file for camera settings is located in the following path:<br>
[camera on the car](src/models_pkg/camera_follow/model.sdf)

[cam above](src/models_pkg/cam_birdeye_REC/model.sdf) <br>
[position of the car in the sim](src/sim_pkg/launch/sublaunchers/car_REC.launch) <br>

