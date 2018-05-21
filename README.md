Some basic python stuff for programming meeting. Will need to have some things installed to work. 

Install python (not 3.0):
https://www.python.org/downloads/

#BioPython install: 
http://biopython.org/DIST/docs/install/Installation.html

Some BioPython install notes (linux)

1. install numpy

sudo apt-get install python-pip #linux installer

sudo pip install cython

2. clone numpy git repo

git clone git://github.com/numpy/numpy.git numpy

cd numpy

3. install numpy (need a C compiler)

python setup.py build

sudo python setup.py install

4. pull latest release (or navigate to site and download)

wget http://biopython.org/DIST/biopython-1.66.tar.gz

5. unzip

tar xzf biopython-1.66.tar.gz

cd biopython-1.66/

6. install

sudo python setup.py install

#Pandas install: 
http://pandas.pydata.org/pandas-docs/stable/install.html

1. how to with pip

sudo pip install pandas

#IPython install: 
http://ipython.org/install.html
