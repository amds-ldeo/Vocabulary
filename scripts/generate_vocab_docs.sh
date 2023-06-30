#!/bin/bash
#
# Regenerates the vocabulary markdown files from the GH sources
#
#
SCRIPT_FOLDER="$(dirname ${0})"
SOURCE_BASE="https://github.com/smrgeoinfo/vocabulary/tree/main/src/vocabularies/"
SOURCES=("GeoXAnalyticalTechnique.ttl")
DEST_FOLDER="vocabularies/"
mkdir -p "${DEST_FOLDER}"
for src in ${SOURCES[@]}; do
    fname="${src%%.*}.md"
    echo "Generating ${fname}..."
    python "${SCRIPT_FOLDER}/vocab2md.py" "${SOURCE_BASE}${src}" > "${DEST_FOLDER}${fname}"
done

quarto render "${DEST_FOLDER}${fname}" --to html


echo "Done.  Type 'exit' to close window. "

powershell


