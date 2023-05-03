# ScoutBot

Educational environment for developing a bipedal robot. ScoutBot is designed for research in robotics and control engineering with a focus on mono- and bipedal locomotion. The project currently uses mesh (`*.dae`) files from the [Xpp] [ROS2] package for the visualization of motion-plans for legged robots.

<p align="center">
<img align="right" src="https://codeberg.org/fesch/scoutbot/raw/branch/main/media/monoped.gif" />
</p>

## Index

- [Repository overview](repository-overview)
- [Install](#install)
- [Usage](#usage)
- [Feature matrix](#feature-matrix)
- [To Do](#to-do)

## Repository overview

- [`src`](src/): Location of [ROS2] code, organized as packages within folders:
  - [`bringup`](src/bringup/):  Hosts launch files.
  - [`description`](src/description/): Hosts mesh and description files.
  - [`gazebo`](src/description/): Hosts [Gazebo] files.
  - [`scripts`](src/scripts/): Scripts that improve the quality of life.

## Install

- Follow [this](https://github.com/FelixSchausberger/vscode_podman_ros2_workspace) setup to get [ROS2] with [VSCode] and [Podman] as your IDE.
- Clone this repository and open it in [VSCode] as a container.

## Usage

To launch the [Gazebo] simulation:

```shell
./src/scripts/clean_build.sh
ros2 launch bringup spawn_scoutbot.launch.py
```

## Feature matrix

| **Feature**   | **Description**     | **Monoped**        | **Biped**          | **ScoutBot** |
| :------------ | :------------------ | :----------------- | :----------------- | :----------- |
| [Gazebo]      | Spawns in [Gazebo]  | :heavy_check_mark: | :heavy_check_mark: | :x:          |
| Transmission  | Simulated actuators | :warning:          | :x:                | :x:          |
| [RViz]        | Shows in [RViz]     | :x:                | :x:                | :x:          |
| CAD (`*.dae`) | CAD model           | :heavy_check_mark: | :heavy_check_mark: | :x:          |

## To Do

1. Add transmissions to [Gazebo] simulation
1. Set up [RViz]
1. Work on mechanical setup (CAD)

[Gazebo]: https://gazebosim.org/home
[Podman]: https://podman.io
[ROS2]: http://www.ros.org
[RViz]: http://wiki.ros.org/rviz
[VSCode]: https://code.visualstudio.com/
[Xpp]: https://github.com/leggedrobotics/xpp
