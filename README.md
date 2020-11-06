# metagraph-cogdl
A collection of metagraph plugins using CogDL

To install, run the following:

```
conda env create
conda activate mgcogdl

pip install torch==1.4.0
export CUDA=cu101
pip install torch-scatter==latest+${CUDA} -f https://pytorch-geometric.com/whl/torch-1.4.0.html
pip install torch-sparse==latest+${CUDA} -f https://pytorch-geometric.com/whl/torch-1.4.0.html
pip install torch-cluster==latest+${CUDA} -f https://pytorch-geometric.com/whl/torch-1.4.0.html
pip install torch-spline-conv==latest+${CUDA} -f https://pytorch-geometric.com/whl/torch-1.4.0.html
pip install torch-geometric
pip install dgl-cu101
git clone https://github.com/THUDM/cogdl.git
cd cogdl
pip install -e .
cd ..

pre-commit install
python setup.py develop
```