
# Installation

## Setting up a user environment

As a `bus_fares_web_scriping` user, it is easiest to install using the [mamba](https://mamba.readthedocs.io/en/latest/index.html) package manager, as follows:

1. Install mamba with the [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) executable for your operating system.
1. Open the command line (or the "miniforge prompt" in Windows).
1. Create the bus_fares_web_scriping mamba environment: `mamba create -n bus_fares_web_scriping -c conda-forge -c cd web_bus_fares_web_scriping cml_bus_fares_web_scriping`
1. Activate the bus_fares_web_scriping mamba environment: `mamba activate bus_fares_web_scriping`

All together:

--8<-- "README.md:docs-install-user"

### Running the example notebooks

If you have followed the non-developer installation instructions above, you will need to install `jupyter` into your `bus_fares_web_scriping` environment to run the [example notebooks](https://github.com/arup-group/bus_fares_web_scriping/tree/main/examples):

``` shell
mamba install -n bus_fares_web_scriping jupyter
```

With Jupyter installed, it's easiest to then add the environment as a jupyter kernel:

``` shell
mamba activate bus_fares_web_scriping
ipython kernel install --user --name=bus_fares_web_scriping
jupyter notebook
```

### Choosing a different environment name

If you would like to use a different name to `bus_fares_web_scriping` for your mamba environment, the installation becomes (where `[my-env-name]` is your preferred name for the environment):

``` shell
mamba create -n [my-env-name] -c conda-forge --file requirements/base.txt
mamba activate [my-env-name]
ipython kernel install --user --name=[my-env-name]
```

## Setting up a development environment

The install instructions are slightly different to create a development environment compared to a user environment:

--8<-- "README.md:docs-install-dev"

For more detailed installation instructions specific to developing the bus_fares_web_scriping codebase, see our [development documentation][setting-up-a-development-environment].
