CURR_DIR=$(pwd)
ARCHIVE_DIR=${CURR_DIR}/archives
echo "Executing script: $0"
echo "Checking if archive directory exists. If not, create it"

if [ ! -d $ARCHIVE_DIR ]
then
    echo "Making directory ${ARCHIVE_DIR}."
    mkdir $ARCHIVE_DIR
else
    echo "$ARCHIVE_DIR already exists."
fi

DIR=$(basename $1)
echo "Archiving directory: $1"

# Create an archive of the given directory"
tar -cf ${ARCHIVE_DIR}/${DIR}.tar.gz ${1}
