## NewCollege and CityCentre Dataset for HTMap

[HTMap](https://github.com/emiliofidalgo/htmap) requires 2 consecutive images from the left and right camera to be combined horizontally for NewCollege and CityCentre datasets.

This repo contains code to generate new images, their coordinates, and ground truth loops file.

## GT Loops format

To keep the file human readable and small, we adopt the following structure

- CSV Comma Separated
- Headers: img, index, loops
- `loop`s contain multiple `Range`s which are Semicolon Separated
- Each `Range` Colon Separated, Start and End indices Both Inclusive

Example `loop`:

```
196:202;271:287

# expands to
196, 197, 198, 199, 200, 201, 202, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282
```
- [utils.py](utils.py) contains
    - `list_unminify`: to convert a minified string to a list of numbers, use flatten=True to get a flat list
    - `list_minify`: to convert a list of numbers to a minified string
