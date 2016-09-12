import os
import platform
import ntpath

# Get OS platform to determine the search path for Blender
my_os = os.name
my_platform_system = platform.system()
my_platform_release = platform.release()

# Test output the OS and release
print("You are running: " + my_platform_system + " " + my_platform_release)

# Read setting file to locate Blender's path and render output
from sys import argv
script, filename = argv
with open(filename) as f:
    my_settings = [line.rstrip('\n') for line in open(filename)]

# Show me the setting variables (remove these lines once script is running properly)
#print(my_settings[0]) # Blender.exe location
#print(my_settings[1]) # folder where Blender files to be rendered
#print(my_settings[2]) # folder where renders are outputted

# Create individual variables for each setting
my_blender_path = my_settings[0]
my_wip_path = my_settings[1]
my_render_output = my_settings[2]

# Get wip folder contents
my_render_files = os.listdir(my_settings[1])
for n in my_render_files:
    my_wip = my_wip_path + "\\" + n #Build the file path to blend files that will be rendered
    my_render_output_name = os.path.basename(os.path.splitext(my_wip)[0]) #Drops the .blend extension to use for naming the render output.
    #Build the string that will be executed for rendering in Blender (currently the .blend will render based on the file's default settings)
    #Future changes include frame range and file extension format.
    my_cli_command = '"' + my_blender_path + '"' + " -b " + my_wip + " -o " + my_render_output +"\\" + my_render_output_name + "_#### -F PNG -f 1"

    #Execute Blender without the UI to render the files in the rendering workspace folder (see my_settings[1] above)
    os.system(my_cli_command)
