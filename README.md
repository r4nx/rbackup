# rbackup

rbackup is a simple one-command backup script.

The only command of the script is:
```commandline
rbackup source -d destination
```

The `source` can be only the directory, while `destination` can be either directory or file.

Example usage:
```commandline
rbackup MyFolder -d D:\Backups
```

Note that the paths can be relative and also no extension needed if the destination is a file.

Use `rbackup -h` for the help.
