import pathlib

import jinja2

from render_engine.plugins import PluginManager

from .page import BasePage


class Archive(BasePage):
    """
    The Archive is a Page object used by the collection that focuses on presenting the Collection's pages.

    Attributes:
        pages (list[BasePage]): The list of pages to include in the archive.
        title (str): The title of the archive.
        template_vars (dict[str, any]): The template variables to use for rendering the archive.
        routes (list[str | pathlib.Path]): The routes for where the archive page should be generated.
        archive_index (int, optional): The index of the page in the series of archive pages. Defaults to 0.
        is_index (bool, optional): Indicates whether the archive is the index page. Defaults to False.
        plugin_manager (PluginManager | None, optional): The plugin manager for the archive. Defaults to None.
        template (str | jinja2.Template, optional): The template to use for rendering the archive.
            Defaults to "archive.html".

    !!! Warning "Not Directly Used"
        The Archive object is not meant to be used directly.
        It is used by the [Collection][src.render_engine.Collection] object.
        Attributes can be used to customize.
    """

    def __init__(
        self,
        title: str,
        pages: list[BasePage],
        template_vars: dict[str, any],
        routes: list[str | pathlib.Path],
        archive_index: int = 0,
        is_index: bool = False,
        plugin_manager: PluginManager | None = None,
        template: str | jinja2.Template = "archive.html",
    ) -> None:
        super().__init__()
        self.slug = title
        self.title = title
        self.archive_index = archive_index
        self.is_index = is_index

        if archive_index:
            self.slug = f"{self._slug}{archive_index}"
        self.pages = pages
        self.plugin_manager = plugin_manager
        self.routes = routes
        self.template = template
        self.template_vars = template_vars
