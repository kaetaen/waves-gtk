install:
	sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
	pip3 install pycairo
	pip3 install PyGObject

run:
	python3 src/main.py