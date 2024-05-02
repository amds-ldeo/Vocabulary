#!/bin/bash
#
# Regenerates the vocabulary markdown files from the GH sources
#
#
SCRIPT_FOLDER="$(dirname ${0})"
SOURCE_BASE="../geochemistry/Minerals/"
SOURCES=(  "mineralSKOS.ttl" )
DEST_FOLDER="../geochemistry/Minerals/html/"
mkdir -p "${DEST_FOLDER}"
for src in ${SOURCES[@]}; do 
	fname="${src%%.*}.md"
	echo "Generating ${fname}..."
	python "${SCRIPT_FOLDER}/vocab2md.py" "${SOURCE_BASE}${src}" > "${DEST_FOLDER}${fname}"
	quarto render "${DEST_FOLDER}${fname}" --to html
	done

echo "Done.  Type 'exit' to close window. "