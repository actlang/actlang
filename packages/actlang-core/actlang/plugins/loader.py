import importlib.util, pathlib

PLUGIN_DIR = pathlib.Path.home() / ".actlang" / "tools"

def load_tool(module_name):
    for tool in PLUGIN_DIR.iterdir():
        mod = tool / f"{module_name}.py"
        if mod.exists():
            spec = importlib.util.spec_from_file_location(module_name, mod)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    raise ImportError("Tool not found")
