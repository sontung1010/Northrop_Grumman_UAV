from dronekit import connect


def ConnectToVehicle():
    # Connect to UDP endpoint.
    vehicle = connect('/dev/ttyTHS1',baud=57600,wait_ready=True)
    print('hello')
    return vehicle

def ConnectionTests(vehicle):
    #print firmware version
    print('Autopilot version: %s'%vehicle.version)
    # Use returned Vehicle object to query device state - e.g. to get the mode:
    print("Mode: %s" % vehicle.mode.name)
    # print mode
    print ("Mode: %s" % vehicle.mode.name)
    # print arming status
    print ("Armed: %s" % vehicle.armed)
    

    
plane = ConnectToVehicle()
ConnectionTests(plane)


