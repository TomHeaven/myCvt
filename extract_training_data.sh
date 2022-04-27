DATA_DIR="/Volumes/Data/实验数据/ILSVRC2012/ILSVRC2012_img_train"
cd $DATA_DIR
find . -name "*.tar" | while read NAME ; do mkdir -p "${NAME%.tar}"; tar -xvf "${NAME}" -C "${NAME%.tar}"; rm -f "${NAME}"; done