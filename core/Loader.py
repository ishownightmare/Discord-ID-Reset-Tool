import importlib 
import pkgutil
import commands 

def load_commands():
    for _, module_name, _ in pkgutil.iter_modules(commands.__path__):
        module = importlib.import_module(f'commands.{module_name}')
        if hasattr(module, 'setup'):
            module.setup()



