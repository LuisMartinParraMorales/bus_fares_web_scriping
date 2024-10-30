"""Console script for bus_fares_web_scriping."""

import click


@click.version_option(package_name="cml_bus_fares_web_scriping")
@click.command()
def cli(args=None):
    """Console script for bus_fares_web_scriping."""
    click.echo(
        "Replace this message by putting your code into bus_fares_web_scriping.cli.cli"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
