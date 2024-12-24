def run_cli():
    from loguru import logger
    import os
    import sys
    import traceback
    from pathlib import Path

    current_path = Path(__file__).parent.parent.resolve()
    sys.path.append(str(current_path))

    chosen_app = os.environ.get('DOCKER_DOWLOG_APP')
    try:
        match chosen_app:
            case 'cli':
                from docker_dowlog.cli import start_app
                start_app()
            case 'web':
                raise NotImplementedError('Web app is not currently implemented')
    except ImportError as e:
        traceback.print_exc()
        logger.error(f'Unable to load libraries: {e}')
        sys.exit(1)


if __name__ == '__main__':
    run_cli()
