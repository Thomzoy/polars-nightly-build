# Nightly build of Polars' main branch
## Usage
To install using pip:

```bash
pip install polars-nightly
```

You can then import polars normaly via `import polars`

## Versioning
The version number appends the build date (e.g. "20240625") to the `polars` version (e.g., "1.1.0"). For instance, to install polars version `1.1.0` built from the main branch on the 25th of June 2024, run:

```bash
pip install "polars-nightly==1.1.0-20240625"
```

## How it works

Each day, the repo's CI
* Fetches the main branch of [polars](https://github.com/pola-rs/polars)
* Builds it
* Pushes everything on this repo, on a branch named "%Y%m%d"
* Add a tag with the same name
* Releases the binaries on [PyPi](https://pypi.org/project/polars-nightly/)
