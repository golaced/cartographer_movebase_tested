google_binary(cartographer_flat_world_imu_node
  USES_ROS
  SRCS
    flat_world_imu_node_main.cc
)

install(TARGETS cartographer_flat_world_imu_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
