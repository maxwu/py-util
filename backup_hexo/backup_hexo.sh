#!/bin/bash
TARGETDIR="/Volumes/TRANSCEND1"  # Path to the SD card on Mac
DATESTR=$(date +%Y-%m-%d_%H-%M-%S)
tar -czvf $TARGETDIR/$DATESTR-hexo.tar.gz ~/devel/hexo
