# Release Notes

Latest stable release: 2.1.1\
Latest nightly release: 2.1.1.15\
Latest alpha release: 3.0.0-alpha-3\
Latest release candidate: 3.0.0-rc-1

Releases are listed from most recent to least recent. All alpha and in-development versions are released to the [epispot-nightly](https://pypi.org/project/epispot-nightly/) project while all other releases are shipped to the [main project](https://pypi.org/project/epispot/).

---

## Version Support

Below is the official list of epispot versions and their support status. If we plan on deprecating a version, there will be a note next to the version listing a date (or approximate date) for when the version will be officially unsupported. The current development version is in bold.

| Version | Patch | Bugfix | Security | Notes |
| ------- | ----- | ------ | -------- | ----- |
| 2.1   | 2.1.1 | ✔️ | ✔️ | Latest stable release |
| 2.0   | 2.0.2 | :x: | ✔️ |
| <= 1.1   | 1.1.0 | :x: | :x: | Deprecated |
| nightly latest   | 2.1.1.15 | :x: | :x: | Deprecated |
| 3.0.0-alpha | 3.0.0a3 | :x: | ✔️ | Suspended (partial support until the release of a stable v3) |
| 3.0.0-rc | 3.0.0rc1 | ✔️ | ✔️ | Supported until release of a stable v3 or another release candidate |
| nightly < latest  | 2.1.1.x | :x: | :x: | Deprecated |

---

## Release Schedule

For epispot v3.0.0:

| Release | Deadline | End of life |
| ------- | ------- | ----------- |
| v3.0.0-alpha-1 | N/A | 12/31/21 |
| v3.0.0-alpha-2 | N/A | 12/31/21 |
| v3.0.0-alpha-3 | 10/18/21 | 12/31/21 |
| ~~v3.0.0-beta~~ | skipped | N/A |
| v3.0.0-rc-1 | released | undecided |
| v3.0.0 | **pending** | LTS |

---

## 3.0.0-rc-1

> **Note**
> No links are available for the changes in this release because development was carried out on an alternate repository in an attempt to completely overhaul the project.
> Additionally, repository history before this release has been cleaned to ensure that the project is in a state that is ready for a stable release.
> All prior changes can be found in the [archive repository](https://github.com/epispot/epispot-archive).

This release marks the first release candidate prior to the official release of v3.0.0.
It is packed with new features and bugfixes intended to be released after intense testing.
It also is a complete overhaul of previous releases in terms of repository structure and aims to maintain most of the same compatibility as the previous alpha releases while modernizing the project for the official v3 release.

Python 3.7 is officially no longer supported, and epispot will no longer undergo CI testing on Python 3.7.
Instead, only Python 3.8, 3.9, and 3.10 will be supported; we plan to support Python 3.11 when it is released.

All documentation has undergone massive changes to ensure that it conforms to a set style guide and also that it is easily understandable.
Still, there is a lot more work to do to ensure that documentation is production-ready, which will be done while epispot v3 is in development.

A new feature now allows users to specify a `delta` parameter in the `Model.integrate()` method for more precise Euler integration.
This allows highly variable models to be plotted with greater accuracy by increasing the number of timesteps within a day.

Perhaps the biggest change feature-wise is the introduction of the `estimates` subpackage.
This subpackage contains a plethora of parameter estimates from the literature that can be used to quickly create new models.
It also integrates with the `params` module so that it can be seamlessly used in all epispot models.
There's also a (not quite complete) `analysis` subpackage for processing raw data and performing statistical analyses.

Speaking of models, they can now be saved to and loaded from files with the `Model.save()` and `Model.load()` methods, respectively.
We use `dill` to do the serialization, which makes all model objects extremely lightweight.

In terms of QA testing, we have added a myriad of new tools to assist with our goal of ensuring ultimate quality.
Among them are `flake8` and `isort`, which work in parallel to automatically identify and fix style issues.
Workflows and tests have also been updated to expand coverage testing and minimize errors.

This is a **huge** release and there are a *lot* of new changes.
We highly encourage you to check them out by reading the documentation [here](https://epispot.github.io/epispot/en/latest/)!
While we develop epispot v3, you can also look at how we're using these features internally at epispot by examining our organization's official [COVID notebook](https://covid-notebook.herokuapp.com).

## 3.0.0-alpha-3

As the third release in the v3-alpha series, this version updates all dependencies and brings Python 3.10 support to epispot.

Epispot will now support all Python versions from 3.7 to 3.10, with our focus being on Python 3.10. [All dependencies have also  been updated](https://github.com/epispot/epispot/pull/113) to ensure compatibility with Python 3.10 and to catch up on missed dependency updates from last release.

Additionally, in minor updates, epispot will be removing unnecessary CI checks (e.g. [DeepSource](https://github.com/epispot/epispot/commit/6119238737e088aceecb99c9bcfc57644f5c322f)) from analyzing non-package files and adding more [detailed summaries for Zenodo uploads](https://github.com/epispot/epispot/commit/95c99a82050e3ed20bdd73567e1d36b6c38bc766/).

Finally, with this release comes a major update to epispot's security policy, which you can view [here](https://github.com/epispot/epispot/blob/master/SECURITY.md). This means that our entire organization will now follow the [Google OSS Vulnerability Guide](https://github.com/google/oss-vulnerability-guide), which will be applied for any security vulnerabilities we find in any epispot versions.

## 3.0.0-alpha-2 (standard-params)

This is the second stage of the v3 release rollout, following [v3.0.0-alpha-1](#300-alpha-1-massive-plots). The major change in this release revolves around solving issue [#73](https://github.com/epispot/epispot/issues/73), which completely redesigns epispot's internals.

In deprecations, we are now officially deprecating the entire `epispot.fitters` module. These changes have been reflected in our [updated documentation](https://epispot.github.io/epispot/en/v3.0.0-alpha-2/fitters.html). New alternatives are expected to arrive soon. Additionally, we've made the decision to officially end support for Python 3.6, following its removal from our testing suite and manifest files (including, finally, `setup.cfg`).

The big news here, of course, are the huge changes to epispot's `Model` and `Compartment` objects. In short, `epispot.models` and `epispot.comps` have been completely redesigned so that each compartment in `epispot.comps` is a sub-compartment of a `Compartment` object, allowing you to create your own custom compartments. Additionally, models now accept the parameters and pass them on to compartments, instead of the other way around. This change is huge and is a large deprecation, so there is a lot to cover. We strongly recommend you read more about this change [here](https://github.com/epispot/epispot/issues/73) or read the new docs.

In minor updates, we've [added support for Dependabot](https://github.com/epispot/epispot/issues/79) and [bumped Numpy to 1.21.1](https://github.com/epispot/epispot/commit/2fb5eff59c3b9d77f22b6dd1f95d34a9ac1bce6c#diff-9a3d09936710783b0cc2e50f54f8cc456be41c432647337fcf9a9391a9e81b98), featuring small performance improvements on the 1.21.0 release. In fact, there's now a `pre-requirements.txt` file to aid manual installation of the epispot package. Additionally, we've [added spellcheck as a routine CI/CD procedure](https://github.com/epispot/epispot/pull/92) on epispot and ensured that our new versions are typo-free. Speaking of CI/CD, we've officially [made the switch *back* from Travis CI to GitHub Actions](https://github.com/epispot/epispot/pull/93) which will give us faster build times and greater reliability. After the first v3 alpha release, we have now also [included alpha releases in our security policy](https://github.com/epispot/epispot/commit/43449d362eab94444a808fb6cedf6f04caee6cf0), so be sure to [check out the new security policy](https://github.com/epispot/epispot/blob/master/SECURITY.md).

Finally, epispot now comes with a
[new built-in sanity check](https://github.com/epispot/epispot/commit/71a70a040b8c60a77e038eb1edee0dda785798ef#diff-3bd065e1fc4a45ad5e94ee148eaf369a81d39db0c3ad4847b0d7323e4fe16a71),
*but it won't run automatically*. This will hopefully increase performance by just a little bit since no checks are being run (unless they are manually invoked).

## 3.0.0-alpha-1 (massive-plots)

This is the first stage of the v3 release rollout. Following this, there will likely be many more `alpha-x` releases. The major changes in this release come from an epispot operation known as `massive-plots`.

Essentially, the main changes are that the `epi.plots` module is now completely updated to feature new, modern graphs using `plotly` for interactive, web-based graphics and `SciencePlots` to create native, scientific charts. Unfortunately, however, `epi.plots.plot_comp_nums` and `epi.plots.compare` are now deprecated. However, new, updated replacements for these can be found in the `epi.plots.native` module.

You can read the documentation for these replacements [here](https://epispot.github.io/epispot/en/v3.0.0-alpha-1/plots/native.html) and the documentation for the new `epi.plots` subpackage [here](https://epispot.github.io/epispot/en/v3.0.0-alpha-1/plots/index.html).
