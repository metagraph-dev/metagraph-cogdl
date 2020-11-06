############################
# Libraries used as plugins
############################

try:
    import cogdl as _

    has_cogdl = True
except ImportError:
    has_cogdl = False


import metagraph

# Use this as the entry_point object
registry = metagraph.PluginRegistry("metagraph_cogdl")


def find_plugins():
    # Ensure we import all items we want registered
    from . import cogdl

    registry.register_from_modules(cogdl)
    return registry.plugins
