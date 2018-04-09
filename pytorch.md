# pytorch 簡介

## 科普：神經網絡的黑盒不黑
- about black box,
	除了input/ output layer, 第一層通常稱作 __feature representation__ :機器可以識別的寶寶形象, 第二層之後的特徵通常無法被人類辨識。
- 透過將output layer拔除或後幾層拔除，將新的model output取出來做visualization，找出該層識別的意義。
- __Transfer Learning__ : 有時我們只需要一個解決分類問題model的“理解能力”，意即，將output layer拔除，透過中間層(feature representation layer)串聯不同的神經網絡，以處理不同的問題(ex: 分類物件-->預測物件價值，其中，為保持model feature extraction的能力，前三個layer會保留)。

## Why pyTorch ?
- 更容易呈現NN工作的流程
- 做Batch normalization 的效率較tensorflow要高
- 