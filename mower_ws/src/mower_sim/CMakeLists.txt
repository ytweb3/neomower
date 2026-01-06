cmake_minimum_required(VERSION 3.8)
project(mower_sim)

find_package(ament_cmake REQUIRED)

# Install folders
install(DIRECTORY launch worlds models rviz
        DESTINATION share/${PROJECT_NAME})

ament_package()
