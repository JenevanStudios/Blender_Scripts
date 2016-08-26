cls
@echo off
title Blender Cycle Command Render

REM This batch file copies the supplied Blender file and begins to render the image
REM example run: C:\Temp\test.bat E:\Temp\LightingFundamentals_bedroom_start\LightingFundamentals_bedroom_start.blend E:\Temp\Render\

REM Set the location of the blender executable
REM This needs to change to an argument or a global variable
Set blender_run_loc=D:\Program Files\Blender Foundation\Blender

REM Set the command line arguments blender file location and the render temp space
SET blender_file_loc=%1
SET render_loc= %2

REM Get file name from given path
For %%A in ("%blender_file_loc%") do (
REM    Set Folder=%%~dpA
    Set blend_name=%%~nxA
)

REM copy the Blender file that will be rendered to the temp render space.
xcopy /v /y %blender_file_loc% %render_loc%

REM new filename
SET blender_file_to_render=%render_loc%\%blend_name%


REM Move the working directory to the local Blender install location 
REM I will have to change this to a global variable to set a more common location
CD /D %blender_run_loc%

REM Start Blender and render the file
REM This line needs some fine tuning
start /d "%blender_run_loc%" blender.exe -b %blender_file_to_render% -o %render_loc%render_output_#### -F PNG -f 1

REM Cleanup
del %blender_file_to_render%

REM Close batch
exit