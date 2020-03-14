# Image and annotation data generation

## Installation

Install blender (This repository is tested with blender 2.82a) in an appropriate place `BLENDER_ROOT` and do

```buildoutcfg
export BLENDER_EXEC=`PATH_TO_BLENDER_EXEC`
```

Run script with

```buildoutcfg
python main.py ${BLENDER_EXEC} --model_file=scene.py --windowless
```

and view result by (uses ImageMagick)

```buildoutcfg
display data/image.png
```

## Objectives

### Setup

Environment:
 * Clear environment
 * Set up simple camera + object + lights

### Annotation

Image:
 * Export image
 * Export png mask of object

Data:
 * 2D bounding box
 * 3D bounding box
 * Translation and rotation vector
 
 ## Future ideas
 
 ### Object
 * Multiple objects
 * Materials
 * Textures
 
 ### Annotations
 * Occlusion
 
 ### Lights
 * More advanced light setup
 
 ### Configuration
 * Define scene on yaml configuration format
 
 ### API
 * Access through ROS somehow