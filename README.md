# Collision Simulation

![Bounce Gif](.github/bounce.gif)

I wanted to simulate collisions between spheres to learn more about impulse and physical simulations. The simulation exports data to a `.csv` file and you can play it back in python. 
I did this because I didn't know how to show graphics in C++.

I used [The Lone Coder](https://www.youtube.com/watch?v=LPzyNOHY3A4)'s video to get the simulation up and running. 
The graphics part of the project was realised by a friend of mine who knows his way around TKinter way better than me.

### Usage

I included a default configuration file at `./config/data.setup`. To generate a different one, run `./show/setup.py` with `tkinter` installed. It will open a graphic dialog which should explain itself.

Then run `make` and the cpp simulation will create a `output.data` file which saves the movements of the objects in a `.csv` format.

To show the result run `./show/input.py` and first select the `data.setup` file and then the `output.data` file. It will open another tkinter window and will play back your simulation.