dlms_data_root = 'tests/data/dlrms_dhaka'

dlms_rec_train = dict(
    type='OCRDataset',
    data_root=dlms_data_root,
    data_prefix=dict(img_path='imgs/'),
    ann_file='labels.json',
    pipeline=None,
    test_mode=False)

dlms_rec_test = dict(
    type='OCRDataset',
    data_root=dlms_data_root,
    data_prefix=dict(img_path='imgs/'),
    ann_file='labels.json',
    pipeline=None,
    test_mode=True)
