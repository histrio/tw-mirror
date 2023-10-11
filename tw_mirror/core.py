import logging
import subprocess
import json

logger = logging.getLogger("tw-mirror")


def iter_tasks():
    out = subprocess.check_output(["task", "export"])
    out = json.loads(out)
    for item in out:
        yield item


def out_sync(args) -> str:
    for task in iter_tasks():
        print(task)
