#!/usr/local/bin/python
"""
This is a version of github_action_main.py set up to run offline in
an IDE environment for testing; not used by github action.  check that
paths to docs, cache are all correct. Quarto must be installed in the
local environment.
"""

import logging
import os
import subprocess
import sys
import click
import rdflib
# import rdflib-sqlalchemy
import requests
import vocab
import vocab2mdCacheV2


# @click.option("--command", default="docs", help="docs or uijson")
# @click.option("--path", default="../vocabulary", help="path to turtle files")

def main(command, path):
    #    logging.debug(f"environment variables are {os.environ}")
    #    print(f"environment variables are {os.environ}")

    #    command = os.environ["INPUT_ACTION"]
    #    path = os.environ["INPUT_PATH"]
    #     if path is None:
    #         print("Did not receive a valid path argument so we cannot run.")
    #         sys.exit(-1)
    #     if not os.path.exists(path):
    #         os.makedirs(path)
    #         # Change to 777 so subsequent steps that deal with the directory don't run into permissions issues
    #         os.chmod(path, 777)
    #         print(f"Created {path} since it didn't exist.")

    command = 'docs'
#    command = 'uijson'
    path = '../docs'
# *******************

    input1 = "earthenv_material_extension_mineral_group|earthenv_material_extension_rock_sediment|earthenv_sampled_feature_role|earthenv_materialsampleobject_type"
#    input1 = "SESAR_material_extension_rock_sediment"
    inputttl = input1.split('|')
# inputttl is a list of skos rdf vocabulary filenames with Turtle serialization
# vocab_source_dir is the path to the directory that contains the source files
    input1 = "ming:mineralgroupvocabulary|rksd:rocksedimentvocabulary|essampledfeatrole:sfrolevocabulary|esmat:essampletype"
#    input1 = "sesrs:rocksedimentvocabulary"

    inputvocaburi = input1.split('|')
# make sure have cache directory -- this is where the sqlAlchemy db will be
    cachepath = "../cache/vocabularies.db"
# this is the directory that holds the source SKOS ttl files.
    sourcevocabdir = "../vocabulary"

    print("github_action_main: target path for output: ", path)
    if path is None:
        print("Did not receive a valid path argument so we cannot run.")
        sys.exit(-1)
    if not os.path.exists(path):
        os.makedirs(path)
        # Change to 777 so subsequent steps that deal with the directory don't run into permissions issues
        os.chmod(path, 777)
        print(f"Created {path} since it didn't exist.")

    # do function of original Makefile here

   # for inputf in inputttl:
   #      result = load_cachedb(sourcevocabdir + "/" + inputf + ".ttl", cachepath)
   #      if (result == 0):
   #          print(f"load_cachedb call successful for: {inputf}")
   #      else:
   #          print(f"load_cachedb had problem processing: {inputf}")

        # ***********************
    index = 0
    while index < len(inputttl):
        # for inputf in inputttl:
        result = load_cachedb(sourcevocabdir + "/" + inputttl[index] + ".ttl", inputvocaburi[index], cachepath)
        if (result == 0):
            print(f"load_cachedb call successful for: {inputttl[index]}")
        else:
            print(f"load_cachedb had problem processing: {inputttl[index]}")
        index += 1
        # ***********************

    #  essfrole_earthenv_sampled_feature_role  spec_earthenv_specimen_type
    if command == "uijson":
        print("uijson action has been removed.  json is now fetched dynamically at page load.")
        sys.exit(-1)
    elif command == "docs":
        print("Generating markdown and html docs")
        index = 0
        print(f"input markdown file: {inputttl[index]}, vocab uri: {inputvocaburi[index]}")
        while index < len(inputttl):
            _run_docs_in_container(os.path.join(path, inputttl[index] + ".md"), inputvocaburi[index])
            _quarto_render_html((os.path.join(path, inputttl[index] + ".md")), path)
            index += 1
    else:
        print(f"Unknown command {command}.  Exiting.")
        sys.exit(-1)


# def _run_make_in_container(target: str):
#    subprocess.run(["/usr/bin/make", "-C", "/app", "-f", "/app/Makefile", target])

def load_cachedb(inputf, inputuri, cachepath):
    # tools/vocab.py --verbosity ERROR -s $(CACHE) load $(SRC)/$@
    print(f"cachdb file to load: {inputf}")
    load_args = ["--verbosity", "ERROR", "-s", cachepath, "load", inputf, inputuri]
    result = _run_python_in_container("vocab.py", load_args, f="")
    if (result == 0):
        print(f"vocab.py call successful for {inputf}")
        return 0
    else:
        print(f"vocab.py had problem processing {inputf}")
        return 1


def _quarto_render_html(markdown_in: str, output_path: str):
    #     print("In githubActionMain: Quarto render: ",markdown_in,  output_path)
    #     result = subprocess.run(["/opt/quarto/bin/quarto", "check"])
    #     print("Quarto check result ", result.returncode)
    #  NOTE update quarto location for your local install...
    result = subprocess.run(["quarto", "render", markdown_in, "-t", "html"])
    #     print("Quarto call result ", result.returncode)
    if (result.returncode == 0):
        print(f"Quarto call successful for {markdown_in}")
        return 0
    else:
        print(f"Quarto had problem processing {markdown_in}")
        return 1


# def _run_uijson_in_container(output_path: str, vocab_type: str):
#     with open(output_path, "w") as f:
#         vocab_args = ["-s", "../cache/vocabularies.db", "uijson", vocab_type, "-e"]
#         _run_python_in_container("vocab.py", vocab_args, f)
#         print(f"Successfully wrote uijson file to {output_path}")


def _run_docs_in_container(output_path: str, vocab_type: str):
    with open(output_path, "w") as f:
        docs_args = ["../cache/vocabularies.db", vocab_type]
        _run_python_in_container("vocab2mdCacheV2.py", docs_args, f)
        print(f"Successfully wrote doc file to {output_path}")


def _run_python_in_container(path_to_python_script: str, args: list[str], f):
    subprocess_args = [sys.executable, path_to_python_script]
    subprocess_args.extend(args)
#    subprocess.run(subprocess_args, stdout=f)
    if f=="":
        result = subprocess.run(subprocess_args)
    else:
        result = subprocess.run(subprocess_args, stdout=f)
#    print("container call result ", result.returncode)
    return result.returncode

if __name__ == "__main__":
    main("docs", "output")
