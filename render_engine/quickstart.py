
import click
from jinja2 import Environment, PackageLoader

import shutil
from pathlib import Path


def create_static_dir (base_dir: str=Path.cwd() : str = "static"):
    """/"""
    Path(base_dir).joinpath(static_dir).mkdir(exist_ok=True)

def create_content_path(base_dir: str=Path.cwd(), content_path: str = "content"):
    """/"""
    Path(base_dir).joinpath(content_path).mkdir(exist_ok=True)

def create_templates_path(
    base_dir: str = Path().cwd()
    include_template_files: bool = True,
    ):
    """
    Create Base Folders for your
    output_dir, static_dir, content_path, and templates_path
    """

    base_dir = Path(base_dir).joinpath('templates')
    templates_path = ''

    if base_template_files:
        return shutil.copytree(, base_dir, dirs_exist_ok=True)

    else:
        return Path(base_dir).joinpath(content_path).mkdir(exist_ok=True)


def create_base_page(
    base_dir: str = "./",
    templates_path: str = "templates",
    ):

    templates_path.joinpath("page.html").touch(exist_ok=True)


def gen_run_template():
    env = Environment(loader=PackageLoader("render_engine", "templates"))
    template = env.get_template("run.txt")
    return template.render()



@click.command()
@click.option('--base-directory', default='./', help='starting directory for your project')
@click.option('--static-path', '-s', default='output', help='directory that rendered HTML files will be saved')
@click.option('--content-path', '-c', default=False, help='directory that rendered HTML files')
@click.option('--blog', prompt='Would you like to create a blog object', help='Add a Blog Object')
@click.option('--microblog', default=True)
@click.option('--pages-directory', prompt='create a separate pages directory in your content path')
@click.option('--no-static-path', '-Xs', default=False, help='If True, do not create a static directory')
@click.option('--no-content-path', '-Xc', default=False, help='If True, do not create a content directory')
def _main(
    base_directory,
    static_path,
    content_path,
    templates_path,
    no_static_path,
    no_content_path,
    blog,
    microblog,
):
    """
    - Create Folders
    - Test Folders Created
    - Test Folders Do Not Overwrite
    - Test Folders Do Not Error if exists already
    """

    click.echo(f"{output_dir=} created")
    click.echo(f"{content_path=} created")
    click.echo(f"{static_dir=} created")
    Path("run.py").write_text(get_run_template)


if __name__ == "__main__":
    typer.run(_main())