***Work in progress-Segmentation pipeline complete ** 
This repo contains the code for the project FoodLens, an application where the user can take picture(s) of the food and receive the results of the nutritional content



TO DO LIST: 
    -Figure out a way for volume estimation. The approach should not be AI
    -Build a more comprehensive pipeline that will extract and upload RGBD images and camera intrinsics to a remote server, and receive other messages. But this will happen concurrently with app development.
    -Build a valid UI for the application
Problems and Challenges
[MAJOR CHALLENGE] I experimented with both Colmap and Open3D but both of them take way too long to reconstruct a 3D surface. 

[MAJOR CHALLENGE] Segmentation takes way too long
I have experimented with the Segment-anything model from Meta and the FoodSAM model: 
https://github.com/jamesjg/FoodSAM

The Segment-Anything Model from Meta takes way too long to infer and the FoodSAM model just straight up does not work (it hasn’t been maintained for at least two years).
Right now i am exploring options with MobileSAM with YOLOv8 as the backbone.


[MAJOR CHALLENGE] Name matching: 
I will be utilizing datasets from various sources. The name and formatting for the same foods might be completely different across datasets. I have explored possibilities with libraries such as fuzzywuzzy but have given up. Those libraries only look for similarities in the string literals rather than the semantic meanings of the words. Sometimes a food item might have a completely different name across datasets and fuzzywuzzy is not going to fix anything beyond string formatting issues.


Should we do the processing locally? 
No. Although Apple has its own framework for ML deployment, segmentation, classification and 3D reconstruction are computation heavy and the processors on the phones are simply not enough. Thus the application will run on a remote server with GPU resources.

Where and how to extract the depth mask? 
We will not extract the depth mask locally on the devices since we also need the coloured images for classification and segmentation. We will send the HEIC files to the server directly. 
As for how to extract the depth data, refer to this valuable article from apple:
https://developer.apple.com/documentation/avfoundation/capturing-photos-with-depth

Segmentation limitations
There was already a public model for Food Segmentation called the FoodSAM. Unfortunately, it is not maintained anymore and the program simply does not work.
I have decided to train a segmentation model myself.

How to figure out the proportions of ingredients?
I am still uncertain about this part. Right now we have promising methods for estimating the volume of the entire dish and working out its ingredients. 


How to set up the environment for development? 
Right now it's a complete mess. The ubuntu from the dual boot keeps failing me on the SSH and I plan to uninstall the ubuntu system completely and just stick with Windows WSL. I will use docker images for each of my developmental stages of the DL models. (Remedied now)


Tracking Progress:

04/30
	-Request to access the Recipe 1M+ Dataset has been approved.
05/05 
	-Rudimentary testing website is built that allows upload of RGB image and its corresponding depth mask. 

18/05
	-Experimentation done with the Invercooking Model released by MetaAI. Results have been disappointing. Probably due to the aggressive resizing of image resolutions done during model training (all to 224x224). 
	-Decided to train a multilabel classification model from scratch
	-Difficulties with downloading datasets. Plan to rent a US based server for this issue. 

01/06
    -Experimented with FoodSAM which used facebook's Segment Anything as the backbone. It cannot execute properly likely due to misconfigured environment on my end. Or it is just that their repo is not maintained. (last updated two years ago)
    -Researched on how to take and extract RGBD images with iPhone cameras. 
    -Experimented with my iPhone 12 on XCode. 

15/06 
    -Early drafts of Graphic Designs has been made. 
    -Started experimenting with Colmap, a 3D processing library. 


20/06
    -Came to the conclusion that Colmap is way to inefficient of a method. Takes too much GPU resources and most critically, time, to output a 3D model. Will look into other 3D libraries such as Open3D or Trimesh.

01/07
    -Decided to give up on 3D reconstruction for now and currently limit ourselves to a single picture inference. In the future we might experiment with multi-angle videos.
    -Begin researching for valid segmentation models. Currently looking at SAM from facebook and YOLO.
    -Begin searching for datasets. Recipe1M+ is not a segmentation dataset. Food segmentation datasets are generally difficult to find due to it being a not-too-popular topic.

09/21 (discussion with collaborator)
I will look into the concept of web hooks. 
Two servers are used for the entire pipeline: One for application (Front ends, backends) and one for inference. 

Monetization: NO (as of right now). There are many open source tools that are used during the development of the application and the licenses and acknowledgements of the libraries being used are still not clear. 
We will not look into this until the development of the application itself is not fully complete.

Initially we were planning on building one model for extracting the ingredients of a food then querying a database on those ingredient keys. Now, with the Nutrition5K dataset, we are outputting the nutritional value of the foods right away without the dataset querying step. But we should still leave spaces for potential upgrades in the future. 

Server

I was originally looking into the possibilities of hosting a server on my own PC that was containerized and separate from other parts of my OS. Which turned out to be too difficult. Therefore I will be using online VPS services. The VPS does not need to be powerful at all; it doesn’t really even need a GPU. All it does right now is return a json file for Lucas to work with. 

I have chosen Railway because it offers a 30 days free trial and is very easy to deploy code on. All you need to do is connect it with a github repository and it will give you a website link for other people to access. 

It also tracks the updates to the github repository. For example, if you commit something to the repo, it will rebuild the application which I think it pretty convenient.

14/09
    -Built a dummy server for app development by my collaborator. It will receive a request from the user side and then output a string which will contain the nutritional content and other information. All processing tasks will be performed on the server side. 

20/09
    -Found the dataset [FoodInsSeg](https://github.com/jamesjg/FoodInsSeg) which looks really promising. It is an instance segmentation dataset.    
    -Looking into yolo11-seg

23/09
    -Cleaned the dataset and reformatted it into the form that YOLO requires. 
    -Put it on a remote server to train for 500 EPOCHS on 4x3090. Early stopping is enabled but the patience it set to 100, a very generous number


24/09 
    -The results from yolo11n-seg is really disappointing. Many food has not been covered. Upon a deeper dive the problem actually lies within the dataset. The dataset is poorly labelled (probably machine labelled)
    -Will search for a new dataset. And experiment with yolo11l-seg as the increase in inference time is not that significant (1.8ms versus 7.8ms on T4 with tensorRT)

07/10
    -Found FoodSeg103. Appears to be manually labelled and of very high quality. 
    -yolo11l-seg will be used. 
    -Put on server to train for 500 EPOCH on 4x 3090Ti. Early stopping is also set with patience = 100

08/10
    -Results from the last experiment is very successful. Probably a combination of larger model and a significantly better dataset. 
