# Snucovery
[![forthebadge](https://forthebadge.com/images/badges/uses-badges.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)

A command line ultility for collecting Aws Service Assets.  This utility is combined with `pyjq`, a python library of the json parser, `jq`.  This allows us to create string based filters to return specific data per service.

# Table of contents

- [Snucovery](#snucovery)
- [Table of contents](#table-of-contents)
- [Usage](#usage)
  - [Installation](#installation)
  - [Updating](#updating)
  - [Testing](#testing)
  - [Uninstallation](#uninstallation)
- [Authors](#authors)
  - [Contributing](#contributing)
- [License](#license)
- [Versioning](#versioning)

# Usage

[(Back to top)](#table-of-contents)

Snucovery is packaged with a command line utility.  Install from `pypi` for easy access.

Once installed, either from `pypi` or locally with `poetry`, usage is as follows:

```sh
snucovery -h
usage: snucovery [-h] -p PROFILE -w WORKBOOK_NAME 

Aws Asset Discovery

optional arguments:
  -h, --help            show this help message and exit
  -p PROFILE, --profile PROFILE
                        An Aws Profile Name that can be set or found in
                        `~/.aws/credentials`
  -w WORKBOOK_NAME, --workbook-name WORKBOOK_NAME
                        Name of the Excel Workbook that will be created
snucovery -p my_aws_profile -w filtered_assets
ls -al ./filtered_assets.xlsx

snucovery -p my_aws_profile

ls -al ./snucovery/Documented_Inventory/Nessus Snucovery Inventory ($Date) ($Time).xlsx
```

## Installation

[(Back to top)](#table-of-contents)

**PyPi**
```sh
pip install snucovery
```

***NOTE***
If you want to install from git, you will need to install [Poetry](https://github.com/sdispater/poetry).

**Source**
```sh
git clone ${REPO}
cd snucovery/
poetry install
```

***NOTE***
You may have a failed installation due to `pyjq` not having the ability to compile correctly.  If so, you need to install `automake`.

**Ubuntu**
```sh
apt update
apt install automake
```

**MacOS**
```sh
brew install automake
```

## Updating

[(Back to top)](#table-of-contents)

**PyPi**
```sh
pip install --upgrade snucovery
```

**Source**
```sh
cd snucovery/
git checkout master
git pull
poetry upgrade
```

## Testing

**Source**
```sh
git clone ${REPO}
cd snucovery/
poetry run pytest
```

By default, the `AwsServices` tests will be skipped.  To run the tests, ensure two things.  First, you need to have a profile name in `~/.aws/credentials` called `test`.  Second, you need to enable integration tests

```sh
export SKIP_INTEGRATION=
poetry run pytest
```

## Uninstallation

[(Back to top)](#table-of-contents)

```sh
pip uninstall snucovery
```

# Authors
[(Back to top)](#table-of-contents)

* **Johnny Martin** - *Initial work* - [iamjohnnym](https://github.com/iamjohnnym)

See also the list of [contributors](https://github.com/socrata-platform/snucovery/contributors) who participated in this project.

## Contributing

[(Back to top)](#table-of-contents)

Your contributions are always welcome! Please have a look at the [contribution guidelines](.github/CONTRIBUTING.md) first.

# License

[(Back to top)](#table-of-contents)

Apache License, Version 2.0 2018 - [Johnny Martin](https://github.com/iamjohnnym/). Please have a look at the [LICENSE.md](LICENSE.md) for more details.

# Versioning
[(Back to top)](#table-of-contents)

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/socrata-platform/snucovery/tags).
