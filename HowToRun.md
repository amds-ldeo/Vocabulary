# Setting up and running SKOS to HTML tools 

Notes by Stephen M. Richard 2023-02-27

Based on configuration set up by Dave Vieglais for the iSamples project, https://github.com/isamplesorg/isamplesorg.github.io

## Tools:
•	**Python code**. The code imports import **sys, textwrap, click, rdflib**, and **datetime**. This code reads a turtle file from a URL and writes a markdown file to the stdout.   The markdown uses some special syntax that is interpreted by Quarto for better html rendering. 

•	**Quarto**. Software that converts files from Quarto-flavor Markdown to various output formats. Quarto is ‘built on Pandoc’.   In the course of debugging, I installed both Quarto (https://quarto.org/docs/get-started/) and Pandoc, but I’m not sure I needed to install Pandoc.

•	**Bash shell script**.  The source URL and target file for the markdown output are defined here. The script executes the python code, then runs Quarto on the python output to generate html. Currently the markdown output and the html representation are saved in the same output directory. Note that I added the call to Quarto to render the markdown to html in the loop that does the markdown transformation. In Dave's original workflow, this is a separate step. 

## Workflow
I’m running Windows 11 Home, and managing Python environments using Anaconda. In order to run the Bash shell scripts, I had to get the Windows Subsystem for Linux running, Install Quarto, set up a python environment. Here’s the steps:


- **get 'Windows Subsystem for Linux' (WSL) working**   https://linuxhint.com/run-sh-file-windows/.  Have to change default subsystem to ubuntu 22.04 (defaulted to docker data for some reason)
- **install Quarto**  https://github.com/quarto-dev/quarto-cli/releases/download/v1.2.335/quarto-1.2.335-win.msi
- get **plantuml.jar** (Apache license) from https://plantuml.com/download
copy jar to {plantumlpath}
add PLANTUML_BIN as env variable 
PLANTUML_BIN =  "java -jar {plantumlpath}\plantuml.jar"  (note path with no spaces...). NOTE-- this is likely not necessary since we're not generating any UML, but I installed it when debugging and I'm not sure things work without it...

- At the Anaconda prompt, make python environment (I named it quarto, the name doesn't matter, you just need to remember what you used.). Anaconda is not essential, its just what I use, there are other ways...: 
  - conda create --name quarto
  - activate quarto
  - check that the python dependencies are installed in your python environment; you might need to do some conda installs...

There are lots of ways to manage your files. Here's what I've done. Set up a github repository for the vocabularies. In the github vocabulary repository 
- The **pages** branch that is the source for github.io pages where the vocabulary presentations are accessed; the python code is in a scripts directory on this branch, and the markdown and html representations of the turtle files are in directories on this branch. I have separate directories for different vocabularies.
- The **main** branch contains the source Turtle files. These are the authoritative versions of the vocabulary and any updates should be made based on this branch. 

In Git, checkout the repository containing the vocabulary, and then checkout the pages branch of the vocabulary repository. 

Working in the Quarto python environment, change directories to the scripts directory in the github pages branch. 

Open the shell script (generate_vocab_docs.sh) in a text editor

Configure the source URL for the vocabularies and the target directory for output. The Source has to be accessible via URL. 

- SOURCE_BASE this is the base URL for the directory that contains the turtle files from which the ouput markdown will be generated. If you're working with turtle files in Github, remember to use the 'raw' versions. The path will be something like
"https://raw.githubusercontent.com/{Github organization}/{*your vocabulary repository*}/{*branch that has Turtle files*}/{*subdirectory containing Turtle files*}/"
- SOURCES a list of turtle files that will be processes, Each file name in quotes, spaces separating file names. E.g. ("file1.ttl"  "file2.ttl"  "file3.ttl")

The destination is a local directory accessible from you python enviornment command line.

- DEST_FOLDER  a quoted local file path to a directory where output will be places. I make the pages branch in my vocabulary repo the destination. 

If you want to run Quarto as part of the process, check that this line appears jsut above 'done' in the for loop that transforms the sources:
```quarto render "${DEST_FOLDER}${fname}" --to html```

Don't forget to save and push any updates if you want to use them again. 

Now run the shell script
```scripts>  .\generate_vocab_docs.sh```

If all goes well, the markdown and html files will show up in the destination folder. 


PROBLEMS to be aware of:
- the conversion process fails if there are any non-base ASCII characters in your source files. The GitHUB process that updates the github.io pages is even more sensitive that the python code to special characters.
- If you  update your turtle file and push to github, the raw files don't get updated right away-- it take about 5 minutes for the updates to propagate, so when you are fixing things in the turtle files, you have to wait before regenerating the html.
