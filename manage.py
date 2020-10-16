# coding=utf-8

"""提供命令行操作."""
import click

from views import app


@click.group()
def cli():
    pass


@cli.command()
def runserver():
    """启动后台web服务."""
    app.run()


if __name__ == '__main__':
    cli()
