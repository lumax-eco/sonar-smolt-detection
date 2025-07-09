# Smolt Detection from Sonar Data

A Machine Learning Project for detecting and counting smolts in sonar data.

## Setup

### 🐍 Python dependencies

Install `uv` with `pipx`:

```sh
pipx install uv
```

Create a virtualenv and install the dependencies with `uv`:

```sh
uv sync
```

Activate the `uv` virutalenv:

```sh
source .venv/bin/activate
```

### 🪣 Data dependencies

To get the data dependencies one can use DVC - To fully use this
repository you would need access to our DVC remote storage. On request, you
will be provided with AWS credentials to access our remote storage.

```sh
dvc pull
```

### Large files (Notebooks)

We use `git-lfs` to version and track large files.

Make sure [`git-lfs`](https://git-lfs.com/) is installed on your system.

Run the following command to init `git-lfs` on this repo check:

```sh
git lfs install
```
