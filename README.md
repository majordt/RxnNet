# RxnNet
An AI framework for automated reaction mechanism discovery.

This is the repository of the Rxnnet program package developed by the Major group.
The code uses two external packages, which must be installed locally on your machine

1) xtb-dist (https://github.com/grimme-lab/xtb)

2) geodesic_interpolate (https://github.com/virtualzx-nad/geodesic-interpolate)

Before cloning this repository, you need to install Git LFS (https://git-lfs.com/)

Clone the repository:
git clone https://github.com/majordt/RxnNet.git

Add the following line to your .bashrc file
export MKL_THREADING_LAYER=GNU

To run the analysis on existing data, follow these steps:
./rxnnet --mode=analyze




