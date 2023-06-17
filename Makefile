install: venv
	. venv/bin/activate; pip3 install -Ur requirements.txt

venv :
	test -d venv || virtualenv -p python3 venv

clean:
	rm -rf venv
	find -iname "*.pyc" -delete

scenario1:
	python3 Scenario1.py

scenario1-sto:
	python3 Scenario1.py -stochastic	 

scenario2:
	python3 Scenario2.py

scenario2-sto:
	python3 Scenario2.py -stochastic

scenario3:
	python3 Scenario3.py

Scenario3-sto:
	python3 Scenario3.py -stochastic	 


