import os
import logging
import argparse
import subprocess
import shutil


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def _getPythonExec() -> str:
    return os.path.join(
        "venv",
        "Scripts",
        "python" + ".exe" if os.name == "nt" else "",
    )


def createVirtualEnv(force: bool = False) -> None:
    """
    Used for initializing the dev environment which are called each time the config.py is run.
    The virtual environment is created in the 'venv' directory, if the directory already exists, it will not be recreated.

    Parameters
    ----------
    force : bool
        If True, forces the recreation of the virtual environment even if it already exists. Default is False.
    """

    if os.path.exists("venv"):
        if force:
            logger.info("Forcing recreation of virtual environment...")
            shutil.rmtree("venv")
        else:
            logger.info("Virtual environment already exists.")
            return

    try:
        logger.info("Creating virtual environment...")
        subprocess.run(
            [
                "python",
                "-m",
                "venv",
                "venv",
            ],
            check=True,
            shell=True,
            cwd=os.getcwd(),
        )
        logger.info("Virtual environment created successfully.")

        pythonExec = os.path.join(
            "venv",
            "Scripts",
            "python" + ".exe" if os.name == "nt" else "",
        )

        logger.info("Upgrading pip...")
        subprocess.run(
            [
                pythonExec,
                "-m",
                "pip",
                "install",
                "--upgrade",
                "pip",
            ],
            check=True,
            shell=True,
            cwd=os.getcwd(),
        )

        logger.info("Installing required packages...")
        subprocess.run(
            [
                pythonExec,
                "-m",
                "pip",
                "install",
                "-r",
                "requirements.txt",
            ],
            check=True,
            shell=True,
            cwd=os.getcwd(),
        )
        logger.info("Required packages installed successfully.")
    except Exception as e:
        logger.error(f"Failed to create virtual environment: {e}")


def installPackages(packages: list[str]) -> None:
    """
    Add python dependencies to the virtual environment.

    Parameters
    ----------
    packages : list[str]
        List of packages to install.
    """

    pythonExec = _getPythonExec()

    try:
        logger.info(f"Installing packages: {', '.join(packages)}")
        subprocess.run(
            [
                pythonExec,
                "-m",
                "pip",
                "install",
            ]
            + packages,
            check=True,
            shell=True,
            cwd=os.getcwd(),
        )
        logger.info("Packages installed successfully.")

        logger.info("Updating requirements.txt...")
        subprocess.run(
            [
                pythonExec,
                "-m",
                "pip",
                "freeze",
                ">",
                "requirements.txt",
            ],
            check=True,
            shell=True,
            cwd=os.getcwd(),
        )
    except Exception as e:
        logger.error(f"Failed to install packages: {e}")


def main():
    parser = argparse.ArgumentParser(description="Configuration Parser")

    subparser = parser.add_subparsers(dest="command")

    subparser.add_parser("run", help="Run the application")

    installParser = subparser.add_parser(
        "install",
        help="Install the virtual environment and required packages",
    )

    installParser.add_argument(
        "packages",
        nargs="+",
        help="List of additional packages to install",
    )

    args = parser.parse_args()

    createVirtualEnv()

    if args.command == "run":
        logger.info("Running the application...")
    elif args.command == "install":
        installPackages(args.packages)


if __name__ == "__main__":
    main()
