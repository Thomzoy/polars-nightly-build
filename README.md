# Nightly build of Polars's main branch

Each build is available in a dedicated branch named `nightly-YYYYMMDD`, with `YYYYMMDD` being the date of the build

## How to use
```bash
git clone --depth=1 https://github.com/Thomzoy/polars-nighty.git
cd polars-nightly
git fetch --depth=1 --tags
cd YYYYMMDD # insert desired date here
pip install --find-links=. polars
```

## Which builds are available ?

Just check the branch names !
