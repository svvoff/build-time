# build-time

scripts for calculating build time in xcode

it writes your build time into `log.csv` file

For working `start` and `end` scripts you should update path to `buildtime.py` in them.

Set `start` script in Start build phase
![Alamofire: Elegant Networking in Swift](https://raw.githubusercontent.com/svvoff/build-time/master/images/start.png)

And set `end` script in Succeeds phase
![Alamofire: Elegant Networking in Swift](https://raw.githubusercontent.com/svvoff/build-time/master/images/success_end.png)
and Fails phase
![Alamofire: Elegant Networking in Swift](https://raw.githubusercontent.com/svvoff/build-time/master/images/fail_end.png)

For ploting your build time result you should install `matplotlib` by executing command `pip install matplotlib`
If you doesn't have `pip` run `easy_install pip`

`python plot.py --input log.csv --product [your project or workspace file]` value for `--product` flag written in `product_name` field into `log.csv`