### Metrics 
The following metrics were obtained after training the YOLO-NAS Large Model for 100 epochs on the [STD-PLAD Dataset](https://drive.google.com/file/d/1KsNziErZ5ZRuWBpwUS5nlTnb8CcB2uQp/view) :
<br/>

    SUMMARY OF EPOCH 100
├── Training<br/>
│   ├── Ppyoloeloss/loss = 1.7261<br/>
│   │   ├── Best until now = 1.7456 (↘ -0.0196)<br/>
│   │   └── Epoch N-1      = 1.7456 (↘ -0.0196)<br/>
│   ├── Ppyoloeloss/loss_cls = 0.7582<br/>
│   │   ├── Best until now = 0.7635 (↘ -0.0053)<br/>
│   │   └── Epoch N-1      = 0.7635 (↘ -0.0053)<br/>
│   ├── Ppyoloeloss/loss_dfl = 0.8715<br/>
│   │   ├── Best until now = 0.8898 (↘ -0.0183)<br/>
│   │   └── Epoch N-1      = 0.8902 (↘ -0.0187)<br/>
│   └── Ppyoloeloss/loss_iou = 0.2128<br/>
│       ├── Best until now = 0.2134 (↘ -0.0006)<br/>
│       └── Epoch N-1      = 0.2148 (↘ -0.002)<br/>
└── Validation<br/>
    ├── F1@0.50 = 0.0732<br/>
    │   ├── Best until now = 0.1229 (↘ -0.0496)<br/>
    │   └── Epoch N-1      = 0.0555 (↗ 0.0177)<br/>
    ├── Map@0.50 = 0.7297<br/>
    │   ├── Best until now = 0.7196 (↗ 0.0101)<br/>
    │   └── Epoch N-1      = 0.6829 (↗ 0.0469)<br/>
    ├── Ppyoloeloss/loss = 1.4735<br/>
    │   ├── Best until now = 1.528  (↘ -0.0546)<br/>
    │   └── Epoch N-1      = 1.6495 (↘ -0.176)<br/>
    ├── Ppyoloeloss/loss_cls = 0.7391<br/>
    │   ├── Best until now = 0.7561 (↘ -0.017)<br/>
    │   └── Epoch N-1      = 0.8762 (↘ -0.1372)<br/>
    ├── Ppyoloeloss/loss_dfl = 0.7077<br/>
    │   ├── Best until now = 0.7249 (↘ -0.0172)<br/>
    │   └── Epoch N-1      = 0.7317 (↘ -0.0241)<br/>
    ├── Ppyoloeloss/loss_iou = 0.1522<br/>
    │   ├── Best until now = 0.1563 (↘ -0.0041)<br/>
    │   └── Epoch N-1      = 0.1629 (↘ -0.0107)<br/>
    ├── Precision@0.50 = 0.0388<br/>
    │   ├── Best until now = 0.0678 (↘ -0.029)<br/>
    │   └── Epoch N-1      = 0.0292 (↗ 0.0096)<br/>
    └── Recall@0.50 = 0.8048<br/>
        ├── Best until now = 0.7955 (↗ 0.0093)<br/>
        └── Epoch N-1      = 0.7717 (↗ 0.0331)<br/>
