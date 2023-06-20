# 🔌 Conda Plugins 🔌

A collection of [conda plugins](https://docs.conda.io/projects/conda/en/latest/dev-guide/plugins/index.html).

To learn about how to implement your own custom plugins, check out our [tutorial template repo](https://github.com/conda/conda-plugin-template).

## Plugins List

<!-- PLUGIN_LIST -->
| &nbsp; | &nbsp; | Name  | Version | Description | Author |
| ----- | ----- | ----- | ----- | ----- | ----- |
| [🏠](https://github.com/conda/conda-libmamba-solver) | [⬇️](https://anaconda.org/main/conda-libmamba-solver) | [`conda-libmamba-solver`][releases-solver] | ![release][shield-solver] | A faster conda solver based on the [mamba project](https://mamba.readthedocs.io/en/latest/). | [@conda/conda-libmamba-solver](https://github.com/conda/conda-libmamba-solver/graphs/contributors) |
| [🏠](https://github.com/conda/conda-lock) | [⬇️](https://anaconda.org/conda-forge/conda-lock) | [`conda-lock`][releases-lock] | ![release][shield-lock] | Generates fully-reproducible lock files for conda environments. | [@conda/conda-lock](https://github.com/conda/conda-lock/graphs/contributors) |
| [🏠](https://github.com/conda/conda-pack) | [⬇️](https://anaconda.org/conda-forge/conda-pack) | [`conda-pack`][releases-pack] | ![release][shield-pack] | Creates relocatable conda environments. | [@conda/conda-pack](https://github.com/conda/conda-pack/graphs/contributors) |
| [🏠](https://github.com/conda/constructor) | [⬇️](https://anaconda.org/anaconda/constructor) | [`constructor`][releases-constructor] | ![release][shield-constructor] | A tool which allows for the construction of an installer for a collection of conda packages. | [@conda/constructor](https://github.com/conda/constructor/graphs/contributors) |
<!-- PLUGIN_LIST -->

[shield-solver]: https://img.shields.io/github/release/conda/conda-libmamba-solver.svg
[shield-pack]: https://img.shields.io/github/v/release/conda/conda-pack.svg
[shield-lock]: https://img.shields.io/github/v/release/conda/conda-lock.svg
[shield-constructor]: https://img.shields.io/github/release/conda/constructor.svg

[releases-solver]: https://github.com/conda/conda-libmamba-solver/releases
[releases-pack]: https://github.com/conda/conda-pack/releases
[releases-lock]: https://github.com/conda/conda-lock/releases
[releases-constructor]: https://github.com/conda/constructor/releases
