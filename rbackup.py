#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# rbackup - simple backup script
# Copyright (C) 2018  Ranx

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import shutil
from datetime import datetime

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(name='rbackup', context_settings=CONTEXT_SETTINGS)
@click.argument('source', type=click.Path(exists=True, file_okay=False, resolve_path=True))
@click.option('--dest', '-d', type=click.Path(writable=True, resolve_path=True), help='Destination file or folder',
              required=True)
def main(source, dest):
    click.echo('Source: {} | Destination: {}'.format(
        click.style(click.format_filename(source), fg='yellow'), click.style(click.format_filename(dest), fg='yellow'))
    )
    backup(source, dest)


def backup(source, dest):
    archive = shutil.make_archive(
        os.path.join(dest, '{}_{}'.format(
            os.path.basename(source), datetime.now().strftime('%H.%M_%d.%m.%y'))) if os.path.isdir(dest) else dest,
        'zip',
        source
    )
    click.secho('Successfully backed up!', fg='green')
    click.echo('Archive: {}'.format(click.format_filename(archive)))


if __name__ == '__main__':
    main()
