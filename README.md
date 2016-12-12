# cartographer_turtlebot_movebase
using google cartorprapher to mapping , using move_base to navigation. control turtlebot to mapping while navigation . 


##instlal
    mkdir -p catkin_ws/src
    cd src
    git clone https://github.com/zhoujoey/cartographer_turtlebot_movebase.git
    cd ../
    catkin_make_isolated --install --use-ninja
    
##hardware
robot:  turtlebot2
lidar:  hokuyo 

##run
> source install_isolated/setup.bash

> turtlebot_navigation hokuyo_carto_turtlebot_test.launch
 

##changed files
1. /src/cartographer_turtlebot/cartographer_turtlebot/launch/
2. /src/cartographer_turtlebot/cartographer_turtlebot/configuration_files/
3. /src/turtlebot/turtlebot_navigation/src/foot_print.py
4. /src/turtlebot/turtlebot_navigation/launch/
5. /src/turtlebot/turtlebot_navigation/carto_nav_turtlebot.rviz

##use dev branck to develop newer funtion

##important modified history

###20161207
add kinect_follow_with_lidar_mapping.launch in /turtlebot/turtlebot_follower
> to make turtlebot mapping and following , use kinect to follow people, use hokuyo lidar to mapping with cartographer. 

add turtlebot_hokuyo_back.launch in /cartographer_turtlebot/
> to let hokuyo lidar fixed in the back of turtlebot and publish its tf .

####test git ssh 
