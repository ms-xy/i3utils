### i3utils

Small python3 helper program leveraging i3-msg.

## CLI

To switch to the workspace that is either named "2" or "2:something" use:

```bash
i3utils switch 2
```

There are two options to set the title of the current workspace.
You can either supply a number for your workspace or let i3utils automatically
reuse any existing workspace number (only the first encountered number is used):

```bash
i3utils title "2: my special workspace with a title"
i3utils title "re-use number '2' for my workspace title"
```

Move the current container to workspace with number 1:

```bash
i3utils moveto 1
```

## GUI

Additionally to the CLI i3utils offers a simple GUI (which consists of only
a text input field).

To start the GUI use the following command (tip: bind it to a key combination
in your window manager for ease of access):

```bash
i3utils ui
```

# GUI Commands

```bash
sleep
suspend
z
```

These three result in putting the system into suspend mode using systemd.

```bash
shutdown
poweroff
```

Result in shutting down the system using systemd.

```bash
reboot
restart
```

Result in restarting the system using systemd.

```bash
display <name> [mode]
display VGA-1 1600x1200
```

If `mode` is `off` then the selected display is disabled. If no mode is supplied
then the preferred mode is selected.

If one display is marked primary, then the new display will be added above the
primary. This is unfortunately the current behaviour. Might be fixed someday ;)

```bash
title <title>
title my workspace
title 2: my workspace
```

Set the workspace title. Works just like the CLI.

### inet

Small python3 helper wrapping around the cumbersome NetworkManager CLI (nmcli).
It is designed to increase workflow speed for a few simple tasks when using
the command line.

Currently only works with pre-defined network connections.

```bash
inet up <connection>
inet down
inet on
inet off
```

The commands should be self-explanatory, really.
Substitute connection with the name of the wanted connection in the
NetworkManager and you're good to go.

If it hangs and you want to interrupt it, you'll have to interrupt twice. That
bug is on my todo list but didn't have time yet ... :P
