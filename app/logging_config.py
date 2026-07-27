import logging

_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")

_console_handler = logging.StreamHandler()
_console_handler.setFormatter(_formatter)

_file_handler = logging.FileHandler("app.log")
_file_handler.setFormatter(_formatter)

logging.basicConfig(level=logging.INFO, handlers=[_console_handler, _file_handler])

logger = logging.getLogger("task_tracker")
