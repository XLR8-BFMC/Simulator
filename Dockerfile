# Use ROS Noetic base image with Ubuntu 20.04 (Focal)
FROM ros:noetic-ros-core-focal

# Set environment variables for ROS and Gazebo
ENV DISPLAY=${DISPLAY}
ENV XDG_RUNTIME_DIR=/tmp/xdg
ENV WAYLAND_DISPLAY=wayland-0
ENV QT_X11_NO_MITSHM=1
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    ros-noetic-desktop-full \
    ros-noetic-gazebo-ros \
    ros-noetic-gazebo-ros-pkgs \
    ros-noetic-gazebo-ros-control \
    ros-noetic-robot-state-publisher \
    ros-noetic-joint-state-publisher \
    ros-noetic-joint-state-publisher-gui \
    ros-noetic-rqt \
    ros-noetic-rqt-common-plugins \
    ros-noetic-xacro \
    gazebo11 \
    python3-pip \
    python3-rosdep \
    python3-rosinstall \
    python3-rosinstall-generator \
    python3-wstool \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Initialize and update rosdep
RUN rosdep init && rosdep update && rosdep fix-permissions && rosdep update 


# Set working directory
VOLUME /Simulator
VOLUME /shared

WORKDIR /Simulator

# Source ROS setup scripts on container startup
CMD ["bash", "-c", "source /opt/ros/noetic/setup.bash && cd /Simulator && catkin_make && source devel/setup.bash && export DISPLAY=${DISPLAY} && export GAZEBO_IP=127.0.0.1 && export GAZEBO_PLUGIN_PATH=/usr/lib/gazebo-11/plugins && exec bash"]

