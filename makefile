laminas.png : Grafica.py Laminas.txt
	python3 Grafica.py
Laminas.txt : Monitas
	./Monitas>Laminas.txt
Monitas : Album.cpp
	c++ Album.cpp -o Monitas
