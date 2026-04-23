#!/usr/local/bin/python
"""
github_action_main original
depends on makefile to run vocab.py
Driver file for the vocabularies GitHub Action.  Runs inside a Docker container,
with all of the vocabularies tools and dependencies copied into the Docker container.

the github workflow needs to copy output files to the docs directory
in the public github, else they disappear with the docker container when workflow
completes
original code by Dave Vieglais for iSamples project
modified by SM Richard 2023-12-14

input arguments are grabbed from environmental variables
"""

import logging
import os
import subprocess
import sys


def main():
    command = os.environ["INPUT_ACTION"]
    print("github_action_main: INPUT_ACTION: ", command)
    path = os.environ["INPUT_PATH"]
    path = os.path.join(path, "docs")
    input = os.environ["INPUT_INPUTTTL"]
    print(f"inputttl string: {input}")
    inputttl = input.split('|')
    for filename in inputttl:
        print(f"files to load: {filename}")

    input = os.environ["INPUT_INPUTVOCABURI"]
    print(f"inputvocaburi string: {input}")
    inputvocaburi = input.split('|')
    for auri in inputvocaburi:
        print(f"vocab URIs: {auri}")

    if len(inputttl) != len(inputvocaburi):
        print(f"inputttl ({len(inputttl)}) and inputvocaburi ({len(inputvocaburi)}) counts do not match. Exiting.")
        sys.exit(-1)

    cachepath = "cache/vocabularies.db"
    sourcevocabdir = os.environ.get("INPUT_VOCABDIR") or "vocabulary"
    print(f"github_action_main: source vocab directory: {sourcevocabdir}")

    print("github_action_main: target path for output: ", path)
    if path is None:
        print("Did not receive a valid path argument so we cannot run.")
        sys.exit(-1)
    if not os.path.exists(path):
        os.makedirs(path)
        os.chmod(path, 777)
        print(f"Created {path} since it didn't exist.")

    # Process each vocabulary independently with a fresh cache DB so data from
    # previously-loaded vocabularies cannot pollute queries for the current one.
    for index, inputf in enumerate(inputttl):
        voc_uri = inputvocaburi[index]
        print(f"\n=== Processing {inputf} ({voc_uri}) ===")

        _reset_cache_db(cachepath)

        ttl_path = os.path.join(sourcevocabdir, inputf + ".ttl")
        if load_cachedb(ttl_path, cachepath, voc_uri) != 0:
            print(f"load_cachedb had problem processing: {inputf}, {voc_uri}; skipping")
            continue
        print(f"load_cachedb call successful for: {inputf}, {voc_uri}")

        if command == "uijson":
            print("Generating uijson for inclusion in webUI build")
            _run_uijson_in_container(os.path.join(path, inputf + ".json"), voc_uri, cachepath)
        elif command == "docs":
            print("Generating markdown and html docs")
            md_path = os.path.join(path, inputf + ".md")
            result = _run_docs_in_container(md_path, voc_uri, cachepath)
            if result == 0:
                _quarto_render_html(md_path, path)
            else:
                print(f"problem with {inputf}, don't call quarto")
        else:
            print(f"Unknown command {command}.  Exiting.")
            sys.exit(-1)


def _reset_cache_db(cachepath: str):
    """Delete any prior cache DB file so each vocab starts from a clean store.

    navocab's internal purge path is unreliable (see known issues), so we
    remove the file here before re-creating it via vocab.py load.
    """
    cachedir = os.path.dirname(cachepath)
    if cachedir and not os.path.exists(cachedir):
        os.makedirs(cachedir)
    if os.path.exists(cachepath):
        try:
            os.remove(cachepath)
            print(f"Removed stale cache DB: {cachepath}")
        except OSError as e:
            print(f"Could not remove {cachepath}: {e}")


def load_cachedb(inputf, cachepath, voc_uri):
    print(f"cachdb file to load: {inputf}")
    load_args = ["--verbosity", "DEBUG", "-s", cachepath, "load", inputf, voc_uri]
    result = _run_python_in_container("/app/tools/vocab.py", load_args, f="")
    if result == 0:
        print(f"vocab.py.load call successful for {inputf}")
        return 0
    print(f"vocab.py.load had problem processing {inputf}")
    return 1


def _quarto_render_html(markdown_in: str, output_path: str):
    result = subprocess.run(["/opt/quarto/bin/quarto", "render", markdown_in, "-t", "html"])
    if result.returncode == 0:
        print(f"Quarto call successful for {markdown_in}")
        return 0
    print(f"Quarto had problem processing {markdown_in}")
    return 1


def _run_make_in_container(target: str):
    print("In githubActionMain: make in container, target: ", target)
    subprocess.run(["/usr/bin/make", "-C", "/app", "-f", "/app/Makefile", target])


def _run_uijson_in_container(output_path: str, vocab_location: str, cachepath: str):
    with open(output_path, "w") as f:
        vocab_args = ["-s", cachepath, "uijson", vocab_location, "-e"]
        testflag = _run_python_in_container("/app/tools/vocab.py", vocab_args, f)
        if testflag == 0:
            print(f"Run_uijson: Successfully wrote uijson file to {output_path}")
            return 0
        print(f"problem processing {vocab_location}")
        return 1


def _run_docs_in_container(output_path: str, vocab_location: str, cachepath: str):
    with open(output_path, "w") as f:
        docs_args = [cachepath, vocab_location]
        testflag = _run_python_in_container("/app/tools/vocab2mdCacheV2.py", docs_args, f)
        if testflag == 0:
            print(f"Docs in container: Successfully wrote doc file {vocab_location} to {output_path}")
            return 0
        print(f"vocab2mdCacheV2. problem processing {vocab_location}")
        return 1


def _run_python_in_container(path_to_python_script: str, args: list[str], f):
    subprocess_args = [sys.executable, path_to_python_script]
    subprocess_args.extend(args)
    if f == "":
        result = subprocess.run(subprocess_args)
    else:
        result = subprocess.run(subprocess_args, stdout=f)
    return result.returncode


if __name__ == "__main__":
    main()
