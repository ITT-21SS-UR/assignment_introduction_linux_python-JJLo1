url="ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README"

#get the filename from the url
filename=${url##*/}

#check if NO file with the filename is present in the current directory
if [ ! -f $filename ];then
    wget $url #if no file with the $filename is present we download it from $url
fi


######################
# The following pipe 
#    1. reads in the "README" file in the current directory
#    2. replaces all uppercase characters with their lowercase versions
#    3. deletes all punctation characters
#    4. splits it into words per line
#    5. removes whitespace lines
#    6. sorts the words alphabeticly
#    7. removes duplicates and writes their number of occurences infront of the word
#    8. sorts by number of occurences
#    9. removes all but the first 10 lines
#   10. removes all numbers and spaces
######################

cat $filename | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | sed 's/ /\n/g' | grep . | sort | uniq -c |sort -g -r | head -10 | tr -d '01234567890 '

