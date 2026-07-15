# Context
1. This folder contains programming codes for a data visualization dashboard. Each markdown file following the format of `mhs-unitx-pointx-grading.md` contains programing codes that determine what is the color showing on the dashboard based on how a player performed at the specifc game point. Each markdown file also contains additional information regarding the game context descriptions as well as once the color returns yellow, what reasons caused it.
2. the order of the included markdown files should be unit1-point1, unit1-point2, ..., unit2-point1, ..., unit2-point7, ..., unit5-point4.
3. The game this dashboard based on or developed around with is in its development process, so it may keep updating to form a new build around a week, which may also change the color logic behind each progress point on the dashboard. The dashboard will read the trace data or log data collected from the game to determine the progress points' colors.
4. To determine whether we should chnage the programming codes behind each progress point, we need to create comprehensive testing program codes to test whether the codes of progress points returning the expected colors. And, if not, what might be the issue, like lacking key log records, the way to calculate the attempts is wrong, etc.
5. An example of the gameplay log records the dashbaord relies on is saved in a JSON file within the path of `./tests/05-01-26`. 

# Goal
1. Creating testing programs or functions to test each of the `mhs-unitx-pointx-grading.md` files, focusing on the production codes determining the colors (yellow or green) of the specific progress point, to see whether they returns the expected colors.
2. If the testing programs tested out returning the wrong color, then the testing programs will also test out the potential reasons, so that we can based on to modify the original color determination production codes.

# What you should do
1. Analyze each of the files following the name pattern of `mhs-unitx-pointx-grading.md`, finding the production codes determining the colors, and then creating testing programs in python to realize the two goals described in the Goal section, each included markdown file should have a python testing programs saved in one python file.
2. You can determine whether the production codes return the expected colors based on the JSON file saved in `tests/05-01-26` and also the expected colors saved in the following list - "Green, Green, Yellow, Green, Green, Yellow, Green, Green, Green, Green, Yellow, Green, Green, Yellow, Green, Green, Green, Green, Green, Green, Green, Green, Green, Green, Green, Green".
3. After the whole process, please creating a new markdown file to record the final results.