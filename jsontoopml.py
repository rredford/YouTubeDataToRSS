#
#  Reads json file to convert to opml file.
#
#  Rolf Redford
#
#  11/27/2020
#
#  1.0 initial version. 

#!/usr/bin/python

import sys
import os.path
from os import path

if not len(sys.argv) == 3:
  exit("Need jsontoopml.py <input file> <output file>\n")

# filenames
infil = str(sys.argv[1]);
outfil = str(sys.argv[2]);

# files
inf = ""
outf = ""

# opml variables
otitle = ""
ochannelID = ""

# open file with handling
try:
  inf = open(infil, "r")
except ValueError:
  print("Input file error: " & ValueError)

# check file exist if it dont, open file,
# unless user want to overwrite anyway.
if path.exists(outfil):
  val = raw_input("Overwrite " + outfil + " file? (y/n):") 
  if not val == "y":
    exit(outfil + " file exists.")

try:
  outf = open(outfil, "w")
except ValueError:
  inf.close() # since already opened
  print("Output file error: " & ValueError)

# Opening lines in file
outf.write("<?xml version=\"1.0\"?>\n")
outf.write("<opml version=\"1.0\">\n")
outf.write("  <head>\n")
outf.write("    <title>youtube data to OPML export</title>\n")
outf.write("  </head>\n")
outf.write("<body>\n")
outf.write("  <outline title=\"YouTube Subscriptions\" text=\"YouTube Subscriptions\">\n")

# now process file, stripping needed info and write in opml file.
for x in inf:
  infile = x
  # There is always TWO channelIds.
  # One is users own channelid, then second is entry channel id.
  # However only second counts.
  # Just copy both times, and second will overwrite and be correct one.
  if "\"channelId\"" in infile:
    work = infile.split("\"") # always at array #3.
    ochannelID = work[3];     # file might have errors but not likely.
  elif "\"title\"" in infile:
    # if matched, its last info needed, write out.
    work = infile.split("\"")
    otitle = work[3];
    outf.write("    <outline\n")
    outf.write("      title=\"" + otitle + "\"\n")
    outf.write("      text=\"" + otitle + "\"\n")
    outf.write("      type=\"rss\"\n")
    outf.write("      xmlUrl=\"https://www.youtube.com/feeds/videos.xml?channel_id=" + ochannelID + "\"\n")
    outf.write("      htmlUrl=\"https://www.youtube.com/channel/" + ochannelID + "\"\n")
    outf.write("    />\n")
    
# now close tags
outf.write("  </outline>\n") #youtube sub... tag
outf.write("</body>\n")
outf.write("</opml>\n")

# close files
inf.close()
outf.close()





