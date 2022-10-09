---
language:
  - en
thumbnail: "https://i.imgur.com/z0BwlOe.png"
tags:
- image matting
- image segmentation
license: apache-2.0
metrics:
- mean_iou
---
PP-HumanSeg v2 model, released by [Paddle](https://github.com/PaddlePaddle/PaddleSeg/tree/release/2.6/contrib/PP-HumanSeg).

Tested on the [PP-HumanSeg-14K](https://github.com/PaddlePaddle/PaddleSeg/blob/release/2.6/contrib/PP-HumanSeg/paper.md) dataset.

| Model Name | Best Input Shape | mIou(%) | Inference Time on Arm CPU(ms) | Modle Size(MB) |
| --- | --- | --- | ---| --- |
| PP-HumanSegV2-Lite | 256x144 | 96.63 | 15.86 | 5.4 |