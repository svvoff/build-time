# build-time

scripts for calculating build time in xcode

it writes your build time into `build_time.csv` file

Set `starty.py` script in Start build phase
![start script run](https://raw.githubusercontent.com/svvoff/build-time/master/images/start.png)

And set `success.py` script in Succeeds phase
![success script run](https://raw.githubusercontent.com/svvoff/build-time/master/images/success_end.png)

And set `fail.py` script in  Fails phase
![fail script run](https://raw.githubusercontent.com/svvoff/build-time/master/images/fail_end.png)

For ploting your build time result you should install `matplotlib` by executing command `pip install -r required.txt`

`python plot.py --project [your project or workspace file]` value for `--project` flag written in `project_name` field into `build_time.csv`

![plot example](https://raw.githubusercontent.com/svvoff/build-time/master/images/figure_example.png)
On plot you will see three lines:
- blue - is common build time
- green - success build time
- red - failed build time