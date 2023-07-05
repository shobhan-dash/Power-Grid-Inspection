# Development of Deep Learning Architectures for Inspection and Monitoring of Power Line Infrastructure
### Overview
This project is a part of our Practise School-I curriculum of BITS Pilani, undertaken by us from May-July 2023 at [CSIR-CEERI](https://ceeri.res.in), Pilani, Rajasthan. The project was completed under the guidance of [Dr. Sumeet Saurav](https://www.ceeri.res.in/profiles/sumeet-saurav/), Senior Scientist, CSIR-CEERI. ([IEEE Page](https://ieeexplore.ieee.org/author/37085633251))
<br/>
The aim of this project is to detect and classify various electrical components in the power grids, localize them, and detect faults and other points of failure. The dataset for this project can be found [here](https://github.com/andreluizbvs/PLAD). 

### Introduction
The dataset contains high-resolution _(5472 x 3648 pixels)_ aerial images of overhead power lines and has about 2500 cumulative instances of components like `Towers, Insulators, Dampers, Spacers and Plates`.
 A cascaded CNN model based on YOLO-NAS has been used for the components' classification, localization, and fault detection.

 ### Pre-processing and Data Augmentation
 #### Test/Train Split: 94% Train, 4% Validation, 2% Train (330, 15, 8 images respectively) 
 Since the number of images in the dataset is very less (due to operational reasons for flying UAVs with high-resolution cameras), the following data augmentation methods have been implemented:
   
    PREPROCESSING:
    - Auto-Orient
    - Resize: Stretch to 2048x1152
    
    AUGMENTATIONS:
    - Outputs per training example: 3
    - Flip: Horizontal, Vertical
    - 90° Rotate: Clockwise, Counter-Clockwise, Upside Down
    - Crop: 0% Minimum Zoom, 20% Maximum Zoom
    - Rotation: Between -15° and +15°
    - Shear: ±15° Horizontal, ±15° Vertical
    - Grayscale: Apply to 25% of images
    - Hue: Between -25° and +25°
    - Saturation: Between -25% and +25%
    - Brightness: Between -25% and +25%
    - Exposure: Between -25% and +25%

  ### Stage I: Object Classification:
  Model Used: YOLO-NAS Large model. After training for 50 epochs on the dataset, the `best_weights.pkt` file is used to predict on the test set.
  ##### A sample output is shown below:

![image](https://drive.google.com/uc?export=view&id=1gNY7mtz5nlOq4sbnQQkfhbyvIitQCos_)

  ###### Here are the results of predicting on the same image by YOLOv8 and YOLO-NAS models after being trained for 50 epochs:
  ![image](https://drive.google.com/uc?export=view&id=1N_1IxDGdBli3C4yxeFWd8rgcXRzPR5D3)
  As it can be seen, YOLO-NAS is significantly better at predicting the bounding boxes for the most important class of this project - insulators.
  #### mAP@0.50 values for each class:
   - damper: 0.8333
   - insulator: 0.9
   - plate: 0.8
   - spacer: 0.9
   - tower: 0.9667
     
  #### Project Contributors:
   - [Shobhan Dash](https://www.linkedin.com/in/shobhan-dash-0998ab228/)
   - [Parth Rastogi](https://www.linkedin.com/in/parth-rastogi-b31415222/)
   - [Jatin Jindal](https://www.linkedin.com/in/jatinjindal322/)
