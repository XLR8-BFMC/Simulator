#!/usr/bin/env python3

# Copyright (c) 2019, Bosch Engineering Center Cluj and BFMC organizers
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE


import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import os
import base64

class CameraHandler():
    # ===================================== INIT==========================================
    def __init__(self):
        """
        Creates a bridge for converting the image from Gazebo image intro OpenCv image
        """
        self.bridge = CvBridge()
        self.cv_image = np.zeros((1080 , 1920))
        rospy.init_node('CAMnod', anonymous=True)
        self.image_sub = rospy.Subscriber("/automobile/camera/camera_follow/image_raw", Image, self.callback)
        self.fifo = '/shared/capture_pipe'
        if not os.path.exists(self.fifo):
                os.mkfifo(self.fifo) 
        rospy.spin()

    def callback(self, data):
        try:
            """
            :param data: sensor_msg array containing the image in the Gazsbo format
            :return: nothing but sets [cv_image] to the usefull image that can be use in opencv (numpy array)
            """
            self.cv_image = self.bridge.imgmsg_to_cv2(data, "rgb8")
            _, encoded_image = cv2.imencode(".jpg", self.cv_image)
            image_bytes = encoded_image.tobytes()
            with open(self.fifo, "wb") as pipe:
                pipe.write(len(image_bytes).to_bytes(4, byteorder="big"))  # Send image size
                pipe.write(image_bytes)  # Send image data
                pipe.flush()
        except BrokenPipeError:
            rospy.logwarn("Broken pipe! No reader available.")
        except Exception as e:
            rospy.logerr(f"Error processing image: {e}")
            

        
            
if __name__ == '__main__':
    try:
        nod = CameraHandler()
    except rospy.ROSInterruptException:
        pass