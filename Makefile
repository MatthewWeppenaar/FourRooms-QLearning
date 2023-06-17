install: venv
	. venv/bin/activate; pip3 install -Ur requirements.txt

venv :
	test -d venv || virtualenv -p python3 venv

clean:
	rm -rf venv
	find -iname "*.pyc" -delete

run:
	python3 Scenario1.py

run2:
	python3 Scenario1.py -stochastic	 

run3:
	python3 Scenario2.py

run4:
	python3 Scenario2.py -stochastic

run5:
	python3 Scenario3.py

run6:
	python3 Scenario3.py -stochastic	 


