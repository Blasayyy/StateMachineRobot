# StateMachine Robot Project

## Overview

This project, conducted as a part of our "Objets connectés" (Connected Objects) course, is a Python-based application designed around the concept of state machines. It's composed of two main parts: the development of a versatile state machine library and its application in controlling a GoPiGo3 robot.

## Part 1: State Machine Library

The first half of the project involved creating a generic library that implements a state machine. The library includes:

  -FiniteStateMachine: This class handles the management of states and transitions that developers can incorporate into it, in addition to managing the main loop or tick of the state.
  
  -ActionState: Each state inheriting from this class can accept callable objects for its entering, in-state, and exiting actions, which will be executed by the FiniteStateMachine.
  
  -Transition Classes: These facilitate state-to-state changes and can handle different conditions for transitioning.
  
  -Blinker: A generic class to manage any required blink mechanism. This class inherits from FiniteStateMachine.
  
The goal was to design a library flexible enough to be utilized in any program requiring a state machine.

## Part 2: GoPiGo3 Robot Integration

The second half of the project centered around the integration of the state machine library into the operation of GoPiGo3 robots. It involved:

  -Robot Initialization/Startup: A sequence of states and transitions to initialize and start the robot.

  -Home State: This state listens for remote control input to trigger different tasks.

  -Robot Tasks (task1, task2): Two tasks that the robot can perform using the state machine library. Task 1 takes input from the remote control to move the robot through its motors, and blink its headlights           accordingly. Task 2 simply moves the robot around and takes the input from the built-in depth sensor to stop it when it is close to objects in front of it. 

  -Robot Class: A class to manage the robot's components.

  -StateMachine Class (C64Proj): This class manages the entire program.

## Getting Started

Follow these steps to run the program on the GoPiGo3 robot:

1. Connect to the Robot: Connect your device to the robot using Wi-Fi.
2. Access the Robot's User Interface: Open a web browser and navigate to 10.10.10.10 to access the robot's user interface.
3. Open Jupyter Python: On the robot's user interface, click on the Jupyter Python option.
4. Upload Project Files: Download the files from the code folder in this repository and copy them into the robot's directory.
5. Run the Program: Finally, execute the main.py file to start the program.
