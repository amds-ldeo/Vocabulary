FROM python:3.12-slim
WORKDIR /app
COPY ./.github/actions/github_action_main.py .
COPY ./tools ./tools

# Vocabulary sources live in per-topic subdirectories (geochemistry/, ETmaterials/, instrumentAll/,
# instruments/). The workflow chooses one via the `vocabdir` input. .dockerignore keeps
# the image small by excluding archives, spreadsheets, PDFs, pre-generated html/, etc.
COPY ./geochemistry ./geochemistry
COPY ./ETmaterials ./ETmaterials
COPY ./instrumentAll ./instrumentAll
COPY ./instruments ./instruments
COPY ./docs  ./docs
COPY ./cache ./cache

# RUN chmod a+x /app/github_action_main.py
RUN chmod a+x /app/github_action_main.py

# Quarto install instructions from https://www.r-bloggers.com/2022/07/how-to-set-up-quarto-with-docker-part-1-static-content/
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gdebi-core \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r /app/tools/requirements.txt

RUN curl -LO https://quarto.org/download/latest/quarto-linux-amd64.deb
RUN gdebi --non-interactive quarto-linux-amd64.deb

ENV PYTHONPATH /app
ENTRYPOINT ["/app/github_action_main.py"]

# This is for debugging the Docker image build process, ensures the container stays up
# ENTRYPOINT ["tail", "-f", "/dev/null"]

