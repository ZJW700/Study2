_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_2x.py', '../_base_/default_runtime.py'
]

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)
    )
)

classes = ('balloon',)
data_root = 'data/ballon/'
data = dict(
    train=dict(
        ann_file=data_root + 'annotations/train_annotation_coco.json',
        img_prefix=data_root + 'train/',
        classes=classes),
    val=dict(
        ann_file=data_root + 'annotations/val_annotation_coco.json',
        img_prefix=data_root + 'val/',
        classes=classes),
    test=dict(
        ann_file=data_root + 'annotations/val_annotation_coco.json',
        img_prefix=data_root + 'val/',
        classes=classes)
)

load_from = 'checkpoints/mask_rcnn_r50_fpn_2x_coco_bbox_mAP-0.392__segm_mAP-0.354_20200505_003907-3e542a40.pth'