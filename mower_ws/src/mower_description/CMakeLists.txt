cmake_minimum_required(VERSION 3.8)
project(mower_description)

find_package(ament_cmake REQUIRED)

# Install URDF, meshes, and config files
install(
  DIRECTORY urdf meshes launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
