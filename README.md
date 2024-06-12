# Nightly build of Polars's main branch

Each build is available in a dedicated branch/tag named `nightly-YYYYMMDD`, with `YYYYMMDD` being the date of the build

## How to use
### 1. Using last available build
```bash
git clone --depth=1 https://github.com/Thomzoy/polars-nighty.git
cd polars-nightly
git fetch --depth=1 --tags
LAST_TAG=$(git describe --tags "$(git rev-list --tags --max-count=1)") # Get most recent tag
git checkout tags/$LAST_TAG
pip install --find-links=./dist polars
```

### 2. Using build from a specific date
```bash
git clone --depth=1 https://github.com/Thomzoy/polars-nighty.git
cd polars-nightly
git fetch --depth=1 --tags
git checkout tags/<YYYYMMDD> # insert desired date here
pip install --find-links=./dist polars
```
## Which builds are available ?

Just check the [tags](https://github.com/Thomzoy/polars-nightly/tags) !
