from cmath import inf
import os
import shutil
import tqdm
import scipy.io


def move_folders(data_dir):
    for i in reversed(range(1000)):
        src_dir = os.path.join(data_dir, str(i))
        dst_dir = os.path.join(data_dir, str(i+1))
        shutil.move(src_dir, dst_dir)

def prepare_val_dataset(val_dir, gt_txt_path, meta_path, out_dir):
    # read labels
    with open(gt_txt_path, 'r') as f:
        labels =  f.readlines()
    labels = [int(label.strip()) for label in labels]
    #print('labels', labels[0], labels[1])
    # scan image file names
    filenames = [f for f in sorted(os.listdir(val_dir)) if not f.startswith('.') and f.endswith('.JPEG')]
    #print('filenames', filenames[0], filenames[1])
    
    meta = scipy.io.loadmat(meta_path)
    #print(' meta', list(meta.keys()),  meta['synsets'][0])
    id_name_dict = {}
    for item in tqdm.tqdm(meta['synsets']):
        id = item[0][0][0][0]
        name = item[0][1][0]
        id_name_dict[id] = name
    
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    print('Copying files ...')    
    for (filename, label) in tqdm.tqdm(zip(filenames, labels), total=len(filenames)):
        src_file = os.path.join(val_dir, filename)
        # convert id to name
        label = id_name_dict[label]
        dst_dir = os.path.join(out_dir, label)
        if not os.path.isdir(dst_dir):
            os.mkdir(dst_dir)
        dst_file = os.path.join(out_dir, label, filename)
        shutil.copy(src_file, dst_file)


if __name__ == '__main__':
    val_dir = '/home/tomheaven/实验/ILSVRC2012/ILSVRC2012_img_val'
    gt_txt_path = 'dataset/imagenet/ILSVRC2012_validation_ground_truth.txt'
    meta_path = 'dataset/imagenet/meta.mat'
    out_dir = 'dataset/imagenet/val'
    prepare_val_dataset(val_dir, gt_txt_path, meta_path, out_dir)
    #move_folders(out_dir)