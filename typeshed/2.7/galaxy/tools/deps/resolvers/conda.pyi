# Stubs for galaxy.tools.deps.resolvers.conda (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from ..resolvers import Dependency, DependencyResolver, InstallableDependencyResolver, ListableDependencyResolver

class CondaDependencyResolver(DependencyResolver, ListableDependencyResolver, InstallableDependencyResolver):
    dict_collection_visible_keys = ...  # type: Any
    resolver_type = ...  # type: str
    versionless = ...  # type: Any
    dependency_manager = ...  # type: Any
    conda_prefix_parent = ...  # type: Any
    ensure_channels = ...  # type: Any
    auto_init = ...  # type: Any
    conda_context = ...  # type: Any
    disabled = ...  # type: Any
    auto_install = ...  # type: Any
    copy_dependencies = ...  # type: Any
    verbose_install_check = ...  # type: Any
    def __init__(self, dependency_manager, **kwds) -> None: ...
    def resolve(self, name, version, type, **kwds): ...
    def list_dependencies(self): ...
    def install_dependency(self, name, version, type, **kwds): ...
    @property
    def prefix(self): ...

class CondaDependency(Dependency):
    dict_collection_visible_keys = ...  # type: Any
    dependency_type = ...  # type: str
    activate = ...  # type: Any
    environment_path = ...  # type: Any
    def __init__(self, activate, environment_path, exact, name: Optional[Any] = ..., version: Optional[Any] = ...) -> None: ...
    @property
    def exact(self): ...
    @property
    def name(self): ...
    @property
    def version(self): ...
    def shell_commands(self, requirement): ...