# pyCompressor
A python implementation of a traditional Dynamic Range Compressor


Currently implemented as a function for a gain computer - it would be better to implement as a class, as then each instance would have it's own unique global variable to identify the previous yL value.


## Warning
Can only be used for mono gain-computer - due to single yL_prev value.

Do not use for multiple different tracks, requires separate yL_prev global variables.


## Todo

* Make allow stereo tracks, with parameter for mono compression on stereo track, or stereo compression
* Block based implementation
* Make more pythonic - native numpy
* Create class structure, allowing instances to use unique 
* Example of sidechain compressor
* Documentation
