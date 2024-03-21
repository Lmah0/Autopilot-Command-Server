# MAVLink-Autopilot

Interoperability system for integration between custom Ground Control System and autonomous aerial vehicles with ArduPilot. Currently integrated and tested for quadcopter designs. Developed for Schulich Unmanned Aerial Vehicles at the University of Calgary.

### Operations
initialize.py - Establishes and verifies the connection to the vehicle.<br>
arm.py - Provides methods to arm and disarm the aerial vehicle.<br>
takeoff.py - Allows the vehicle to takeoff to a target altitude (relative to home altitude)<br>
mode.py - Switches flight modes<br>
waypoint.py - Flies to a specified waypoint relative to the current position, or through geo-coordinates<br>

### main.py - Simple terminal interface to trigger Autopilot commands.