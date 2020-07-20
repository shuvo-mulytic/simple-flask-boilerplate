from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


#-- This can be also done by using `environ.get()`--#
# from os import environ

# NAME_OF_ENV_VAR = environ.get('NAME_OF_ENV_VAR')