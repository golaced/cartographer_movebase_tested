cmake_minimum_required(VERSION 2.8.3)
project(bb8_slam_zhou)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  tf
  sensor_msgs
  nav_msgs
  geometry_msgs
)


################################################
## Declare ROS messages, services and actions ##
################################################

## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

 generate_messages(
   DEPENDENCIES
   std_msgs  # Or other packages containing msgs
 )


###################################
## catkin specific configuration ##
###################################
catkin_package(
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)


add_executable(foot_print src/foot_print.cpp)
target_link_libraries(foot_print ${catkin_LIBRARIES})
add_dependencies(foot_print bb8_slam_zhou_generate_messages_cpp)



#############
## Install ##
#############


install(TARGETS foot_print
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 ) 


install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)


install(DIRECTORY src 
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY configuration_files 
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

#############
## Testing ##
#############
