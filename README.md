# Web VR environment for simulating chemical reaction

## [Simulation Youtube Video Link](https://youtu.be/LcMCMsXlwF0?si=d1AX52LC8tG824wi)

## Structure of the project
<img width="1164" alt="Screen Shot 2023-01-18 at 10 32 21 PM" src="https://user-images.githubusercontent.com/96154184/213371939-861c0bc8-9fc8-4cd5-b47e-f461a7e2463d.png">

## Installation guide
1. Clone this code to the local device
2. Open clonded repostitory in visual studio code or terminal
3. If flask is not installed, run command "pip install Flask". If pip is not installed,
run "python -m ensure pip -upgrade" and "python get-pip.py"
4. After installing all the required module, run "python3 view.py" or "python view.py"
5. Copy and paste the link that appears to the web browser or press ctrl and click the link

## Implemented Skills
Python Flask (view.py): This enables to build development server to display our web vr environment and connect it to 
our back ground simulation code(Data-ph.py).

JavaScript (functions.js): This functions in Javascript enables VR environment to change/react according to the user's action 
which increases user interactivity. All the api call to our flask web server is made under Javascript and other features such as slider,
graph trend visibility, input table, etc. communicate with the server through Javascript.

HTML/A-frame(input.html, index.html): This part work as the frontend of this porject. Input page is displayed to get the anticiapted
ph measure, molecules, etc. from the user and guid the user to the web vr environment. All the frontend part was done through html using
html library called A-frame.
