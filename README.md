# osm-pbf-merger

This is a Docker container which allows you to merge PBF files.

PBF files are typically those downloaded from [Geofabrik](http://download.geofabrik.de/).

This uses [OSM Convert](https://wiki.openstreetmap.org/wiki/Osmconvert#Parallel_Processing) to do the processing itself.

## Build the container
Here you can replace `osm-pbf-merger:latest` with an image and tag name of your choice

`docker build -t osm-pbf-merger:latest .`

## Merge some PBF files
Some test data is included in the repository and this gets merged by the example script `run.bat`. The command is:

`docker run -it --rm -v /path/to/your/pbf/files:/data osm-pbf-merger:latest FILE1 [FILE2 [FILE3 []]] [-o OUTPUT_FILE]`

You cannot specify a full path for the output, it will be written to the same folder as the input files. If not specified, but output file will be called `out.osm.pbf`. The directory with the input files must be mounted to `/data` as a volume inside the contanier.