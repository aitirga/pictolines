import tensorflow as tf
from pathlib import Path


def hotfix_gpus():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)

        except RuntimeError as e:
            print(e)


def get_root_path():
    return Path(__file__).parent.parent


def get_config_path():
    return get_root_path() / 'config'


def get_project_root():
    return get_root_path().parent

def get_output_path():
    if not os.path.exists(Path.cwd() / 'output'):
        os.mkdir(Path.cwd() / "output")
    return Path.cwd() / 'output'
