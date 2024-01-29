# This configuration prepares the ICDAR15 1811 and 2077
# version, and uses ICDAR15 2077 version by default.
# Read https://arxiv.org/pdf/1904.01906.pdf for more info.
data_root = 'data/namjari_khotian'
cache_path = 'data/cache'

train_preparer = dict(
    obtainer=dict(
        type='NaiveDataObtainer',
        cache_path=cache_path,
        files=[
            dict(
                url='http://0.0.0.0:8000/namjari_khotian.zip',
                save_name='namjari_khotian.zip',
                md5='4232b46c81ba99eea6d057dcb06b8f75',
                content=['image', 'annotation'],
                mapping=[
                    [
                        'namjari_khotian/train/labels.txt',
                        'annotations/train.txt'
                    ], ['namjari_khotian/train/images', 'textrecog_imgs/train'],
                ]),
        ]),
    gatherer=dict(type='MonoGatherer', ann_name='train.txt'),
    parser=dict(
        type='ICDARTxtTextRecogAnnParser', separator=' ', format='img text'),
    packer=dict(type='TextRecogPacker'),
    dumper=dict(type='JsonDumper'))

test_preparer = dict(
    obtainer=dict(
        type='NaiveDataObtainer',
        cache_path=cache_path,
        files=[
            dict(
                url='http://0.0.0.0:8000/namjari_khotian.zip',
                save_name='namjari_khotian.zip',
                md5='4232b46c81ba99eea6d057dcb06b8f75',
                content=['image', 'annotation'],
                mapping=[[
                    'namjari_khotian/test/labels.txt',
                    'annotations/test.txt'
                ], ['namjari_khotian/test/images', 'textrecog_imgs/test']]),
        ]),
    gatherer=dict(type='MonoGatherer', ann_name='test.txt'),
    parser=dict(
        type='ICDARTxtTextRecogAnnParser', separator=' ', format='img text'),
    packer=dict(type='TextRecogPacker'),
    dumper=dict(type='JsonDumper'))
delete = [
    'annotations', 'namjari_khotian'
]
config_generator = dict(
    type='TextRecogConfigGenerator',
    # test_anns=[
    #     dict(ann_file='textrecog_test.json'),
    #     dict(dataset_postfix='namjari', ann_file='textrecog_test_namjari.json')
    # ]
)
