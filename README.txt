To create a virtual environment:
cd to working directory in terminal
Enter "make" in terminal

IMPORTANT NOTE:
This make file will only work when running on Ubuntu
If you want to run this on Mac change:

	"test -d venv || virtualenv -p python3 venv"
To:

	"test -d venv || python3 -m venv venv"

To run you must activate your virtual environment in working directory:
	source ./venv/bin/activate

2 example runs are included for each Scenario:

In working directory(after environment has been created) enter

make run: runs Scenario1.py with no flag and saves an image of the best/last run.
         
make run2: runs Scenario1.py with the '-stocastic' flag and saves an image of the best/last run.

make run3: runs Scenario2.py with no flag and saves an image of the best/last run.

make run4: runs Scenario2.py with the '-stocastic' flag and saves an image of the best/last run.

make run5: runs Scenario3.py with no flag and saves an image of the best/last run.
         
make run6: runs Scenario3.py with the '-stocastic' flag and saves an image of the best/last run.

Make clean: removes virtual environment

Scenario 1-takes about 0.5 seconds to run on my PC whereas it takes about 2 seconds to run on nightmare

Scenario 2-takes about 123 seconds to run on my PC whereas it takes about 303 seconds to run on nightmare

Scenario 3-takes about 0.3 seconds to run on my PC whereas it takes about 3 seconds to run on nightmare