#at now + 8 hours -f ~/myscript.sh

nohup bash -c "sleep $(echo '2 * 60 * 60' | bc) ; bash run.sh -g 4 -t train --cfg experiments/cifar100/cvt/cvt-13-224x224.yaml" > train_cifar100_cvt.log &
#nohup bash run.sh -g 4 -t train --cfg experiments/cifar100/cvt/local-cvt-13-224x224.yaml > train_cifar100_local_cvt.log &