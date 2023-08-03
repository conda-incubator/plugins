# 🔌 Conda Plugins 🔌

A collection of [conda plugins](https://docs.conda.io/projects/conda/en/latest/dev-guide/plugins/index.html).

To learn about how to implement your own custom plugins, check out our [tutorial template repo](https://github.com/conda/conda-plugin-template).

## Plugins List

<!-- PLUGIN_LIST -->
| &nbsp; | &nbsp; | Name  | Version | Description | Author |
| ----- | ----- | ----- | ----- | ----- | ----- |
| [🏠](https://github.com/conda/conda-libmamba-solver) | [⬇️](https://anaconda.org/main/conda-libmamba-solver) | `conda-libmamba-solver` | [![release][libmamba-shield]][libmamba-releases] | A faster conda solver based on the [mamba project][mamba project]. | [@conda/conda-libmamba-solver][libmamba-contributors] |
| [🏠](https://github.com/conda/conda-lock) | [⬇️](https://anaconda.org/conda-forge/conda-lock) | `conda-lock` | [![release][lock-shield]][lock-releases] | Generates fully-reproducible lock files for conda environments. | [@conda/conda-lock][lock-contributors] |
| [🏠](https://github.com/travishathaway/conda-protect) | [⬇️](https://anaconda.org/thath/conda-protect) | `conda-protect` | [![release][protect-shield]][protect-releases] | Protects conda environments to avoid mistakenly modifying them; utilizes the [pre-command plugin hook][pre/post-command blog post]. | [@travishathaway](https://github.com/travishathaway) |
| [🏠](https://github.com/conda/constructor) | [⬇️](https://anaconda.org/anaconda/constructor) | `constructor` | [![release][contructor-shield]][constructor-releases] | A tool which allows for the construction of an installer for a collection of conda packages. | [@conda/constructor][constructor-contributors] |
<!-- PLUGIN_LIST -->

[libmamba-shield]: https://img.shields.io/github/release/conda/conda-libmamba-solver.svg
[libmamba-releases]: https://github.com/conda/conda-libmamba-solver/releases
[libmamba-contributors]: https://github.com/conda/conda-libmamba-solver/graphs/contributors
[mamba project]: https://mamba.readthedocs.io/en/latest/

[lock-shield]: https://img.shields.io/github/v/release/conda/conda-lock.svg
[lock-releases]: https://github.com/conda/conda-lock/releases
[lock-contributors]: https://github.com/conda/conda-lock/graphs/contributors

[protect-shield]: https://img.shields.io/github/v/release/travishathaway/conda-protect.svg
[protect-releases]: https://github.com/travishathaway/conda-protect/releases
[pre/post-command blog post]: https://conda.org/blog/2023-07-31-latest-conda-release-includes-new-plugin-hooks#conda-protect-and-the-pre-command-hook

[contructor-shield]: https://img.shields.io/github/release/conda/constructor.svg
[constructor-releases]: https://github.com/conda/constructor/releases
[constructor-contributors]: https://github.com/conda/constructor/graphs/contributors
