DATA_DIR="/home/tomheaven/实验//ILSVRC2012/ILSVRC2012_img_train"
cd $DATA_DIR
find . -name "*.tar" | while read NAME ; do mkdir -p "${NAME%.tar}"; tar -xvf "${NAME}" -C "${NAME%.tar}"; rm -f "${NAME}"; done