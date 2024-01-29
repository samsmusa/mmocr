namjari_khotian_textrecog_data_root = 'data/namjari_khotian'

namjari_khotian_textrecog_train = dict(
    type='OCRDataset',
    data_root=namjari_khotian_textrecog_data_root,
    ann_file='textrecog_train.json',
    pipeline=None)

namjari_khotian_textrecog_test = dict(
    type='OCRDataset',
    data_root=namjari_khotian_textrecog_data_root,
    ann_file='textrecog_test.json',
    test_mode=True,
    pipeline=None)
