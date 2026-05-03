---
type: chapter
tags: [aima, chapter, computer-vision]
created: 2026-05-02
updated: 2026-05-02
sources: ["raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf"]
chapter: 27
---

# Chapter 27 - Computer Vision

## Summary

Chapter 27 of *Artificial Intelligence: A Modern Approach* (4th Edition) covers **computer vision**. This chapter is part of Part VI: Communicating, Perceiving, and Acting. The chapter contains approximately 11,721 words and covers foundational concepts, algorithms, and frameworks central to understanding computer vision in the context of artificial intelligence.

## Key Points

- **Introduction**: 27
CHAPTER
COMPUTER VISION
Inwhichweconnectthecomputertotheraw,unwashedworldthroughtheeyesofacamera.
Most animals have eyes, often at significant cost: eyes take up a lot of space; use energy;
andarequitefragile. Thiscostisjustifiedbytheimmensevaluethateyesprovide. Anagent
thatcanseecanpredictthefut...
- **27.1 Introduction**: Visionisaperceptualchannelthatacceptsastimulusandreportssomerepresentationofthe
world. Most agents that use vision use passive sensing—they do not need to send out light
to see. In contrast, active sensing involves sending out a signal such as radar or ultrasound,
andsensingareflection. Examplesofag...
- **27.2 Image Formation**: Imagingdistortstheappearanceofobjects. Apicturetakenlookingdownalongstraightset
ofrailwaytrackswillsuggestthattherailsconvergeandmeet. Ifyouholdyourhandinfront
ofyoureye,youcanblockoutthemoon,eventhoughthemoonislargerthanyourhand(this
works with the sun too, but you could damage your eyes checking i...
- **27.2.1 Images without lenses: The pinhole camera**: Image sensors gather light scattered from objects in a scene and create a two-dimensional Scene
(2D) image. In the eye, these sensors consist of two types of cell: There are about 100 Image
millionrods,whicharesensitivetolightatawiderangeofwavelengths,and5millioncones.
Cones,whichareessentialforcolo...
- **27.2.2 Lens systems**: Pinholecamerascanfocuslightwell,butbecausethepinholeissmall,onlyalittlelightwill
get in, and the image will be dark. Over a short period of time, only a few photons will hit
eachpointonthesensor,sothesignalateachpointwillbedominatedbyrandomfluctuations;
wesaythatadarkfilmimageisgrainyandadarkdigital...

## Sections Overview

### Introduction

27
CHAPTER
COMPUTER VISION
Inwhichweconnectthecomputertotheraw,unwashedworldthroughtheeyesofacamera.
Most animals have eyes, often at significant cost: eyes take up a lot of space; use energy;
andarequitefragile. Thiscostisjustifiedbytheimmensevaluethateyesprovide. Anagent
thatcanseecanpredictthefuture—itcantellwhatitmightbumpinto;itcantellwhetherto
attack or to flee or to court; it can guess whet...

### 27.1 Introduction

Visionisaperceptualchannelthatacceptsastimulusandreportssomerepresentationofthe
world. Most agents that use vision use passive sensing—they do not need to send out light
to see. In contrast, active sensing involves sending out a signal such as radar or ultrasound,
andsensingareflection. Examplesofagentsthatuseactivesensingincludebats(ultrasound),
dolphins(sound),abyssalfishes(light),andsomerobots(...

### 27.2 Image Formation

Imagingdistortstheappearanceofobjects. Apicturetakenlookingdownalongstraightset
ofrailwaytrackswillsuggestthattherailsconvergeandmeet. Ifyouholdyourhandinfront
ofyoureye,youcanblockoutthemoon,eventhoughthemoonislargerthanyourhand(this
works with the sun too, but you could damage your eyes checking it). If you hold a book
flatinfrontofyourfaceandtiltitbackwardandforward, itwillseemtoshrinkandgrowin...

### 27.2.1 Images without lenses: The pinhole camera

Image sensors gather light scattered from objects in a scene and create a two-dimensional Scene
(2D) image. In the eye, these sensors consist of two types of cell: There are about 100 Image
millionrods,whicharesensitivetolightatawiderangeofwavelengths,and5millioncones.
Cones,whichareessentialforcolorvision,areofthreemaintypes,eachofwhichissensitive
toadifferentsetofwavelengths. Incameras,theimagei...

### 27.2.2 Lens systems

Pinholecamerascanfocuslightwell,butbecausethepinholeissmall,onlyalittlelightwill
get in, and the image will be dark. Over a short period of time, only a few photons will hit
eachpointonthesensor,sothesignalateachpointwillbedominatedbyrandomfluctuations;
wesaythatadarkfilmimageisgrainyandadarkdigitalimageisnoisy;eitherway,theimage
isoflowquality.
Enlarging the hole (the aperture) will make the imag...

### 27.2.3 Scaled orthographic projection

The geometric effects of perspective imaging aren’t always pronounced. For example, win-
dows on a building across the street look much smaller than ones right nearby, but two win-
dows that are next to each other will have about the same size even though one is slightly
farther away. We have the option to handle the windows with a simplified model called
Scaledorthographic scaled orthographic pro...

### 27.2.4 Light and shading

The brightness of a pixel in the image is a function of the brightness of the surface patch in
thescenethatprojectsto thepixel. Formoderncameras, thisfunctionislinearformiddling
intensitiesoflight,buthaspronouncednonlinearitiesfordarkerandbrighterillumination. We
willusealinearmodel. Imagebrightnessisastrong,ifambiguous,cuetoboththeshapeand
the identity of objects. The ambiguity occurs because the...

### 27.2.5 Color

Fruit is a bribe that a tree offers to animals to carry its seeds around. Trees that can signal
when this bribe is ready have an advantage, as do animals that can read these signals. As a
result,mostfruitsstartgreen,andturnredoryellowwhenripe,andmostfruit-eatinganimals
can see these color changes. Generally, light arriving at the eye has different amounts of
energyatdifferentwavelengths,andisrepre...

### 27.3 Simple Image Features

Light reflects off objects in the scene to form an image consisting of, say, twelve million
three-bytepixels. Aswithallsensorstherewillbenoiseintheimage,andinanycasethereis
alotofdatatodealwith. Thewaytogetstartedanalyzingthisdataistoproducesimplified
representationsthatexposewhat’simportant,butreducedetail. Muchcurrentpracticelearns
these representations from data. But there are four properties o...

### 27.3.1 Edges

Edges Edges are straight lines or curves in the image plane across which there is a “significant”
change in image brightness. The goal of edge detection is to abstract away from the messy,
multi-megabyteimageandtowardsamorecompact,abstractrepresentation,asinFigure27.6.
Effectsinthesceneveryoftenresultinlargechangesinimageintensity,andsoproduceedges
in the image. Depth discontinuities (labeled 1 in...

### 27.3.2 Texture

In everyday language, the texture of surfaces hints at what they feel like when you run a Texture
finger over them (the words “texture,” “textile,” and “text” have the same Latin root, a word
for weaving). In computational vision, texture refers to a pattern on a surface that can be
sensedvisually. Usually,thesepatternsareroughlyregular. Examplesincludethepatternof
windowsonabuilding,thestitcheson...

### 27.3.3 Optical flow

Next, let us consider what happens when we have a video sequence, instead of just a single
static image. Whenever there is relative movement between the camera and one or more
Opticalflow objects in the scene, the resulting apparent motion in the image is called optical flow. This
describes the direction and speed of motion of features in the image as a result of relative
motionbetweentheviewerand...

### 27.3.4 Segmentation of natural images

Segmentation is the process of breaking an image into groups of similar pixels. The basic Segmentation
ideaisthateachimagepixelcanbeassociatedwithcertainvisualproperties,suchasbright-
ness, color, and texture. Within an object, or a single part of an object, these attributes vary
relatively little, whereas across an inter-object boundary there is typically a large change in
one or more of these at...

### 27.4 Classifying Images

Imageclassificationappliestotwomaincases. Inone,theimagesareofobjects,takenfrom
a given taxonomy of classes, and there’s not much else of significance in the picture—for
example,acatalogofclothingorfurnitureimages,wherethebackgrounddoesn’tmatter,and
theoutputoftheclassifieris“cashmeresweater”or“deskchair.”
Intheothercase,eachimageshowsascenecontainingmultipleobjects. Soingrassland
you might see a ...

### 27.4.1 Image classification with convolutional neural networks

Convolutionalneuralnetworks(CNNs)arespectacularlysuccessfulimageclassifiers. With
enough training data and enough training ingenuity, CNNs produce very successful classifi-
cationsystems,muchbetterthananyonehasbeenabletoproducewithothermethods.
The ImageNet data set played a historic role in the development of image classification
systems by providing them with over 14 million training images, cla...

### 27.4.2 Why convolutional neural networks classify images well

Image classification is best understood by looking at data sets, but ImageNet is much too
largetolookatindetail. TheMNISTdatasetisacollectionof70,000imagesofhandwritten
digits,0–9,whichisoftenusedasastandardwarmupdataset. Lookingatthisdataset(some
examplesappearinFigure27.12)exposessomeimportant,quitegeneral,properties. Youcan
takeanimageofadigitandmakeanumberofsmallalterationswithoutchangingtheid...

### 27.5 Detecting Objects

Imageclassifierspredictwhatisintheimage—theyclassifythewholeimageasbelongingto
oneclass. Objectdetectorsfindmultipleobjectsinanimage,reportwhatclasseachobjectis,
Boundingbox andalsoreportwhereeachobjectisbygivingaboundingboxaroundtheobject.1 Thesetof
classesisfixedinadvance. Sowemighttrytodetectallfaces,allcars,orallcats.
Slidingwindow We can build an object detector by looking at a small sliding ...

### 27.6.2 Binocular stereopsis

Most vertebrates have two eyes. This is useful for redundancy in case of a lost eye, but it
helpsinotherwaystoo. Mostpreyhaveeyesonthesideoftheheadtoenableawiderfieldof
vision. Predatorshavetheeyesinthefront,enablingthemtousebinocularstereopsis. Hold Binocularstereopsis
bothindexfingersupinfrontofyourface,withoneeyeclosed,andadjustthemsothefront
fingeroccludestheotherfingerintheopeneye’sview. Nows...

### 27.7 Using Computer Vision

Here we survey a range of computer vision applications. There are now many reliable com-
puter vision tools and toolkits, so the range of applications that are successful and useful is
extraordinary. Many are developed at home by enthusiasts for special purposes, which is
testimonytohowusablethemethodsareandhowmuchimpacttheyhave. (Forexample,an
enthusiast created a great object-detection-based pet...

### 27.7.1 Understanding what people are doing

Ifwecouldbuildsystemsthatunderstoodwhatpeoplearedoingbyanalyzingvideo,wecould
build human-computer interfaces that watch people and react to their behavior. With these
interfaces, we could: design buildings and public places better, by collecting and using data
about what people do in public; build more accurate and less intrusive security surveillance
systems;buildautomatedsportscommentators;make...

### 27.7.2 Linking pictures and words

Many people create and share pictures and videos on the Internet. The difficulty is finding
what you want. Typically, people want to search using words (rather than, say, example
sketches). Because most pictures don’t come with words attached, it is natural to try and
Taggingsystem build tagging systems that tag images with relevant words. The underlying machinery is
straightforward—weapplyimagecl...

### 27.7.3 Reconstruction from many views

Reconstructing a set of points from many views—which could come from video or from an
aggregation of tourist photographs—is similar to reconstructing the points from two views,
buttherearesomeimportantdifferences. Thereisfarmoreworktobedonetoestablishcor-
respondencebetweenpointsindifferentviews,andpointscangoinandoutofview,making
the matching and reconstruction process messier. But more views mea...

### 27.7.4 Geometry from a single view

Geometricrepresentationsareparticularlyusefulifyouwanttomove,becausetheycanreveal
where you are, where you can go, and what you are likely bump into. But it is not always
convenienttousemultipleviewstoproduceageometricmodel. Forexample,whenyouopen
thedoorandstepintoaroom,youreyesaretooclosetogethertorecoveragoodrepresentation...

### 27.7.5 Making pictures

Itisnowcommontoinsertcomputergraphicsmodelsintophotographsinaconvincingfash-
ion,asinFigure27.23,whereastatuehasbeenplacedintoaphotoofaroom. Firstestimate
adepthmapandalbedoforthepicture. Thenestimatethelightingintheimagebymatching
ittootherimageswithknownlighting. Placetheobjectintheimage’sdepthmap,andrender
theresultingworldwithaphysicalrenderingprogram—astandardtoolincomputergraphics.
Finally,b...

### 27.7.6 Controlling movement with vision

Oneoftheprincipalusesofvisionistoprovideinformationbothformanipulatingobjects—
pickingthemup,graspingthem,twirlingthem,andsoon—andfornavigatingwhileavoiding
obstacles. The ability to use vision for these purposes is present in the most primitive of
animal visual systems. In many cases, the visual system is minimal, in the sense that it
extracts from the available light field just the information t...

## Key Entities Mentioned

- Aristotle
- Stuart Russell

## Algorithms & Concepts

- [[Therearestraightforward
algorithm]]

## Cross-References

- Previous: [[Chapter 26 - Robotics]]
- Next: [[Chapter 28 - Philosophy, Ethics, and Safety of AI]]
- Part: Part VI: Communicating, Perceiving, and Acting

## Sources

- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 27. Pearson.
- Source file: `raw/efdd4d1d4c2087fe1cbe03d9ced67f34.pdf`
